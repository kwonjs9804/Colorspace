import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('BG.png')
imageresize = cv2.resize(image, dsize=(512, 512))
for i in range(0, 30):
    circle = cv2.circle(imageresize, (213, 130), 10, (0, 0, 255), 3)
# point = cv2.line(imageresize, (130, 130), (130, 130), 10)
# imageresize_2 = cv2.resize(image_2, dsize=(256, 256))

result = imageresize + circle
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()

# # result = imageresize, point
# # plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# # plt.show()
