import cv2,sys
import numpy as np

#ascii 가 없는 키 입력 처리
width, height =512 ,512



#초기 원의 좌표
x,y,R=256,256,50

direction = 0

#main
while True:
    #waitkey + extension키 입력까지 받아들임 , 특수키
    key= cv2.waitKeyEx(30) # timeout(delay)=30ms, imshow전에 키를 먼저해도 상관없음
    if key == 0x1B: #esc(16진수 hexa)
        break
    elif key == 0x270000: #right key #6자리중에 2자리만 씀 waitkey보다 key의 길이가 길기 때문에 더 무거움 
        direction=0
        x+=10
    elif key == 0x280000: #down key
        direction=1
        y+=10
    elif key == 0x250000: #left key
        direction =2
        x-=10
    elif key == 0x260000: #up key
        direction=3
        y-=10
    
    img=np.ones((width,height,3),np.uint8)*255
    cv2.circle(img,(x,y),R,(0,0,255),-1) # -1 안이 채워져있다.
    cv2.imshow('frame',img)
    
    #경계코드 추가
    
    
cv2.destroyAllWindows()