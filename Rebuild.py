# Github 업로드
# 경로: Website
# git add .
# git commit -m "edit soruce"
# git push origin main

import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loaded_image = None

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.sid = QImage('lcdrgb.jpg')

        # 불러오기 버튼
        btn = QPushButton("ImageChange", self)
        btn.resize(btn.sizeHint())
        btn.move(260, 50)
        btn.clicked.connect(self.openFileNameDialog)

        # 히스토그램 이미지 라벨 적용 후 출력
        self.label = QLabel(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setGeometry(500, 300, self.sid.width() + 200,
                         self.sid.height() + 200)
        # 전체 UI 리사이징
        self.resize(720, 480)

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, '불러올 이미지를 선택하세요', " ", "All Files (*);;")
        if fileName:
            print(fileName)
            src = cv2.imread(fileName)
            self.loaded_image = src
            self.sid = QImage(fileName).scaled(250, 250)

    # 원본 이미지 출력
    def drawImage(self, painter):
        painter.drawImage(20, 100, self.sid)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawImage(painter)
        histogram_image_path = self.histogram(self.sid)
        if histogram_image_path:
            histogram_pixmap = QPixmap(histogram_image_path).scaled(250, 250)
            painter.drawPixmap(250, 100, 500, 250, histogram_pixmap)

    def histogram(self, image):
        if self.loaded_image is not None:
            gray = cv2.cvtColor(self.loaded_image, cv2.COLOR_BGR2GRAY)
            result = np.zeros(
                (self.loaded_image.shape[0], 256), dtype=np.uint8)
            hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
            cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)
            for x, y in enumerate(hist):
                cv2.line(result, (int(x), result.shape[0]), (int(
                    x), result.shape[0] - int(y)), 255)
            dst = np.hstack([gray, result])

            temp_file = tempfile.NamedTemporaryFile(
                suffix=".png", delete=False)
            cv2.imwrite(temp_file.name, dst)
            temp_file.close()

            return temp_file.name
        else:
            print("Image not loaded!")
            return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec_())
