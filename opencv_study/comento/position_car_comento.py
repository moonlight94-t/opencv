import cv2, sys
from glob import glob
import numpy as np

myli=glob('comento/open/train/*.txt')
back=np.ones((1040,1920,3),np.uint8)*255
back2=cv2.imread('comento/syn_06469.png')

for i in myli:
    with open(i,"r") as f:
        lines=f.readlines()
        for j in range(len(lines)):
            x1=lines[j].split('\n')[0].split(' ')[1] #좌측
            #y1=lines[j].split('\n')[0].split(' ')[2]
            x2=lines[j].split('\n')[0].split(' ')[3] #우측
            y2=lines[j].split('\n')[0].split(' ')[4] #상단
            #x3=lines[j].split('\n')[0].split(' ')[5]
            y3=lines[j].split('\n')[0].split(' ')[6] #하단
            #x4=lines[j].split('\n')[0].split(' ')[7]
            #y4=lines[j].split('\n')[0].split(' ')[8]
        
            x_centor=int((int(x2)+int(x1))/2)
            y_centor=int((int(y3)+int(y2))/2)
            
            cv2.circle(back, (x_centor,y_centor), radius=3, color=(0, 0, 255), thickness=-1)
            cv2.circle(back2, (x_centor,y_centor), radius=3, color=(0, 0, 255), thickness=-1)
            

cv2.imwrite('car_position1.jpg',back)
cv2.imwrite('car_position2.jpg',back2)

cv2.imshow('frame',back)
cv2.imshow('frame2',back2)
cv2.waitKey()
cv2.destroyAllWindows()