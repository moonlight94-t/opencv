import os
import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import cv2
import numpy as np

# 비디오 열기
mp4Path = 'C:/Users/User.DESKTOP-5C3VHRV/opencv/opencv_study/comento/test_cctv.mp4'
cap=cv2.VideoCapture(mp4Path)
fps = cap.get(cv2.CAP_PROP_FPS)              # 초당 프레임 수
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 총 프레임 수
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)    # 비디오의 너비
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 비디오의 높이
model = torch.hub.load('C:/Users/User.DESKTOP-5C3VHRV/opencv/opencv_study/comento/yolov5', 'custom', path='C:/Users/User.DESKTOP-5C3VHRV/opencv/opencv_study/comento/best.pt', source='local')
model.conf=0.82
framelist=[]
resultlist=[]

while(True):
    retval, frame = cap.read()
    cv2.imshow('frame',frame)
    result = model(frame,size=1920)
    framelist.append(frame)
    resultlist.append(result)
    key = cv2.waitKey(int(1000/30))
    if key==27:
        break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()

print(result[0].pandas().xyxy[0])

#result[1].pandas().xyxy[0]


# 프레임 마다 객체인식

# 이전 정보 바탕으로 객체 추적 및 속도 계산

# 교통량 및 속도 저장 한 것을 그래프 그리기