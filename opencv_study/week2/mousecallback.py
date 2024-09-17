import cv2,sys
import numpy as np

# 마우스 콜백함수 구현
# 마우스에서 이벤트가 발생하면 호출되는 함수 : 버튼클릭, 마우스이동 등 

#flags : 마우스 버튼과 함께 눌리는 ctrl, shfit,alt 키 눌러졌는지 확인 
pt1=(0,0)
pt2=(0,0)
def mouse_callback(event, x, y, flags, param):
    #global img # 함수 안에서도 img수정가능하게 
    img=param[0] #parameter 인수로 받아서 전역변수설정안하고 img값 얻어옴
    global pt1,pt2 # 함수안에 정의하면 함수는 pt1을 기억못함 
    
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),3)
        print('1')
        pt1=(x,y)
    elif event==cv2.EVENT_LBUTTONUP:
        pt2=(x,y)
        #cv2.rectangle(img,pt1,pt2,(255,0,0),3)
    elif event==cv2.EVENT_MOUSEMOVE: #누른채로 움직여도 좌표출력함 elif에 비해 if가 우선순위를 가지는 것이 아닌가?
        print(x,y)#그런 논리가 아니라 누른건 한번이고 움직이면 새로운 이벤트라서 콜백함수가 새로 호출되고 1은 나오지않고 좌표만 찍힘
        
        
    cv2.imshow('img',img) # 그림화면을 업데이트
        
# 흰색 캔버스 생성
#img = np.zeros((512,512,3),np.uint8)+255
img = np.ones((512,512,3),np.uint8)*255


# main에서 setMouseCallback 함수를 실행하면서 콜백함수를 지정
cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse_callback, [img])# [img]가 parameter

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()