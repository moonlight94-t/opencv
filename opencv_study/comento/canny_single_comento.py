import cv2,sys
import numpy as np

src=cv2.imread('comento/syn_06469.png')

img=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY) #이 gray논리가 모두 다 적용될 것인가
asize=5
#canny
def on_trackbar(pos):
    global dst
    th1 = cv2.getTrackbarPos('th1','frame')
    th2 = cv2.getTrackbarPos('th2','frame')
    
    # inrange함수 적용
    dst = cv2.Canny(img2, th1, th2, asize)
    cv2.imshow('frame',dst)
 
img2=cv2.GaussianBlur(img,(5,5),0)   
cv2.namedWindow('frame')

cv2.createTrackbar('th1','frame',97,255,on_trackbar)
cv2.createTrackbar('th2','frame',250,255,on_trackbar)

cv2.imshow('frame',img2)
#cv2.imshow('frame2',img)
while True:
    key=cv2.waitKey()
    if key==ord(' '):
        if asize==3:
            asize=5
            print('5')
        elif asize==5:
            asize=7
            print('7')
        else:
            asize=3
            print('3')
    if key==13:
        cv2.imwrite('test1.jpg',dst)
    if key==27:
        cv2.destroyAllWindows()
        break

src2=cv2.imread('con1.jpg',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(src2,150,255,cv2.THRESH_BINARY)
src_masked=cv2.bitwise_and(dst,dst,mask=mask)

cv2.imshow('frame3',src_masked)
key=cv2.waitKey()
if key==13:
    cv2.imwrite('test1.jpg',src_masked)
cv2.destroyAllWindows()