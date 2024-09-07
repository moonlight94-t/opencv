import cv2, sys

cap=cv2.VideoCapture(0)

a1=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
a2=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
#print(a1,a2)

while(True):
    retval, frame = cap.read()
    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(100) # 10fps니까 100ms 대기
    if key==27: # ascii에서 esc가 27임
        break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()