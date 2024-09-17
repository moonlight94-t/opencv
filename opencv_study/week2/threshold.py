import cv2, sys
import matplotlib.pyplot as plt
import myLib

src=cv2.imread('apple.jpg',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('load fail')

# src histogram 확인
myLib.hist_gray(src)

# threshold함수를 이용해서 흑과 백으로 나눈다.
_,src_th=cv2.threshold(src, 170,255,cv2.THRESH_BINARY) #170이 threshold 기준, 기준 넘은것을 255 나머지는 0
#안을 채우고 싶으면 230으로 올려서 반사된 부분도 사과로 인식되게
cv2.imshow('frame',src_th)
cv2.waitKey()
cv2.destroyAllWindows()