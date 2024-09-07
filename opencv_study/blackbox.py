import cv2, sys, shutil, os
from datetime import datetime as dt
import time, threading

#60초에 비디오 한개 생성, 60초를 어떻게 인식시킬까? / fps10
# 연산에 소모되는 시간차이는 어떻게 해결할까? 쓰레드 멀티프로세싱
# imread는 놓치는 프레임이 있다.
def videorecord(folderpath):
    global cap, endpoint 
    #endpoint=0
    
    def timer_thread(stop_event): # 소프트웨어 함수이기때문에 몇백ms의 오차, 정확하게 c언어코딩하면 1~2ms에서 제어가능 # c언어 하드웨어 제어 좋음 python 소프트웨어 생산성
        global endpoint
        for _ in range(60):
            if endpoint==0:
                break
            time.sleep(1)
        stop_event.set()  # 이벤트 설정 (녹화 중지)   
    stop_recording = threading.Event()
    timer = threading.Thread(target=timer_thread, args=(stop_recording,))
    timer.start()
    #filenumber=dt.now()
    
    fileName=dt.now().strftime("%Y%m%d-%H%M%S")+".mp4"
    framesize=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # codec
    recordpath=os.path.join(folderpath,fileName)
    out = cv2.VideoWriter(recordpath, fourcc, fps, framesize)
    while (True):
        retval, frame = cap.read()
    
        if not retval:
            out.release()
            cv2.destroyAllWindows()
            endpoint = 0
            break
    
        out.write(frame)
        cv2.imshow('MyBlack',frame)
        delay = int(1000/fps)
        key = cv2.waitKey(delay)
        
        # if (dt.now()-filenumber).total_seconds() >= 60 :
        #     out.release()
        #     cv2.destroyAllWindows()
        #     endpoint=1
        #     return # 프로그램이 끝난걸 어떻게 인식시킬까?
        
        if stop_recording.is_set():
            out.release()
            cv2.destroyAllWindows()
            endpoint = 0
            return
        
        if key==27:
            out.release()
            cv2.destroyAllWindows()
            endpoint = 0
            return #break
    
def folder():
    foldername=dt.now().strftime("%Y%m%d-%H%M")
    path=os.path.join('data/blackbox/',foldername)
    try:
        os.mkdir(path)
    except:
        shutil.rmtree(path)
        os.mkdir(path)
        
    return path
        
def stroage(path):
    total=0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total+=entry.stat().st_size
            elif entry.is_dir():
                total+=stroage(entry.path)
    return total

if __name__ == "__main__" :
    cap=cv2.VideoCapture(0,cv2.CAP_MSMF) # direct show , 카메라 로딩 시 gstreamer 같은 추가 라이브러리 x DS_HOW 하면 fps잘못읽어옴
    endpoint=1 # 넣을수는 없을까?     
    while (endpoint==1):
        foldernumber=dt.now()
        newfolder=folder()
        
        # if endpoint==0:
        #     break
        
        while endpoint==1:
            videorecord(newfolder)
            
            if (dt.now()-foldernumber).total_seconds() >= 3600:
                break
        
        if stroage("data/blackbox") >= 3221225472: #3gb, 폴더제거는 1시간에 1번 이루어짐 
            older=min(os.listdir("data/blackbox"))
            olderpath=os.path.join('data/blackbox/',older)
            shutil.rmtree(olderpath)
            print(f"{older} is deleted")


    if cap.isOpened():
        cap.release()
    