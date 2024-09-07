import cv2,sys
import numpy as np

src = cv2.imread('road.png',cv2.IMREAD_GRAYSCALE)

if src is None :
    sys.exit('failed')
    
dst = cv2.Canny(src,64,128) # threshold 2개를 주어야함

cv2.imshow('frame',src)
cv2.imshow('frame2',dst)

cv2.waitKey()
cv2.destroyAllWindows() # 검출하고싶은부분만 마스킹해서 딴 다음에 차선 주변의 노이즈만 처리