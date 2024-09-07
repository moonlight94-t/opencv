# plt interpolation
# cmap="gray" 이미지가 컬러일 경우 cmap지정안해도 컬러로 출력

import cv2, sys
from matplotlib import pyplot as plt

fileName = "data/cat.jpg"

imgGray=cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray',interpolation='bicubic') # 알아서 interpolation을 해줌 default antialiased
plt.show() #interpolation 이미지 해상도를 키웠을때 공백을 채워줌 기본적으로는 선형 