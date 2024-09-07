import cv2, sys
import matplotlib.pyplot as plt
import numpy as np

#목적 노이즈 저조도 ?
# 노이즈 -> 샤프닝 -> 밝기조절
#450 x 1040
# def on_trackbar(pos):
#     a = cv2.getTrackbarPos('sigmacolor','bilateral') #마우스 입력을 받아서 트랙바의 위치값을 읽어옴
#     b = cv2.getTrackbarPos('sigmaspace','bilateral')
    

#     dst4 = cv2.bilateralFilter(src, -1, a, b)
#     cv2.imshow('bilateral',dst4)
    
# def on_trackbar2(pos):
#     aa= cv2.getTrackbarPos('v','fast')
#     bb= cv2.getTrackbarPos('s','fast')

#     dst5 = cv2.fastNlMeansDenoisingColored(src, None, aa, bb,7, 21)
#     cv2.imshow('fast',dst5)

# def on_trackbar3(pos):
#     aaa= cv2.getTrackbarPos('add','result')

#     result=cv2.add(sharpening_img,(aaa,aaa,aaa))
#     cv2.imshow('result',result)
    
src = cv2.imread('misson/01.png')
# bgr=cv2.split(src)
# #cv2.imshow('red',bgr[2])
# #cv2.imshow('blue',bgr[0])
# #cv2.imshow('green',bgr[1])
# r = cv2.GaussianBlur(bgr[2], (5, 5), 0)
# filtered_img = cv2.merge([bgr[0], bgr[1], bgr[2]])
# cv2.imshow('how',filtered_img)


# dst2 = cv2.GaussianBlur(src,(0,0),5)
# dst3=cv2.medianBlur(src,3)
# dst4 = cv2.equalizeHist(src)
dst4 = cv2.bilateralFilter(src, -1, 24, 36) # 2개 값 셋팅 24 42

#dst5 = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21) # 4개 값 셋팅

#dst = cv2.normalize(dst4,None,0,255,cv2.NORM_MINMAX) 

mask = np.asarray([[0,-0.5,0],[-0.5,3,-0.5],[0,-0.5,0]], dtype = np.float32)
sharpening_img = cv2.filter2D(dst4,-1, mask)
cv2.imshow('sharpening_img', sharpening_img)

# cv2.namedWindow('bilateral')
# cv2.namedWindow('fast')
# cv2.namedWindow('result')
# cv2.createTrackbar('sigmacolor','bilateral',10,150,on_trackbar)
# cv2.createTrackbar('sigmaspace','bilateral',5,75,on_trackbar)

# cv2.createTrackbar('v','fast',10,50,on_trackbar2)
# cv2.createTrackbar('s','fast',10,50,on_trackbar2)

# cv2.createTrackbar('add','result',0,255,on_trackbar3)

result=cv2.add(sharpening_img,(3,3,3))
cv2.imshow('result',result)
cv2.imwrite('result.jpg',result)


#cv2.imshow('bilateralnormal',dst)
# cv2.imshow('gaussian',dst2)
# cv2.imshow('median',dst3)
cv2.imshow('bilateral',dst4)
# cv2.imshow('fast',dst5)
cv2.waitKey()
cv2.destroyAllWindows()

