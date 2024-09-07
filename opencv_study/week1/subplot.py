# 이미지를 4장 불러온다

import cv2, sys
from matplotlib import pyplot as plt

img1 = cv2.imread('data/lena.jpg')
img2 = cv2.imread('data/orange.jpg')
img3 = cv2.imread('data/apple.jpg')
img4 = cv2.imread('data/baboon.jpg')

if img1 is None or img2 is None or img3 is None or img4 is None:
    sys.exit("load fail")
    
    
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)

#subplot

fig, ax= plt.subplots(2,2,figsize=(10,10))
#aspect 정사각형 비율 유지여부 
ax[0][0].imshow(img1,aspect='auto') # 비율 바꿀수있음
ax[0][0].axis('off')
ax[0][1].imshow(img2,aspect='auto')
ax[0][1].axis('off')
ax[1][0].imshow(img3,aspect='auto')
ax[1][0].axis('off')
ax[1][1].imshow(img4,aspect='auto')
ax[1][1].axis('off')
ax[1][1].set_title('orange')

fig.canvas.manager.set_window_title('Trial 4')
fig.suptilte('trial 3')

plt.show()