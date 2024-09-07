# 동영상을 불러올 때 videoCapture()

import cv2, sys

fileName='data/vtest.avi'

# 동영상의 해상도 width height, frame수(fps) 확인
# videocapture 클래스 객체 생성 + 생성자 호출(파일열기가 일어남)
cap= cv2.VideoCapture(fileName)

framesize=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) , int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
a3=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 전체 몇 프레임
a4=int(cap.get(cv2.CAP_PROP_FPS))

# 동영상의 이미지를 다 가져올 때 까지 반복
while(True):
    # 동영상에서 한장의 image를 가져옴
    # retval : 동영상에서 이미지 가져올때 정상동작했나? True False 
    # frame : 이미지 한장
    retval, frame = cap.read() # 인코딩 된 동영상을 읽으면 raw image로 읽음 / 동영상 코덱 디코딩도 포함 코덱 문제 발생시 pc에 코덱 설치
    
    if not retval :
        break  
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(100) # 10fps니까 100ms 대기
    if key==27: # ascii에서 esc가 27임
        break
    
# 동영상을 열었으면 닫아야 한다
if cap.isOpened():
    cap.release() # 열림 해제
    
cv2.destroyAllWindows()
        

