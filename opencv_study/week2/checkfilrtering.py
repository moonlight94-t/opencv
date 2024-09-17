import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

#이미지 불러오기

src=cv2.imread('../misson/misson_image01.png')

if src is None:
    sys.exit('load failed')

#컬러 채널 분리
# colors = ['b','g','r']
# bgr_planes = cv2.split(src)

# for (p, c) in zip(bgr_planes, colors):
#     hist = cv2.calcHist([p],[0],None,[256],[0,256])
#     print(hist.shape)
#     plt.plot(hist, color=c)    
# plt.show()

#그냥 rgb를 add하면 색이 틀어짐, 그레이스케일은 밝기채널만 보기때문에 더하고 뺴고 용이

#YCbCr(YCC) luminance
src_YCC = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
hist1 = cv2.calcHist([src_YCC],[0],None,[256],[0,256])
plt.plot(hist1)
#plt.show()

Y,cb,cr = cv2.split(src_YCC)
#normalize 적용 minmax값이 이미 적지만 있기 때문에 크게 변하지않음 
src_norm = cv2.normalize(Y,None,0,255,cv2.NORM_MINMAX)

hist2 = cv2.calcHist([src_norm],[0],None,[256],[0,256])
plt.plot(hist2)
#plt.show()

#equalize 적용
src_equal=cv2.equalizeHist(Y)
hist3 = cv2.calcHist([src_equal],[0],None,[256],[0,256])
plt.plot(hist3)
plt.show()

# 합치기
src_YCC=cv2.merge((src_equal,cb,cr)) # tuple

# 다시변환
src_YCC_add=cv2.add(Y,50)
src_YCC_add=cv2.merge((src_YCC_add,cb,cr))
src_add = cv2.cvtColor(src_YCC_add,cv2.COLOR_YCrCb2BGR)

cv2.imshow('frame',src_add)
cv2.waitKey()
cv2.destroyAllWindows()