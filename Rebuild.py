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
        self.sid = QImage('coder.png').scaled(100, 100)
        self.img = QImage('coder.png').scaled(0, 0)
        # 불러오기 버튼
        btn = QPushButton("ImageChange", self)
        btn.resize(btn.sizeHint())
        btn.move(27, 120)
        btn.clicked.connect(self.openFileNameDialog)

        btn_histogram = QPushButton("Show Histogram", self)
        btn_histogram.resize(btn_histogram.sizeHint())
        btn_histogram.move(27, 150)
        btn_histogram.clicked.connect(self.gray_histogram)

        # 전체 UI 리사이징
        self.resize(1020, 640)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # 원본 이미지 출력
    def drawImage(self, painter):
        painter.drawImage(40, 20, self.sid)
        painter.drawImage(40, 180, self.img)

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, '불러올 이미지를 선택하세요', " ", "All Files (*);;")
        if fileName:
            print(fileName)
            src = cv2.imread(fileName)
            self.loaded_image = src
            # 불러온 이미지 원본
            self.img = QImage(fileName).scaledToWidth(250)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawImage(painter)
        if self.histogram_image:
            histogram_pixmap = QPixmap(self.histogram_image).scaledToWidth(500)
            painter.drawPixmap(300, 40, histogram_pixmap)

    # 흑백/히스토그램
    def gray_histogram(self, image):
        if self.loaded_image is not None:
            self.img = self.loaded_image
            hist = cv2.calcHist([self.img], [0], None, [256], [0, 256])
            cv2.normalize(hist, hist, 0, hist.shape[0], cv2.NORM_MINMAX)
            plt.plot(hist)
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
