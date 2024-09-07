# inrange함수를 잘 설정하려면 trackbar 기능 필요

import sys
import numpy as np
import cv2

# 트랙바 콜백함수 생성
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min','Trackbar') #마우스 입력을 받아서 트랙바의 위치값을 읽어옴
    hmax = cv2.getTrackbarPos('H_max','Trackbar')
    
    # inrange함수 적용
    dst = cv2.inRange(src_hsv, (hmin,150,0),(hmax,255,255)) # 이거 전역변수 설정 헷갈린다?
    cv2.imshow('Trackbar',dst)


src = cv2.imread('data2/candies.png')

if src is None:
    sys.exit("Image Load Failed")
    
# 색상의 범위를 잘 지정하려면 bgr->hsv

src_hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

# 창에 트랙바를 넣기 위해서 창을 생성
cv2.namedWindow('Trackbar')
#cv2.imshow('Trackbar', src) 이게 왜 필요한거야?

# 트랙바 생성 'H_min' 트랙바이름, 0~180범위 
# 트랙바를 움직일때 호출되는 함수 call-back함수 어떤 이벤트가 발생했을때 이벤트에 따라 호출되는 함수
cv2.createTrackbar('H_min','Trackbar',0,180,on_trackbar)
cv2.createTrackbar('H_max','Trackbar',0,180,on_trackbar)

# 초기값
on_trackbar(0)

cv2.waitKey()
cv2.destroyAllWindows()