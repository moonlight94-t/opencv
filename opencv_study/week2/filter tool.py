#filter tool
#2차원 커널을 가지고 직접 계산하는 방식

import cv2,sys
import numpy as np

src=cv2.imread('../data2/rose.bmp',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('load fail')
    
# 사용자 커널(필터) 생성 - cnn에서 가중치는 커널임
kernal = np.ones((3,3),dtype=np.float32)/9 #9개니까 9로 나누어줌 아마 밝기 유지의미
#-1 은 입력영상과 동일한 데이터 타입으로 출력하겠다 는 의미 = size가 동일하다
kernal1=np.array([[-2,-1,0],[-1,1,1],[0,1,2]]) #embossing kernal
dst= cv2.filter2D(src,-1,kernal1)
dst2= cv2.blur(src,(3,3)) # 위와 거의 비슷

cv2.imshow('frame',dst)
cv2.imshow('frame2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()