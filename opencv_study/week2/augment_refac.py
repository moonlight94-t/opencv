import cv2,os
import numpy as np
# 검은색 물체는 작동하지 않음, 마스킹 논리를 반대로해야함.
# 검은 윤곽이 왜 생기는지: 리사이징 과정에서 보간법 문제, 그림자의 검은 색 두가지 원인으로 판단됨
class augment:
    def masking(self,src): #masking 방법은 자유, 객체를 인식해서 윤곽을 그려주기
        pt=[]
        img = cv2.resize(src,(800,600),interpolation=cv2.INTER_AREA)
        def mouse_callback(event, x, y, flags, param):
            nonlocal img,pt
            if event==cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img,(x,y),1,(0,0,0),-1)
                pt.append([x,y])
            elif event==cv2.EVENT_RBUTTONDOWN:
                pt=np.array(pt)
                cv2.fillPoly(img,[pt],0)
                pt=[]
            cv2.imshow('img',img)
       
        cv2.namedWindow('img')
        cv2.setMouseCallback('img',mouse_callback, [img])

        cv2.imshow('img',img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        return img
    
    def scissor(self,src,src2):
        img = cv2.resize(src,(800,600),cv2.INTER_AREA)
        _,src2_mask= cv2.threshold(src2,20,255,cv2.THRESH_BINARY) # 배경을 어떻게 걸러낼 것인지 threshold
        src2_mask=cv2.bitwise_not(src2_mask)
        dst= cv2.bitwise_and(img,img,mask=src2_mask)
        return dst

    #rotate and scaling # 단 여기서 잘리지 않을만큼의 크기로 사진을 찍어야함
    def rotate(self,dst,angle=0,scale=1.0):
        (h, w) = dst.shape[:2]
        center = (w // 2, h // 2)
        aff=cv2.getRotationMatrix2D(center, angle, scale)
        rotated_image = cv2.warpAffine(dst,aff , (w, h))
        return rotated_image
    
    # 다시 사진에 붙이기, 9개의 위치에 붙임, 저장도 함, 224 이미지로 resize
    def locating_saving(self,button, src , name,clas='class0',ratio=0.05):
        if button:
            back = cv2.imread('0912/white_back.jpg')
        else:
            back = cv2.imread('0912/wood_back.jpg')
        back=cv2.resize(back,(300,400),interpolation=cv2.INTER_AREA)
        sticker=cv2.resize(src,(300,400),interpolation=cv2.INTER_NEAREST)

        # mask 
        wow=np.zeros((800,600,3),np.uint8)
        # 어느정도 위치는 비율보고 결정해야함, 스티커에서 어느정도를 살릴 것인지
        for a,b in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
            ratio=0.05
            back_h_blank= 800-2*int(ratio*800)-400
            back_w_blank= 600-2*int(ratio*600)-300
            h_blank=int(ratio*800+back_h_blank*a/2)
            w_blank=int(ratio*600+back_w_blank*b/2)
            # 1번째위치 남은 위치를 3등분해서 더하면 영역값이 나옴 
            h_blank_after=h_blank+400
            w_blank_after=w_blank+300
            wow2=wow.copy()
            wow2[h_blank:h_blank_after,w_blank:w_blank_after]= sticker
            crop=wow2[200:600,150:450]
            _,crop_mask= cv2.threshold(crop,70,255,cv2.THRESH_BINARY_INV) #threshold 값 조정 필요 
            cv2.copyTo(back,crop_mask,crop)
            if button:
                crop = cv2.resize(crop,(224,224),interpolation=cv2.INTER_NEAREST)#보간법에 따라 마스킹이 잘 안될 수 있음 
                os.makedirs(f'0912/{clas}',exist_ok=True)
                cv2.imwrite(f'0912/{clas}/{name}_{a}{b}_white.jpg',crop)
            else:
                crop = cv2.resize(crop,(224,224),interpolation=cv2.INTER_NEAREST)
                os.makedirs(f'0912/{clas}',exist_ok=True)
                cv2.imwrite(f'0912/{clas}/{name}_{a}{b}_wood.jpg',crop)

    def creating(self,dst,clas,anglelist=[0,40,80],scalelist=[1.0,0.8,1.8],flipflag=True,fliplist=[1,0]):
        for i in anglelist:
            for j in scalelist:
                aug_image=self.rotate(dst,i,j)
                if flipflag:
                    for k in fliplist:
                        aug_image=cv2.flip(aug_image,k)
                        name=f'angle{i}_scale{j}_flip{k}'
                        self.locating_saving(True,aug_image,name,clas)
                        self.locating_saving(False,aug_image,name,clas)
                else:
                    name=f'angle{i}_scale{j}'
                    self.locating_saving(True,aug_image,name,clas)
                    self.locating_saving(False,aug_image,name,clas)
                    
cal=augment() # 객체 생성
src=cv2.imread('0912/class1/origin_5.jpg')
cal.creating(cal.scissor(src,cal.masking(src)),'class1') # masking 해서 물체를 따로 띄어낸 후 옵션에 따라 변화를 주고 배경의 각 9개의 위치에 각각 붙여놓음.

#src2=cv2.imread('origin_5_mask.jpg',cv2.IMREAD_GRAYSCALE)# masking 이미지