import cv2

src1=cv2.imread('data2/airplane.bmp')
src2=cv2.imread('data2/field.bmp')

dst = cv2.addWeighted(src1=src1,alpha=0.9, src2=src2 ,beta=0.1,gamma=0) # 두 파일 크기가 같아야하나?

cv2.imshow('frame',dst)
cv2.waitKey()
cv2.destroyAllWindows()
