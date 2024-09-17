import cv2,sys
import numpy as np
from glob import glob

asize=5
#canny
def on_trackbar(pos):
    global dst
    th1 = cv2.getTrackbarPos('th1','frame')
    th2 = cv2.getTrackbarPos('th2','frame')
    dst = cv2.Canny(img, th1, th2, asize)
    cv2.imshow('frame',dst)
 

order=0
focus=[]
pic_list=glob('comento/open/train/*.png')
th1=179
th2=255
while True:
    i = pic_list[order]
    img=cv2.imread(i,cv2.IMREAD_GRAYSCALE)
    
    cv2.namedWindow('frame')
    cv2.createTrackbar('th1','frame',th1,255,on_trackbar)
    cv2.createTrackbar('th2','frame',th2,255,on_trackbar)
    
    key=cv2.waitKey()
    if key==ord(' '):
        if order+1 < len(pic_list):
            order+=1
            th1 = cv2.getTrackbarPos('th1','frame')
            th2 = cv2.getTrackbarPos('th2','frame')
            cv2.destroyAllWindows()
    if key==13:
        focus.append(i)
        if order+1 < len(pic_list):
            order+=1
            th1 = cv2.getTrackbarPos('th1','frame')
            th2 = cv2.getTrackbarPos('th2','frame')
            cv2.destroyAllWindows()
    if key==27:
        cv2.destroyAllWindows()
        break    
    
#src2=cv2.imread('con1.jpg',cv2.IMREAD_GRAYSCALE)
# _,mask=cv2.threshold(src2,150,255,cv2.THRESH_BINARY)
#     src_masked=cv2.bitwise_and(,dst,mask=mask)
#     img=cv2.bitwise_and(img,img,mask=)