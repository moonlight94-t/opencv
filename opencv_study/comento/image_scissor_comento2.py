import cv2

img = cv2.imread('open/test/124157654.png')
src = cv2.imread('origin_mask2.jpg')
_,src2_mask= cv2.threshold(src,20,255,cv2.THRESH_BINARY) # 배경을 어떻게 걸러낼 것인지 threshold
src2_mask=cv2.bitwise_not(src2_mask)
src2_mask=cv2.cvtColor(src2_mask,cv2.COLOR_BGR2GRAY)
dst= cv2.bitwise_and(img,img,mask=src2_mask)


cv2.imshow('img',dst)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('cropped_scissor2.png',dst)