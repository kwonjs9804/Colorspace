# Github 업로드
# 경로: Website
# git add .
# git commit -m "edit soruce"
# git push origin main

import cv2

image = cv2.imread("lcdrgb", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Test", image)
cv2.waitKey()
cv2.destroyAllWindows()
