import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 박스 선택 출력
        self.lbl = QLabel('none', self)
        self.lbl.move(100, 80)
        # 불러오기 버튼
        btn1 = QPushButton("load", self)
        btn1.clicked.connect(self.btn_fun_FileLoad)
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
        vbox.addStretch(1)
        vbox.addWidget(cb)
        vbox.addWidget(self.lbl)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
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

    # 이미지 불러오기
    def btn_fun_FileLoad(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', ' ')
        if fname[0]:
            pixmap = QPixmap(fname[0])
            self.label.setPixmap(pixmap)
            self.label.setContentsMargin(10, 50, 10, 10)
            self.label.resizw(pixmap, width(), pixmap.height())
            self.resize(pixmap.width(), pixmap.height())
        else:
            QmessageBox.about(self, '이미지 낫 파운드')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
