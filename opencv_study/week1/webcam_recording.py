import cv2, sys

cap=cv2.VideoCapture(0)

framesize=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #codec
out1 = cv2.VideoWriter('data/record0.mp4',fourcc,fps,framesize)
out2 = cv2.VideoWriter('data/record2.mp4',fourcc,fps,framesize, isColor=False)

while (True):
    retval, frame = cap.read()
    
    if not retval:
        break
    
    out1.write(frame)
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(gray)
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    
    key = cv2.waitKey(int(1000/fps))
    if key==27:
        break

if cap.isOpened():
    cap.release()
    out1.release()
    out2.release()
    cv2.destroyAllWindows()