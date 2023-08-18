import cv2
import numpy as np
import matplotlib.pyplot as plt
from coordinate import point_x, point_y


image = cv2.imread('BG.png')
imageresize = cv2.resize(image, dsize=(512, 512))

a = int(point_x)
b = int(point_y)

for i in range(0, 30):
    circle = cv2.circle(imageresize, (a, b), 10, (0, 0, 255), 3)

result = imageresize
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()
