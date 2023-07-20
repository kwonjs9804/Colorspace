import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tempfile
import os  # os 모듈을 추가해줍니다.
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loaded_image = None

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.sid = QImage('coder.png').scaled(100, 100)
        self.img = QImage('coder.png').scaled(0, 0)
        # 불러오기 버튼
        btn = QPushButton("ImageChange", self)
        btn.resize(btn.sizeHint())
        btn.move(27, 120)
        btn.clicked.connect(self.openFileNameDialog)
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
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, '불러올 이미지를 선택하세요', " ", "All Files (*);;", options=options)

        if fileName:
            print(fileName)
            src = cv2.imread(fileName)
            self.loaded_image = src
            # 불러온 이미지 원본
            self.img = QImage(fileName).scaledToWidth(250)

    # 불러온 이미지와 흑백, 히스토그램 배치
    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawImage(painter)
        histogram_image = self.gray_histogram(self.img)
        if histogram_image:
            histogram_pixmap = QPixmap(histogram_image
                                       ).scaledToWidth(500)
            painter.drawPixmap(300, 40, histogram_pixmap)
            # drawPixmap(x, y, width, height)

    # 흑백/히스토그램
    def gray_histogram(self, image):
        if self.loaded_image is not None:
            self.img = self.loaded_image
            hist = cv2.calcHist([self.img], [0], None, [256], [0, 256])
            cv2.normalize(hist, hist, 0, hist.shape[0], cv2.NORM_MINMAX)
            plt.plot(hist)

            # 이미지 출력 후에 temp_file 삭제
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.close()
            cv2.imwrite(temp_file.name, self.loaded_image)
            os.remove(temp_file.name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec_())
