import cv2,sys
from glob import glob

#img2=cv2.imread('comento/syn_06478.png')


def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min','Trackbar')
    hmax = cv2.getTrackbarPos('H_max','Trackbar')
    smin = cv2.getTrackbarPos('S_min','Trackbar')
    smax = cv2.getTrackbarPos('S_max','Trackbar')
    vmin = cv2.getTrackbarPos('V_min','Trackbar')
    vmax = cv2.getTrackbarPos('V_max','Trackbar')
    
    # inrange함수 적용
    dst = cv2.inRange(img, (hmin,smin,vmin),(hmax,smax,vmax))
    cv2.imshow('Trackbar',dst)
    
#cv2.namedWindow('Trackbar')
#cv2.imshow('Trackbar', src) #이게 왜 필요한거야?

# 트랙바 생성 'H_min' 트랙바이름, 0~180범위 
# 트랙바를 움직일때 호출되는 함수 call-back함수 어떤 이벤트가 발생했을때 이벤트에 따라 호출되는 함수
# cv2.createTrackbar('H_min','Trackbar',0,255,on_trackbar)
# cv2.createTrackbar('H_max','Trackbar',15,255,on_trackbar)
# cv2.createTrackbar('S_min','Trackbar',0,255,on_trackbar)
# cv2.createTrackbar('S_max','Trackbar',15,255,on_trackbar)
# cv2.createTrackbar('V_min','Trackbar',235,255,on_trackbar)
# cv2.createTrackbar('V_max','Trackbar',255,255,on_trackbar)
pic_list=glob('comento/open/train/*.png')
order=0
focus=[]
hmin, hmax,smin,smax,vmin,vmax= 0,15,0,15,235,235
while True:
    i = pic_list[order]
    img=cv2.imread(i)
    #img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.namedWindow('Trackbar')
    cv2.createTrackbar('H_min','Trackbar',hmin,255,on_trackbar)
    cv2.createTrackbar('H_max','Trackbar',hmax,255,on_trackbar)
    cv2.createTrackbar('S_min','Trackbar',smin,255,on_trackbar)
    cv2.createTrackbar('S_max','Trackbar',smax,255,on_trackbar)
    cv2.createTrackbar('V_min','Trackbar',vmin,255,on_trackbar)
    cv2.createTrackbar('V_max','Trackbar',vmax,255,on_trackbar)  
    #cv2.imshow('Trackbar',img2)
    key=cv2.waitKey()

    if key==ord(' '):
        if order+1 < len(pic_list):
            order+=1
            hmin = cv2.getTrackbarPos('H_min','Trackbar')
            hmax = cv2.getTrackbarPos('H_max','Trackbar')
            smin = cv2.getTrackbarPos('S_min','Trackbar')
            smax = cv2.getTrackbarPos('S_max','Trackbar')
            vmin = cv2.getTrackbarPos('V_min','Trackbar')
            vmax = cv2.getTrackbarPos('V_max','Trackbar')
            cv2.destroyAllWindows()
    if key==13:
        focus.append(i)
        if order+1 < len(pic_list):
            order+=1
            hmin = cv2.getTrackbarPos('H_min','Trackbar')
            hmax = cv2.getTrackbarPos('H_max','Trackbar')
            smin = cv2.getTrackbarPos('S_min','Trackbar')
            smax = cv2.getTrackbarPos('S_max','Trackbar')
            vmin = cv2.getTrackbarPos('V_min','Trackbar')
            vmax = cv2.getTrackbarPos('V_max','Trackbar')
            cv2.destroyAllWindows()
    if key==27:
        cv2.destroyAllWindows()
        break
            
print(focus)