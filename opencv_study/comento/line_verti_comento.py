import cv2
from glob import glob
import numpy as np
12
43
a=0
b=0
c=0
d=0
# def find_region(x, y):
#     global a,b,c,d
    
#     y_line1 = 2.557093 * x -1153.920415
#     y_line2 = 1.834570 * x - 1436.452991
   
#     if y < y_line1 and y < y_line2:
#         a+=1
#     elif y > y_line1 and y > y_line2:
#         b+=1
#     elif y==y_line1 or y==y_line2:
#         c+=1
#     else:
#         d+=1 #error 역할 
#     return [a,b,c,d]

def y_line1(x):
    return 2.865591 * int(x) -1388.118279
def y_line2(x):
    return 2.299007 * int(x) -1920.242990

def vertification(x,y):
    a,b,c,d=0,0,0,0
    if y> y_line1(x):
        a+=1
    elif y> y_line2(x) and y< y_line1(x):
        b+=1
    elif y< y_line2(x):
        c+=1
    else:
        d+=1
    return (a,b,c,d)

    
myli= glob('comento/open/train/*.txt')
before=0
resultlist=[]
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
        
        
            x_centor=(int(x2)+int(x1))/2
            y_centor=(int(y3)+int(y2))/2
#1920 1040            

            # if int(y3)> y_line1(x3) and int(y4)> y_line1(x4):
            #     a+=1
            # elif int(y3)> y_line2(x3) and int(y4)> y_line2(x4) and int(y3)< y_line1(x3) and int(y4)< y_line1(x4):
            #     b+=1
            # elif int(y3)< y_line2(x3) and int(y4)< y_line2(x4):
            #     c+=1
            # else:
            #     d+=1
            
            anew,bnew,cnew,dnew=vertification(x_centor,y_centor)
            a+=anew
            b+=bnew
            c+=cnew
            d+=dnew
            result=[a,b,c,d]
            
            if result[3]>before:
                resultlist.append(i)
                before=result[3]
            

print(resultlist)
print(result)
#6003개나 제대로 검출못함 쓰레기임 
#[5747, 5709, 5544, 0] error는 없음 