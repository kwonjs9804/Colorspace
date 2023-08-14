import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('BG.png')
imageresize = cv2.resize(image, dsize=(512, 512))
for i in range(0, 30):
    circle = cv2.circle(imageresize, (156, 230), 2, (0, 0, 255), 10)

result = imageresize + circle
plt.show(result)


# result = imageresize + circle
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.show([image], [circle])

# # result = imageresize, point
# # plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# # plt.show()
