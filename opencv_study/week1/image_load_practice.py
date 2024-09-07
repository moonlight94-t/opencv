# 파일 읽어오기

import cv2
import sys
import os

fileName="cat.jpg"

imgpath=os.path.join("data/",fileName)

img=cv2.imread(imgpath)

print(img.shape) # image height width channel, numpy array
#예외처리 루틴

if img is None:
    print("Image load fail")
    sys.exit()
    
# 이미지배열을 파일로 저장하는 함수
cv2.imwrite('cat1.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,85]) # jpg 정보 유지율 
#cv2.imwrite('cat2.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,30]) # 화질을 높게 손실율을 적게 설정
#창에 출력
cv2.namedWindow('img',cv2.WINDOW_FREERATIO) # WINDOW_FULLSCREEN
cv2.imshow('img',img)


#'q'키를 눌렀을 때 창이 종료되게
loop=True
while (loop):
    inKey=cv2.waitKey() #ascii code return 키보드에 누른 것 , 기본적으로 키 입력 한 번 받는거라 while로 돌려주어야함
    if inKey==ord('q'):
        #cv2.destroyAllWindows()
        cv2.destroyWindow('img')
        loop=False

print(inKey)