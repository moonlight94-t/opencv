import cv2
import numpy as np

img = np.full((400,400,3),255, np.uint8) # 400x400x3 공간을 전부 255로 채움 흰색캔버스


text='hello? opencv ' + cv2.__version__
cv2.putText(img, text, (50,350),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),2,cv2.LINE_AA)

pt1=(50,100)
pt2=(img.shape[0]-50, img.shape[1]-100)
cv2.line(img, pt1, pt2, (0,0,255),3,cv2.LINE_4)
# linetype8 은 대각선은 좀 표면이 거칠음 AA가 부드러움
# 꺼끌꺼끌해지면 연산량 적어짐 부드러우면 선을 많이 긋는거라 연산많아짐
# 보통 글씨 쓸때는 AA 많이씀

qt1=(30,70)
qt2=(50,100)
# (x1,y1) (x2,y2)
cv2.rectangle(img, qt1, qt2, (0,0,255), 1, cv2.LINE_4)
# x,y,width,height
cv2.rectangle(img, (30,70,100,100),(255,0,0), 1, cv2.LINE_4)

cv2.circle(img, qt1, 30 ,(0,255,0),2,cv2.LINE_AA) # 좌표값은 int 여야함. 픽셀위치니까

#cv2.polylines

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()