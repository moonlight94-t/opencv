import sys
import numpy as np
import cv2
src=cv2.imread('red.jpg')

hsv= cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
redmask = cv2.inRange(hsv,(0,155,50),(10,255,255))
yellowmask = cv2.inRange(hsv,(15,110,50),(50,255,255))
greenmask = cv2.inRange(hsv,(40,155,50),(80,255,255))


red1 = cv2.copyTo(hsv,redmask)
yel1 = cv2.copyTo(hsv,yellowmask)
gre1 = cv2.copyTo(hsv,greenmask)

#cv2.bitwise_or

red2=cv2.countNonZero(redmask) # countNonZero는 copyTo 된거 넣으면 에러, 아마 그레이 스케일 넣어야 되나봄 
yel2=cv2.countNonZero(yellowmask)
gre2=cv2.countNonZero(greenmask)

if red2 > yel2 and red2 > gre2 :
    print("red signal")
elif yel2 > gre2 and yel2 > red2:
    print("yellow signal")
elif gre2 > yel2 and gre2 > red2:
    print("green signal")
else:
    print("unknown")

# cv2.imshow('red',red1)
# cv2.imshow('yel',yel1)
# cv2.imshow('gre',gre1)

# cv2.waitKey()
# cv2.destroyAllWindows()