import cv2

src = cv2.imread('ugly_lena.jpg')

dst=cv2.medianBlur(src,3)

cv2.imshow('frame',dst) #image는 주변 픽셀간의 큰 차이가 나는 경우가 거의 없다 서서히 변하는게 보통 이런 논리 
cv2.waitKey()
cv2.destroyAllWindows()
