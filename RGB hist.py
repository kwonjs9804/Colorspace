import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lcdrgb.png', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()


img = cv2.imread('lcdrgb.png')

channels = cv2.split(img)
colors = ['b', 'g', 'r']
for ch, color in zip(channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.show()
