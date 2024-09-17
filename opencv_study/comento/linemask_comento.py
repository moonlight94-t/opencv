import cv2, sys
import numpy as np
from glob import glob

src= cv2.imread('comento/syn_06469.png')

myli=glob('redblue/*.jpg')
con1=np.ones((1040,1920),np.uint8)*0
con2=np.ones((1040,1920),np.uint8)*0
for i in myli:
    img=cv2.imread(i)
    red = cv2.inRange(img, (0,0,235),(15,15,255))
    blue = cv2.inRange(img, (205,0,0),(255,15,15))
    con1 = cv2.bitwise_or(con1,red)
    con2 = cv2.bitwise_or(con2,blue)
    
pt1 = []
pt2 = []
def mouse_callback(event, x, y, flags, param):
    global pt1,pt2 #없어도 잘 작동하는데?
    if event==cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_ALTKEY:
            pt4=np.array(pt2)
            cv2.fillPoly(param[0],[pt4],color=255)
            pt2=[]
            
        else:
            pt2.append([x,y])
    
    if event==cv2.EVENT_RBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_ALTKEY:
            pt3=np.array(pt1)
            cv2.fillPoly(param[0],[pt3],color=255)
            pt1=[]
            
        else:
            pt1.append([x,y])
    
    cv2.imshow('img',param[0])
        
for i in [con1, con2]:
    if i is None:
        sys.exit('load fail')
    
    cv2.namedWindow('img')
    cv2.setMouseCallback('img',mouse_callback, [i])
    cv2.imshow('img',i)
    key=cv2.waitKey()
    if key == ord(' '):
        cv2.imwrite("con1.jpg",i)
    cv2.destroyAllWindows()


# masking





# canny edge