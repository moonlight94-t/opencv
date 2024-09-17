import cv2,sys
import numpy as np

src = cv2.imread('0912/class1/origin_5.jpg') # 4000, 3000
img = cv2.resize(src,(800,600),interpolation=cv2.INTER_AREA) #여기선 width, height
# 224 이미지로 resize

 
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
    cv2.imwrite('origin_5_mask.jpg',img)
cv2.destroyAllWindows()