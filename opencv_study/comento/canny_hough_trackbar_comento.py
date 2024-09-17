import cv2,sys
import numpy as np
from glob import glob

def on_trackbar(pos):
    global back,src
    ground=back.copy()
    rho = cv2.getTrackbarPos('rho','Trackbar')
    thr = cv2.getTrackbarPos('thr','Trackbar')
    minLeng = cv2.getTrackbarPos('minleng','Trackbar')
    maxGap = cv2.getTrackbarPos('maxgap','Trackbar')
    
    th1=cv2.getTrackbarPos('th1','Trackbar')
    th2=cv2.getTrackbarPos('th2','Trackbar')
    
    dst = cv2.Canny(img, th1, th2, 5)
    src2=cv2.imread('con1.jpg',cv2.IMREAD_GRAYSCALE)
    _,mask=cv2.threshold(src2,150,255,cv2.THRESH_BINARY)
    src=cv2.bitwise_and(dst,dst,mask=mask)

    lines = cv2.HoughLinesP(src, rho=rho, theta=np.pi/180, threshold=thr, minLineLength=minLeng, maxLineGap=maxGap)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(ground, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('Trackbar',ground)

order=0
focus=[]
rho,thr,minLeng,maxGap,th1,th2=1,15,0,2,179,255
pic_list=glob('comento/open/train/*.png') 
while True:
    i = pic_list[order]
    img=cv2.imread(i)
    back=img.copy()
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('Trackbar')
    cv2.createTrackbar('th1','Trackbar',th1,255,on_trackbar)
    cv2.createTrackbar('th2','Trackbar',th2,255,on_trackbar)
    
    cv2.createTrackbar('rho','Trackbar',rho,2,on_trackbar)
    cv2.createTrackbar('thr','Trackbar',thr,200,on_trackbar)
    cv2.createTrackbar('minleng','Trackbar',minLeng,500,on_trackbar) #이미지 크기에 따라
    cv2.createTrackbar('maxgap','Trackbar',maxGap,100,on_trackbar)
    
    key=cv2.waitKey()
    if key==ord(' '):
        if order+1 < len(pic_list):
            order+=1
            rho = cv2.getTrackbarPos('rho','Trackbar')
            thr = cv2.getTrackbarPos('thr','Trackbar')
            minLeng = cv2.getTrackbarPos('minleng','Trackbar')
            maxGap = cv2.getTrackbarPos('maxgap','Trackbar')
            
            th1=cv2.getTrackbarPos('th1','Trackbar')
            th2=cv2.getTrackbarPos('th2','Trackbar')
            
            cv2.destroyAllWindows()
    if key==13:
        focus.append(i)
        if order+1 < len(pic_list):
            order+=1
            rho = cv2.getTrackbarPos('rho','Trackbar')
            thr = cv2.getTrackbarPos('thr','Trackbar')
            minLeng = cv2.getTrackbarPos('minleng','Trackbar')
            maxGap = cv2.getTrackbarPos('maxgap','Trackbar')
            
            th1=cv2.getTrackbarPos('th1','Trackbar')
            th2=cv2.getTrackbarPos('th2','Trackbar')
            
            cv2.destroyAllWindows()
    if key==27:
        cv2.destroyAllWindows()
        break    
    
print(focus)