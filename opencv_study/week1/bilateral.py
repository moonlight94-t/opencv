# cartoon filter

import cv2,sys

src= cv2.imread('data/lena.bmp')

dst = cv2.bilateralFilter(src,-1,10,5) # 주변의 픽셀을 사용해서 연산을 부드럽게 해줌, 엣지(선)는 살리고 안 면부분 피부같은 것이 부드러워짐


cv2.imshow('frame',src)
cv2.imshow('frame2',dst)

cv2.waitKey()
cv2.destroyAllWindows()