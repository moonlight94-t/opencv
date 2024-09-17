import cv2, sys
import numpy as np

# 좌표를 얻기위한 콜백함수
radius=25
def drawROI(img, corners,radius): #직선과 원을 그리는 함수
    # 이미지 복사해서 레이어를 하나 추가(가이드 라인과 모서리포인트를 추가로 그려주는)
    cpy = img.copy()
    
    #컬러지정
    c1=(192,192,255) # 원의 색상
    c2=(128,128,255) # 직선의 색상, 이 색이 좀더 진함
    
    line_thick=2
    
    #원을 그린다.
    for pt in corners:
        cv2.circle(cpy,tuple(pt.astype(int)),radius,c1,-1,cv2.LINE_AA) #그릴때 좌표값은 무조건(무조건은 모르겠고 여기서는) 정수여야함
    # opencv 함수마다 좌표를 정수 또는 소수로 원하는 경우가 다름 
    #4개 모서리 라인
    cv2.line(cpy,tuple(corners[0].astype(int)),tuple(corners[1].astype(int)),c2,line_thick,cv2.LINE_AA)
    cv2.line(cpy,tuple(corners[1].astype(int)),tuple(corners[2].astype(int)),c2,line_thick,cv2.LINE_AA)
    cv2.line(cpy,tuple(corners[2].astype(int)),tuple(corners[3].astype(int)),c2,line_thick,cv2.LINE_AA)
    cv2.line(cpy,tuple(corners[3].astype(int)),tuple(corners[0].astype(int)),c2,line_thick,cv2.LINE_AA)
    
    disp=cv2.addWeighted(img,0.3,cpy,0.7,0)
    
    return disp
    
# 버튼 업 다운 이동 끌어서 이동하는 구현 논리    
def mouse_callback(event,x,y,flags,param):
    global startQuad,dragSrc,radius,ptOld
    #ptOld 전역변수 이유 local ptold는 호출된 후 함수 나가면 저장안되고 사라짐
    
    if event==cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv2.norm(startQuad[i]-(x,y))<radius:
                dragSrc[i]=True
                ptOld=(x,y) #이동 이전의 위치 
                break
            
    if event==cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i]=False # dragsrc는 4 모서리 중에 어떤 모서리를 끌고 있는지 판단하기 위함
            #현재 이동중인 모서리 포인트를 true
    
    #이동중에 모서리 원과 직선을 새로 그려서 업데이트        
    if event==cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                dx = x-ptOld[0]
                dy = y-ptOld[1]
                
                startQuad[i]+=(dx,dy) #numpy는 array랑 tuple이랑 합쳐주네 
                #창에 업데이트
                cpy=drawROI(param[0],startQuad,radius)
                cv2.imshow('frame',cpy)
                ptOld=(x,y)
                break

img=cv2.imread('week2/book.jpg')

if img is None:
    sys.exit('load fail')
    
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse_callback,[img]) #[img, param2, param3] 여러개주고 param[0]지정해서 불러오기 가능
#cv2.imshow('frame',img)
#cv2.waitKey()
#cv2.destroyAllWindows()

h,w = img.shape[:2] #541 512

# 다각형의 좌표를 시계방향으로 그림
srcQuad=np.array([[220, 128], [469, 147], [378, 481], [47, 391]], np.float32)
dstQuad=np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]],np.float32) # image indexing 0부터 시작하니 w-1 
spare=30
startQuad=np.array([[spare,spare],[w-spare,spare],[w-spare,h-spare],[spare,h-spare]],np.float32)

# 4개의 점 중 무슨 점이 이동하는지 식별하기 위한 플래그
dragSrc = [False,False,False,False]

# 처음 한번은 drawROI 함수를 호출해서 그려준다. 굳이 필요한가?! 안하면 처음에 이동시킬 반원이 안나옴 
disp=drawROI(img,startQuad,radius)

# pers =cv2.getPerspectiveTransform(srcQuad,dstQuad) #변환 행렬을 만들어줌 
# dst = cv2.warpPerspective(img,pers,(w,h)) #여긴 또 width height네 

cv2.imshow('frame',disp) 

while True:
    key=cv2.waitKey()
    if key==13: #enter key
        pers =cv2.getPerspectiveTransform(startQuad,dstQuad) #변환 행렬을 만들어줌 
        dst = cv2.warpPerspective(img,pers,(w,h))
        cv2.imshow('frame2',dst)
        cv2.waitKey()
        cv2.destroyAllWindows()
        break
    elif key==27:
        cv2.destroyAllWindows()
        sys.exit()