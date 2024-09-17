import cv2,sys,os
from glob import glob

#인수값 전달은 보통 복사해서 전달해주는 것,copy() 라서 본래 값을 콜백함수 내에서 바꿀수가 없음
#플래그
#최적화
def drawBox(img, corners): 
    cpy = img.copy()
    c1=(192,192,255) 
    cv2.rectangle(cpy,corners[0],corners[1],c1,2) #그릴때 좌표값은 무조건(무조건은 모르겠고 여기서는) 정수여야함
    disp=cv2.addWeighted(img,0.3,cpy,0.7,0)
    return disp

def mouse_callback(event,x,y,flags,param):
    global ptOld,click,corners,paramold,paramnew,oldbox
    
    if event==cv2.EVENT_LBUTTONDOWN:
        ptOld=(x,y)
        click=True
                
    if event==cv2.EVENT_LBUTTONUP:
        click=False
        oldbox.append(corners)
        paramold.append(param[0])
        param[0]=drawBox(param[0],corners) #계속 그려지는 부분
        paramnew=param[0] #이전박스 불러온 다음 그릴용도
           
    if event==cv2.EVENT_MOUSEMOVE:
        if click:
            ptNew=(x,y)
            corners=[ptOld,ptNew]
            cpy=drawBox(param[0],corners)
            cv2.imshow('frame',cpy)
            
    if event==cv2.EVENT_RBUTTONDOWN: # 이거 밖에 키로 넣어도 변수범위가 설정이 가능하려나 global로 빼면 당연히 가능은하겠지
        if paramold:
            param[0]=paramold[-1]
            paramold=paramold[:-1]
            cv2.imshow('frame',param[0])
        # 그 박스안에 좌표가 있을때만 지우기 이거는 박스겹치면?
        # 박스를 여러개 칠때 지울때도 생각해서 어떻게 박스저장할까
        
click=False
pic_list=glob('dat/*.jpg')
order=0
clas='cat'
           
while True:
    i = pic_list[order]
    paramold=[]
    oldbox=[]
    paramnew=None
    img= cv2.imread(i)
    if img is None:
        sys.exit('load fail')
        
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame',mouse_callback,[img])
    cv2.imshow('frame',img)

    while True:
        key=cv2.waitKeyEx()
        if key==13: #enter key
            if oldbox:
                for j in oldbox:
                    name= i.split('\\')[-1].split('.')[0]
                    f=open(f'{name}.txt','w')
                    f.write(f"{clas} {j[0][0]} {j[0][1]} {j[1][0]} {j[1][1]}\n")
                    f.close()
        elif key==ord(' '): # 클래스 지정 버튼 처럼 바뀌게 
            if clas=='cat':
                clas='person'
            else:
                clas='cat'
        elif key==0x270000:  # 화살표 ->를 누르면 다음이미지
            if order+1 < len(pic_list):
                order+=1
                cv2.destroyAllWindows()
                break    
        elif key==0x250000: #화살표<-텍스트가 있으면 박스를 이미지위에 띄워줌
            name= i.split('\\')[-1].split('.')[0]+'.txt'
            if os.path.exists(name):
                f=open(name,'r')
                reader=f.readlines()
                if paramnew is not None:
                    img=paramnew
                for k in reader:
                    oldone=(int(k.split('\n')[0].split(' ')[1]),int(k.split('\n')[0].split(' ')[2]))
                    newone=(int(k.split('\n')[0].split(' ')[3]),int(k.split('\n')[0].split(' ')[4]))
                    disp=drawBox(img,[oldone,newone])
                    img=disp # 읽어온다음 지우는건 또 별개문제이고 img 전역변수를 업데이트해도되는지    
                cv2.imshow('frame',disp)
                cv2.setMouseCallback('frame',mouse_callback,[img]) #img 다시 인수로 넣어주기 
                #이래야 이전박스 불러온 다음 거기에 박스 또 그릴 수 있음 
        elif key==27:
            cv2.destroyAllWindows()
            sys.exit()   
    if order+1 <len(pic_list):
        order+=1
    else:
        break

