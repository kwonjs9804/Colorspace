import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Project(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    # 이미지 불러오기
    def openFileNameDialog(self):
        filename = QFileDialog.getOpenFileName(
            self, '이미지 불러오기', ' ')

        if fileName:
            print(fileName)
            self.sid = QImage(fileName).scaled(120, 120)

        # if filename[0]:
        #     pixmap = QPixmap(filename[0])
        #     self.label.setPixmap(pixmap)
        #     self.label.setContentsMargin(10, 50, 10, 10)
        #     self.label.resizw(pixmap, width(), pixmap.height())
        #     self.resize(pixmap.width(), pixmap.height())
        # else:
        #     messagebox.about(self, '이미지 낫 파운드')

    def initUI(self):
        self.sid = QImage("lcdrgb.jpg").scaled(220, 220)

        btn = QPushButton("load", self)
        btn.clicked.connect(self.openFileNameDialog)

        btn = QPushButton("ImageChange", self)
        btn.resize(btn.sizeHint())
        btn.move(20, 250)
        btn.clicked.connect(self.openFileNameDialog)

    #     self.setGeometry(1400, 250, 520, 400)
    #     self.show()

        # 박스 및 항목
        cb = QComboBox(self)
        cb.addItem('Original')
        cb.addItem('Greyscale')
        cb.addItem('RGB')
        cb.addItem('CMYK')
        cb.move(50, 50)
        cb.activated[str].connect(self.onActivated)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(cb)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)
        self.setWindowTitle('Colorspace')
        self.resize(400, 200)
        self.center()
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    # 가운데 정렬
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# -------------------------

    # 이미지 출력


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawImage(painter)
        painter.end()

    # # 이미지 나란히 출력
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    sys.exit(app.exec_())
