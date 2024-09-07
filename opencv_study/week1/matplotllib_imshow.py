# 이미지 출력 cv2.imshow() -> plt.imshow()

import cv2
import sys
from matplotlib import pyplot as plt

fileName="data/cat.jpg"

img=cv2.imread(fileName)

if img is None:
    sys.exit("Image Load is failed")
    
# opencv module은 color space 순서 B G R 
# matplotlib은 R G B 

# color space를 바꿔주는 함수 채널순서도 바꾸어줌
cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img) #창에 그림을 넣는 것
plt.axis('off') # xy pixel 좌표 끔
plt.show()