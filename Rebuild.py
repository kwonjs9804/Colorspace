import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
import CIE_XYZ_Curve
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.sid = QImage('lcdrgb.jpg')
        self.sid.width = 200
        self.sid.height = 20

        btn = QPushButton("ImageChange", self)
        btn.resize(btn.sizeHint())
        btn.move(260, 50)
        btn.clicked.connect(self.openFileNameDialog)

        self.resize(640, 480)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, '불러올 이미지를 선택하세요', " ", "All Files (*);;")
        if fileName:
            print(fileName)
            self.sid = QImage(fileName).scaled(200, 200)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawImage(painter)
        painter.end()

    def drawImage(self, painter):
        painter.drawImage(100, 100, self.sid)
        # painter.drawImage(self.sid.width() + 100,
        #                   self.histogram())

    def histogram(self, image):
        src = cv2.imread("lcdrgb.jpg")
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        result = np.zeros((src.shape[0], 256), dtype=np.uint8)
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)
        for x, y in enumerate(hist):
            cv2.line(result, (int(x), result.shape[0]), (int(
                x), result.shape[0] - int(y)), 255)
        dst = np.hstack([gray, result])
        return dst

    def SetWaveLengthGraph():
        major_xticks = list(range(400, 800+100, 100))
        minor_xticks = list(range(360-10, 830+10, 20))
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xticks(major_xticks)
        ax.set_xticks(minor_xticks, minor=True)
        ax.set_xlim([360-10, 830+10])
        # ax.tick_params(axis='x', labelsize=20, length=10, width=3, rotation=30)
        # ax.tick_params(axis='x', which='minor', length=5, width=2 )

    def DrawCIE_RGB_Curve():
        SetWaveLengthGraph()
        CIE_RGB_X = np.zeros(CIE_XYZ_Curve.NumOfWavelengths)
        CIE_RGB_Z = np.zeros(CIE_XYZ_Curve.NumOfWavelengths)
        CIE_RGB_Y = np.zeros(CIE_XYZ_Curve.NumOfWavelengths)
        # convert from CIE XYZ color matching function to CIE RGB color matching function
        for i in range(0, CIE_XYZ_Curve.NumOfWavelengths):
            CIE_RGB = np.matmul(CIE_XYZ_Curve.matXYZ_TO_CIE_RGB, [
                                CIE_XYZ_Curve.CIE_X[i], CIE_XYZ_Curve.CIE_Y[i], CIE_XYZ_Curve.CIE_Z[i]])
            CIE_RGB_X[i] = CIE_RGB[0]
            CIE_RGB_Y[i] = CIE_RGB[1]
            CIE_RGB_Z[i] = CIE_RGB[2]
        plt.title('CIE RGB color matching function(CIE RGB Curve)')
        plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_RGB_X, 'r', label='R')
        plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_RGB_Y, 'g', label='G')
        plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_RGB_Z, 'b', label='B')
        plt.legend()
        plt.show()

    def DrawCIE_XYZ_Curve():
        SetWaveLengthGraph()
        plt.title('CIE XYZ color matching function(CIE XYZ Curve)')
        plt.plot(CIE_XYZ_Curve.RangeWavelength,
                 CIE_XYZ_Curve.CIE_X, 'r', label='X')
        plt.plot(CIE_XYZ_Curve.RangeWavelength,
                 CIE_XYZ_Curve.CIE_Y, 'g', label='Y')
        plt.plot(CIE_XYZ_Curve.RangeWavelength,
                 CIE_XYZ_Curve.CIE_Z, 'b', label='Z')
        plt.legend()
        plt.show()

    # main

    print('Number of arguments: {}'.format(len(sys.argv)))
    print('Argument(s) passed: {}'.format(str(sys.argv)))

    selectedCurve = 0
    if (len(sys.argv) > 1):
        selectedCurve = int(sys.argv[1])

    if (selectedCurve == 1):
        DrawCIE_XYZ_Curve()
    else:
        DrawCIE_RGB_Curve()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Project()
    sys.exit(app.exec_())
