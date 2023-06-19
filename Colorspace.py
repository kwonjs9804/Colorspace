import cv2

image = cv2.imread(
    "/Users/j_siki/Desktop/HYU/Programming/Colorspace/lcdrgb.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Test", image)
cv2.waitKey()
cv2.destroyAllWindows()
