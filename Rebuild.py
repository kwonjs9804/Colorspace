# Github 업로드
# 경로: Website
# git add .
# git commit -m "edit soruce"
# git push origin main

import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.sid = QImage('lcdrgb.jpg')

        btn = QPushButton("ImageChange", self)
        btn.resize(btn.sizeHint())
        btn.move(260, 50)
        btn.clicked.connect(self.openFileNameDialog)

        self.label = QLabel(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setGeometry(500, 300, self.sid.width() + 200,
                         self.sid.height() + 200)
        self.resize(640, 480)

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
            self.sid = QImage(fileName).scaled(250, 250)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawImage(painter)
        histogram_pixmap = self.histogram(self.sid).scaled(250, 250)
        painter.drawPixmap(330, 100, 250, 250, histogram_pixmap)

    def drawImage(self, painter):
        painter.drawImage(100, 100, self.sid)

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

        height, width = dst.shape
        bytesPerLine = 3 * width
        qimage = QImage(dst.data, width, height, bytesPerLine,
                        QImage.Format_RGB888).rgbSwapped()

        return QPixmap.fromImage(qimage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec_())
