import cv2
import numpy as np
import matplotlib.pyplot as plt

isColor = True

if not isColor:
    #grayscale
    src = cv2.imread('data2/candies.png',cv2.IMREAD_GRAYSCALE)
    #밝기변화 
    dst=cv2.add(src,50)
    hist1=cv2.calcHist([src],[0],None,[256],[0,256])
    hist2=cv2.calcHist([dst],[0],None,[256],[0,256])
    dst1=src+100 #overflow , broadcasting
    #dst1 = np.clip(src+100,0,255).astype(np.uint8) # 범위를 0에서 255 지정하고 덧셈연산 수행 최대치 한정 / ?
    plt.plot(hist1)
    plt.plot(hist2)
    plt.show()


if isColor:
    src=cv2.imread('data/lena.bmp')
    dst=cv2.add(src,(0,0,-50)) # bgr 100 씩 더함 tuple
    dst1=src+100
    
    # color channel 분리
    colors=['b','g','r']
    bgr_planes=cv2.split(src) # tuple형태로 나옴, numpy array배열이 하나씩 나누어져서 나옴
    
    for (p,c) in zip(bgr_planes,colors):
        hist=cv2.calcHist([p],[0],None,[256],[0,256])
        plt.plot(hist,color=c)#color 그래프 그릴때 색상 지정
    
    
#cv2.imshow('frame',src)
cv2.imshow('frame2',dst)
#cv2.imshow('fream3',dst2)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()