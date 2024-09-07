import sys
import numpy as np
import cv2

# 트랙바 콜백함수 생성
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min','Trackbar')
    hmax = cv2.getTrackbarPos('H_max','Trackbar')
    smin = cv2.getTrackbarPos('S_min','Trackbar')
    smax = cv2.getTrackbarPos('S_max','Trackbar')
    vmin = cv2.getTrackbarPos('V_min','Trackbar')
    vmax = cv2.getTrackbarPos('V_max','Trackbar')
    
    # inrange함수 적용
    dst = cv2.inRange(src_hsv, (hmin,smin,vmin),(hmax,smax,vmax))
    cv2.imshow('Trackbar',dst)


#src = cv2.imread('red.jpg') # (0,155,50),(10,255,255)
#src = cv2.imread('yellow.jpg') # (15,110,50),(50,255,255)
#src = cv2.imread('green.jpg') # (40,155,50),(80,255,255)
src= cv2.imread('traffic.png')

if src is None:
    sys.exit("Image Load Failed")
    
# 색상의 범위를 잘 지정하려면 bgr->hsv

src_hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

# 창에 트랙바를 넣기 위해서 창을 생성
cv2.namedWindow('Trackbar')
#cv2.imshow('Trackbar', src) #이게 왜 필요한거야?

# 트랙바 생성 'H_min' 트랙바이름, 0~180범위 
# 트랙바를 움직일때 호출되는 함수 call-back함수 어떤 이벤트가 발생했을때 이벤트에 따라 호출되는 함수
cv2.createTrackbar('H_min','Trackbar',0,180,on_trackbar)
cv2.createTrackbar('H_max','Trackbar',180,180,on_trackbar)
cv2.createTrackbar('S_min','Trackbar',0,255,on_trackbar)
cv2.createTrackbar('S_max','Trackbar',255,255,on_trackbar)
cv2.createTrackbar('V_min','Trackbar',0,255,on_trackbar)
cv2.createTrackbar('V_max','Trackbar',255,255,on_trackbar)


# 초기값
on_trackbar(0)

cv2.waitKey()
cv2.destroyAllWindows()