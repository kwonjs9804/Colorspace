import cv2

# 이미지를 그레이스케일로 읽어옴
image = cv2.imread('White.png', cv2.IMREAD_COLOR)
b, g, r = cv2.split(image)
inverse = cv2.merge((r, g, b))

# 히스토그램 계산
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])

# 픽셀 값과 개수를 가중 평균하여 평균값 계산
total_pixels_r = r.shape[0] * r.shape[1]  # 이미지의 전체 픽셀 수
sum_value_r = 0
total_pixels_g = g.shape[0] * g.shape[1]  # 이미지의 전체 픽셀 수
sum_value_g = 0
total_pixels_b = b.shape[0] * b.shape[1]  # 이미지의 전체 픽셀 수
sum_value_b = 0

for i in range(len(hist_r)):
    sum_value_r += i * hist_r[i]
for j in range(len(hist_g)):
    sum_value_g += j * hist_g[j]
for k in range(len(hist_b)):
    sum_value_b += k * hist_b[k]

mean_value_r = sum_value_r / total_pixels_r
print("R:", mean_value_r)
mean_value_g = sum_value_g / total_pixels_g
print("G:", mean_value_g)
mean_value_b = sum_value_b / total_pixels_b
print("B:", mean_value_b)
