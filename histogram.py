# from PyQt5.QtWidgets import QLabel, QApplication, QVBoxLayout, QWidget
# from PyQt5.QtGui import QImage, QPixmap
# import cv2
# import numpy as np

# src = cv2.imread("lcdrgb.jpg")
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# result = np.zeros((src.shape[0], 256), dtype=np.uint8)

# hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)

# for x, y in enumerate(hist):
#     cv2.line(result, (int(x), result.shape[0]), (int(
#         x), result.shape[0] - int(y)), 255)

# dst = np.hstack([gray, result])

# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ----------------------------------------------------------------

import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QApplication, QVBoxLayout, QWidget


class ImageHistogramApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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

        pixmap = QPixmap.fromImage(qimage)
        label = QLabel(self)
        label.setPixmap(pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(label)

        self.setLayout(layout)
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle('Image with Histogram')
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = ImageHistogramApp()
    sys.exit(app.exec_())
