# cv2.normalize

import cv2, sys
import numpy as np

src=cv2.imread('data2/Hawkes.jpg',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')
    
pixmin, pixmax,a,b = cv2.minMaxLoc(src) # a,b 최소 최대 위치 , 113 213 차이가 얼마 안나서 이미지가 뿌옇게 보이는것 대비를 크게 해서 이미지를 선명하게 만들겠다는 논리(분산을 크게해서)

# 이미지 정규화
dst = cv2.normalize(src,None,0,255,cv2.NORM_MINMAX) #dst인수로 넣으면 정의가 안되어있으니까 None 그냥 ret으로 받음 
# 없는 정보를 만드는것이 아니라 정보간격을 최대한 벌려서(분포를 바꾸어서) 사람눈으로 식별 용이하게 만듬

cv2.imwrite('data2/Hawkes_norm.jpg',dst)

cv2.imshow('frame1',src)
cv2.imshow('frame2',dst)
cv2.waitKey()
cv2.destroyAllWindows()