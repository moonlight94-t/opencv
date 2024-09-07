import cv2
import matplotlib.pyplot as plt


src = cv2.imread('data2/Hawkes.jpg',cv2.IMREAD_GRAYSCALE)
src2= cv2.imread('data2/Hawkes_norm.jpg',cv2.IMREAD_GRAYSCALE)

dst = cv2.equalizeHist(src) # 정규화는 일정한 간격으로 벌려주는 것, equalizerHist는 데이터 수치가 높은 구간은 간격이 넓게 수치가 적은부분은 간격이 좁게 중요한것이 더 대비되게, edge가 더 선명하게 살아남
hist1 = cv2.calcHist([src2],[0],None,[256],[0,256])
hist2 = cv2.calcHist([dst],[0],None,[256],[0,256])
plt.plot(hist1)
plt.plot(hist2)

cv2.imshow('frame',src2)
cv2.imshow('frame1',dst)
plt.show()
cv2.waitKey()

cv2.destroyAllWindows()

