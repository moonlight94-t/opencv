import cv2,sys
import numpy as np
import math

#데이터 증강에 사용
src=cv2.imread('../data2/rose.bmp')
def translate(src,x=0,y=0):
    

    if src is None:
        sys.exit('load fail')
    
    # 이미지의 이동변환
    aff = np.array([[1,0,x],[0,1,y]],dtype=np.float32)

    dst = cv2.warpAffine(src,aff,(0,0)) #(0,0)변환후에 출력되는 output크기 dsize, 
    #(0,0)input이미지 크기 그대로 출력 아닌거같은데 scaling값은 알아서 계산해줌 docu 출처
    return dst
    
#dst=translate(src,50,50)

def shear(src,x=0,y=0,):
    h,w = src.shape[:2]
    if x>0 and y==0:
        aff = np.array([[1,x,0],[0,1,0]],dtype=np.float32)
        dst= cv2.warpAffine(src,aff,(w+int(h*x),h))
    if x==0 and y>0:
        aff = np.array([[1,0,0],[y,1,0]],dtype=np.float32)
        dst= cv2.warpAffine(src,aff,(w,h+int(w*y)))
    
    return dst

def scaling(src,x=1,y=1):
    h, w = src.shape[:2]
    aff= np.array([[x,0,0],[0,y,0]],dtype=np.float32)
    dst=cv2.warpAffine(src,aff,(w*x,h*y))
    return dst

def rotate(src,theta): #중심축은 기본적으로 좌측상단, (0,0)
    theta_rad = np.deg2rad(theta) #라디안 값으로 바꿔줘야함
    theta_rad = theta*math.pi/180
    aff=np.array([[np.cos(theta_rad),np.sin(theta_rad),0],[-np.sin(theta_rad),np.cos(theta_rad),0]])
    dst=cv2.warpAffine(src,aff,(0,0))
    return dst

def rotate2(src,theta):
    h,w=src.shape[:2]
    
    center=w/2,h/2
    
    rot =cv2.getRotationMatrix2D(center,angle=theta,scale=1)
    dst =cv2.warpAffine(src,rot,(0,0))
    return dst
    

#dst=scaling(src,2,1)
dst=cv2.resize(src,(1024,1024),interpolation=cv2.INTER_CUBIC)# 해상도 설정 inter_nearest보다 엣지가 깍두기 없이 부드럽고 2등
dst=cv2.resize(src,(0,0),fx=1.5,fy=1.5)# 비율 설정 
dst1=cv2.resize(src,(1024,1024),interpolation=cv2.INTER_NEAREST) #3등
dst2=cv2.resize(src,(1024,1024),interpolation=cv2.INTER_LANCZOS4) #3개중에 가장 오래걸림 1등
# dst=rotate(src,10)
# dst=rotate2(src,10) 

cv2.imshow('cubic',dst)
cv2.imshow('nearest',dst1)
cv2.imshow('lanczos4',dst2)
cv2.waitKey()
cv2.destroyAllWindows()