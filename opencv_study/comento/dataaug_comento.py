import cv2
import numpy as np

# 배경 이미지 불러오기
background = cv2.imread('newimage2.png')

# 잘라낸 차량 이미지 불러오기
car = cv2.imread('cropped_scissor.png')
car = cv2.resize(car, (720,390))

# 차량 이미지를 배경 위에 붙일 좌표 설정
x, y = -250, 70  # 배경 위에 차량을 붙일 좌표 #-20,40

# 차량 이미지의 마스크 만들기 (배경 제거를 위한)
car_gray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(car_gray, 20, 255, cv2.THRESH_BINARY)
translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
height, width = mask.shape[:2]
car=cv2.warpAffine(car, translation_matrix, (width, height))
mask = cv2.warpAffine(mask, translation_matrix, (width, height))

# 마스크의 반전 이미지 (배경만 남기기 위한)
mask_inv = cv2.bitwise_not(mask)

# 배경에서 차량이 들어갈 부분만 남김
background_roi = cv2.bitwise_and(background, background, mask=mask_inv)

# 차량 이미지에서 차량 부분만 남김
car_fg = cv2.bitwise_and(car, car, mask=mask)

# 배경과 차량 이미지를 합성
result = cv2.add(background_roi, car_fg)

cv2.imwrite('newimage3.png',result)
# 결과 출력
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()