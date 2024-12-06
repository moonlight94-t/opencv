import cv2,sys
import numpy as np

img = cv2.imread('open/test/124157654.png')
 
pt=[]
def mouse_callback(event, x, y, flags, param):
    global img,pt
    
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),1,(0,0,0),-1)
        pt.append([x,y])
    elif event==cv2.EVENT_RBUTTONDOWN:
        pt=np.array(pt)
        cv2.fillPoly(img,[pt],0)
        pt=[]
    cv2.imshow('img',img)

#img = np.ones((256,256,3),np.uint8)*255

cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse_callback, [img])

cv2.imshow('img',img)
key=cv2.waitKey()
if key == ord(' '):
    cv2.imwrite('origin_mask2.jpg',img)
cv2.destroyAllWindows()