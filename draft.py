import cv2
img=cv2.imread("image.jpg")
img=cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.namedWindow("src",0)
cv2.imshow("src", img)
cv2.waitKey(0)
