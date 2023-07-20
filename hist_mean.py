import cv2

# 이미지를 그레이스케일로 읽어옴
image = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)

# 히스토그램 계산
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# 픽셀 값과 개수를 가중 평균하여 평균값 계산
total_pixels = image.shape[0] * image.shape[1]  # 이미지의 전체 픽셀 수
sum_value = 0

for i in range(len(hist)):
    sum_value += i * hist[i]

mean_value = sum_value / total_pixels
print("평균값:", mean_value)
