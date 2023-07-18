# Github 업로드
# 경로: Website
# git add .
# git commit -m "edit soruce"
# git push origin main

# import cv2

# image = cv2.imread("lcdrgb", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Test", image)
# cv2.waitKey()
# cv2.destroyAllWindows()

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
        self.loaded_image = None  # Store the loaded image in a class attribute

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
        self.resize(640, 480)

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, '불러올 이미지를 선택하세요', " ", "All Files (*);;")
        if fileName:
            print(fileName)
            src = cv2.imread(fileName)
            self.loaded_image = src  # Store the loaded image in the class attribute
            self.sid = QImage(fileName).scaled(250, 250)
            self.update()  # Trigger a repaint to show the loaded image and histogram

    def drawImage(self, painter):
        painter.drawImage(100, 100, self.sid)
        histogram_pixmap = self.histogram(self.loaded_image).scaled(250, 250)
        painter.drawPixmap(330, 100, histogram_pixmap)

    def histogram(self, image):
        # Use the stored image (self.loaded_image) for histogram calculation
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            result = np.zeros((image.shape[0], 256), dtype=np.uint8)
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
        else:
            # If no image is loaded, return an empty pixmap
            return QPixmap(250, 250)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec_())
