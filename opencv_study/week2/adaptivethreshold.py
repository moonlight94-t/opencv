import cv2, sys
import matplotlib.pyplot as plt
import myLib

src=cv2.imread('../data/srcThreshold.png',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('load fail')

# src histogram 확인
myLib.hist_gray(src)

# threshold함수를 이용해서 흑과 백으로 나눈다.
src_th=cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,51,7)
#maxvalue, blocksize:주변의 51개의 블록을 본다는것(51x51)-해상도에 따라 선택
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C
#논문을 보고 상황에 따라 threshold함수를 정확하게  


cv2.imshow('frame',src_th)
cv2.waitKey()
cv2.destroyAllWindows()