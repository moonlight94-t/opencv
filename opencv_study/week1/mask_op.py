import cv2, sys

img1= cv2.imread('data2\HappyFish.jpg')

img2=img1 # 얕은 복사
img3=img1.copy() # 깊은 복사

img1.fill(255)

img4=img3[40:120, 30:150].copy()
#numpy.ndarray의 슬라이싱 [행,열] 단 image에서는 행이 y축 열이 x축을 의미

#mask연산
src= cv2.imread('data2/airplane.bmp')
mask= cv2.imread('data2/mask_plane.bmp',cv2.IMREAD_GRAYSCALE) 
# 원본이미지가 그레이면 굳이 변환필요없는데 원본 칼라이고 마스크는 그레이여야함
dst= cv2.imread('data2/field.bmp')


cv2.copyTo(src,mask,dst)
#dst 출력영상 src와 크기 및 타입이 같은 dst를 넣어주면 새로 생성하지 않고 연산 수행
#그렇지 않으면 dst새로 생성해서 return

#mask 깔끔하게 만드는게 어려움
# alpha채널이 마스크가 됨

img=cv2.imread('data2/opencv-logo-white.png',cv2.IMREAD_UNCHANGED)
# alpha채널도 읽어오려면 unchanged
dst2=cv2.imread('data2/cat.bmp')

src2=img[:,:,:3].copy()
mask2=img[:,:,3].copy()
#mask의 영역
h,w=mask2.shape[:2]
crop= dst2[10:10+h, 10:10+w] # image size 보고 이미지 넣을 위치
# 얕은 복사라서 crop을 바꾸면 dst가 바뀜!!

dst3=cv2.copyTo(src2,mask2,crop) # mask연산은 mask크기만큼만
#src,mask,crop은 다 같은 크기여야함
#crop은 dst2배열을 부르는 또 다른이름


cv2.imshow('img',dst2)
cv2.waitKey()
cv2.destroyAllWindows()
