import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp',cv2.IMREAD_GRAYSCALE) # 필터처리할때 윤곽선을 찾음? 그래서 그레이스케일로 윤곽선 따냄 

if src is None:
    sys.exit('failed')
    
#blur 처리

dst = cv2.blur(src,(3,3)) # 필터의 크기가 3x3 , 이것을 보통 많이 씀 -> 계산량 , 필터사이즈를 키우면 blurring이 심해짐 , 보통 정사각형을 많이씀
dst2 = cv2.blur(src,(5,5))
gst = cv2.GaussianBlur(src,(0,0),3) # 노이즈 제거에 용이함 sigma로 blurring 조절

cv2.imshow('frame',src)
cv2.imshow('frame2',dst)
cv2.imshow('frame3',dst2)
cv2.waitKey()
cv2.destroyAllWindows()
