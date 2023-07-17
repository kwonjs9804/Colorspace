import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sid = QImage("lcdrgb.jpg").scaled(220, 220)

        btn = QPushButton("ImageChange", self)
        btn.resize(btn.sizeHint())
        btn.move(20, 250)
        btn.clicked.connect(self.openFileNameDialog)

        self.setGeometry(1400, 250, 520, 400)
        self.show()
# -----------------------------

    # 이미지 출력
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawImage(painter)
        painter.end()

    # 이미지 나란히 출력
    def drawImage(self, painter):
        painter.drawImage(10, 10, self.sid)
        painter.drawImage(self.sid.width() + 20, 10,
                          self.grayScale(self.sid.copy()))

    # 이미지 색변환
    def grayScale(self, image):
        for i in range(self.sid.width()):
            for j in range(self.sid.height()):
                c = image.pixel(i, j)
                gray = qGray(c)
                alpha = qAlpha(c)
                red = qRed(c)
                green = qGreen(c)
                blue = qBlue(c)
                image.setPixel(i, j, qRgba(gray, gray, gray, alpha))
        return image
# --------------------------

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, '불러올 이미지를 선택하세요', " ", "All Files (*);;")

        if fileName:
            print(fileName)
            self.sid = QImage(fileName).scaled(120, 120)


app = QApplication([])
ex = Example()
sys.exit(app.exec_())
