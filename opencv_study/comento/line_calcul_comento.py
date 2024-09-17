import cv2
from glob import glob
import numpy as np

myli=glob('redblue/*.jpg')
con1=np.ones((1040,1920),np.uint8)*0
con2=np.ones((1040,1920),np.uint8)*0
for i in myli:
    img=cv2.imread(i)
    red = cv2.inRange(img, (0,0,235),(15,15,255))
    blue = cv2.inRange(img, (205,0,0),(255,15,15))
    con1 = cv2.bitwise_or(con1,red)
    con2 = cv2.bitwise_or(con2,blue)

p1=[]
p2=[]
def mouse_callback(event, x, y, flags, param): #내부함수 캡슐화 
    global p1
    if event==cv2.EVENT_LBUTTONDOWN:
        p1.append((x,y))
    if event==cv2.EVENT_RBUTTONDOWN:
        m = (p1[0][1]-p1[1][1])/(p1[0][0]-p1[1][0])
        b = p1[0][1]- m*p1[0][0]
        p1 =[]
        print(m,b)
    cv2.imshow('frame1',param[0])
    
def mouse_callback2(event, x, y, flags, param):
    global p2
    if event==cv2.EVENT_LBUTTONDOWN:
        p2.append((x,y))
    if event==cv2.EVENT_RBUTTONDOWN:
        m = (p2[0][1]-p2[1][1])/(p2[0][0]-p2[1][0])
        b = p2[0][1]- m*p2[0][0]
        p2=[]
        print(m,b)
    
    cv2.imshow('frame2',param[0])
    
#con1=cv2.imread('car_position2.jpg')   
cv2.namedWindow('frame1')
cv2.namedWindow('frame2')
cv2.setMouseCallback('frame1',mouse_callback, [con1])
cv2.setMouseCallback('frame2',mouse_callback2,[con2])

cv2.waitKey()
cv2.destroyAllWindows()

#2.557093425605536 -1153.9204152249135
#1.8354700854700854 -1436.4529914529915

# 좌표가 주어졌을 때 어느 구간에 속하는지 판별하기 위한 함수
def find_region(x, y):
    
    y_line1 = 2.557093 * x -1153.920415
    y_line2 = 1.834570 * x - 1436.452991
    
    if y < y_line1 and y < y_line2:
        return "첫 번째 구간"
    elif y > y_line1 and y > y_line2:
        return "세 번째 구간"
    elif y==y_line1 or y==y_line2:
        return "line error"
    else:
        return "두 번째 구간"
    
print(find_region(50,20))