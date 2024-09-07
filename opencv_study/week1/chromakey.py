# 크로마키 두 영상의 길이가 다를 때 어떻게 할것인가
import cv2, sys
import numpy as np

cap1 = cv2.VideoCapture('data2/woman.mp4')
cap2 = cv2.VideoCapture('data2/raining.mp4')

if not cap1.isOpened():
    sys.exit('video1 open failed')
if not cap2.isOpened():
    sys.exit('video2 open failed')
    
# 동영상의 FPS 읽어오기
fps1 = int(cap1.get(cv2.CAP_PROP_FPS)) #23
fps2 = int(cap2.get(cv2.CAP_PROP_FPS)) #25 왜 int로 감싸주지? 인수로 int를 넣어야하는 필요성이 있는건지 실제로 24.999 이렇게 나오는지? 처음 썼을때 논리 확인

fpscount1 = cap1.get(cv2.CAP_PROP_FRAME_COUNT) #409
fpscount2 = cap2.get(cv2.CAP_PROP_FRAME_COUNT) #353

# 초당 몇 프레임인지
delay = int(1000/fps1)

# 합성 여부 설정 플래그
do_composite = False # 이런 프로그램 제어하는 논리

hmin=40
hmax=60
vmin=0
vmax=255

def on_trackbar(pos):
    global hmin, hmax#, vmin, vmax
    hmin = cv2.getTrackbarPos('H_min','Trackbar')
    hmax = cv2.getTrackbarPos('H_max','Trackbar')
    vmin = cv2.getTrackbarPos('V_min','Trackbar') 
    vmax = cv2.getTrackbarPos('V_max','Trackbar')
    
    # inrange함수에 넣어줌
    #dst = cv2.inRange(hsv, (hmin,150,vmin),(hmax,255,vmax))
    #cv2.copyTo(frame2, dst, frame1)
    #cv2.imshow('Trackbar', frame1) # 여기서 imshow 해버리면 딱 hsv 읽어왔던 한프레임만 가지고함, 계속 read()하는 것은 while에서 작동하기 때문
  
cv2.namedWindow('Trackbar')  
cv2.createTrackbar('H_min','Trackbar',40,60,on_trackbar)
cv2.createTrackbar('H_max','Trackbar',60,80,on_trackbar) # assertion error
cv2.createTrackbar('V_min','Trackbar',0,255,on_trackbar)
cv2.createTrackbar('V_max','Trackbar',255,255,on_trackbar)
cv2.setTrackbarPos('H_min','Trackbar',40) #초기값 설정, 사실 creat바에 있어서 의미없음


while True:
    ret1, frame1 = cap1.read() # read함수 작동원리: while 돌리는 이유, 첫 프레임 부터 호출할 때마다 한 프레임 씩 읽어옴 
    if not ret1:
        break
    
    if do_composite :
        ret2, frame2 = cap2.read()
        if not ret2:
            break
    

        # hsv 색공간에서 영역을 검출해서 합성 rgb로는 어디까지가 녹색인지 명확히 하기힘듬
        hsv= cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(hmin,150,vmin),(hmax,255,vmax)) # 범위 답을 이미 찾은 것 실제로는 찾아야함 / 50 70 , 150 255, 0 255 / inrange 범위 안에 있는지
        cv2.copyTo(frame2, mask, frame1) # frame2 frame1 자리 논리: 결국 논리가 비그림에서 녹색부분만 잘라서 가져오는 논리인데 
        

    # 결과 확인
    cv2.imshow('Trackbar', frame1) # 여기서 업데이트 하는걸 어떻게 처리할 것인지
    #on_trackbar(0) 필요성? 이걸 초기화라고 부를 이유가 있나?
    key=cv2.waitKey(delay) # delay도 필요하구나 정리가 너무 안되어있음

    if key==ord(' '):
        do_composite = not do_composite
    elif key==27: #esc는 문자열로 표현이 안되어서 ord에 못넣음
        break
    

cap1.release()
cap2.release()
cv2.destroyAllWindows()