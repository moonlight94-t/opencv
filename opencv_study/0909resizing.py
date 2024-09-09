import cv2,sys
import numpy as np


pt1 = []
def mouse_callback(event, x, y, flags, param):
    global pt1
    
    if event==cv2.EVENT_LBUTTONDOWN: #if문 먼저확인하는 논리 실행순서
        if flags & cv2.EVENT_FLAG_ALTKEY:
            cv2.imwrite('resizing.jpg',img)
        else:
            cv2.circle(param[0],(x,y),50,(0,0,255),1)
    
    if event==cv2.EVENT_RBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_ALTKEY:
            pt2=np.array(pt1)
            cv2.polylines(img,[pt2], isClosed=True,color=(255,0,0),thickness=1)
            pt1=[]
            
        else:
            pt1.append([x,y])
    
    cv2.imshow('img',img)
        
img = np.ones((512,512,3),np.uint8)*255

cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse_callback, [img])
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()


blured=cv2.blur(img, (7,7), 0)

dst1=cv2.resize(blured,(128,128),interpolation=cv2.INTER_AREA)
dst2=cv2.resize(img,(128,128))

cv2.imshow('frame', dst1)
cv2.imshow('frame2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()