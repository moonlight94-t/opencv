import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

src1 = cv2.imread('data2/Hawkes_norm.jpg',cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('data2/Hawkes.jpg',cv2.IMREAD_GRAYSCALE)

if src1 is None : 
    sys.exit('image load failed')
    
hist = cv2.calcHist([src1],[0],None,[256],[0,256]) # 이미지, 0번채널(grayscale), 마스크여부 ,hitsize 몇개로 나누는지 , range
hist2 = cv2.calcHist([src2],[0],None,[256],[0,256])
print(type(hist)) #np.ndarray

cv2.imshow('src1',src1)
cv2.imshow('src2',src2)
plt.plot(hist)
plt.plot(hist2)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()

