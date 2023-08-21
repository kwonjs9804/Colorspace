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
        self.loaded_image = None
        self.histogram_image = None

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.ico = QImage('coder.png').scaled(100, 100)
        self.img = QImage('coder.png').scaled(0, 0)
        # 버튼
        btn = QPushButton("ImageChange", self)
        btn.resize(btn.sizeHint())
        btn.move(27, 120)
        btn.clicked.connect(self.openFileNameDialog)

        btn_histogram = QPushButton("Gray Histogram", self)
        btn_histogram.resize(btn_histogram.sizeHint())
        btn_histogram.move(150, 50)
        btn_histogram.clicked.connect(self.gray_histogram)
        # 출력 UI
        self.resize(1020, 640)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawImage(painter)

    def drawImage(self, painter):
        painter.drawImage(40, 20, self.ico)
        painter.drawImage(40, 180, self.img)

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, '불러올 이미지를 선택하세요', " ", "All Files (*);;")
        if fileName:
            print(fileName)
            self.loaded_image = cv2.imread(fileName)
            # 불러온 이미지 원본
            self.img = QImage(fileName).scaledToWidth(250)

    # 흑백/히스토그램
    def gray_histogram(self):
        convertimg = self.loaded_image
        hist = cv2.calcHist([convertimg], [0], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, hist.shape[0], cv2.NORM_MINMAX)
        plt.plot(hist, color='black')
        plt.title('Gray Histogram')
        plt.xlabel('Bins')
        plt.ylabel('Frequency')
        plt.xlim([0, 256])
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec_())
