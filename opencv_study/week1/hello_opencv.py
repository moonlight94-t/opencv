import sys
import cv2

#opencv 버전확인
print('Hello OpenCV', cv2.__version__)
#image read 읽어오면 numpy.ndarray
img_gray = cv2.imread('data/lena.bmp', cv2.IMREAD_GRAYSCALE)
img_bgr = cv2.imread('data/lena.bmp') # 왜 bgr인지

if img_gray is None or img_bgr is None:
    print('Image load failed!')
    sys.exit()

# 창의 이름 설정
cv2.namedWindow('image_gray')
cv2.namedWindow('image_bgr')
# 불러온 img 이미지 배열를 'image'창에 띄워줌
cv2.imshow('image_gray', img_gray)
cv2.imshow('image_bgr', img_bgr)
# 키 입력을 기다리는 함수
# 안에 delay 값 인수 단위 : ms / default = inf
cv2.waitKey()
# 모든 창을 다 닫는다.
cv2.destroyAllWindows()