import cv2,sys
import numpy as np


pt1 = []
pt2 = []
def mouse_callback(event, x, y, flags, param):
    global pt1,pt2 #없어도 잘 작동하는데?
    if event==cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_ALTKEY:
            pt4=np.array(pt2)
            cv2.fillPoly(img,[pt4],color=(240,0,0))
            pt2=[]
            
        else:
            pt2.append([x,y])
    
    if event==cv2.EVENT_RBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_ALTKEY:
            pt3=np.array(pt1)
            cv2.fillPoly(img,[pt3],color=(0,0,240))
            pt1=[]
            
        else:
            pt1.append([x,y])
    
    cv2.imshow('img',img)
        
img = cv2.imread('comento/syn_06478.png') #1920x1040

if img is None:
    sys.exit('load fail')
   
cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse_callback, [img])
cv2.imshow('img',img)
key=cv2.waitKey()
if key == ord(' '):
    cv2.imwrite('06478.jpg',img)
cv2.destroyAllWindows()