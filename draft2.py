import cv2
import numpy as np

cap=cv2.VideoCapture(0)
ret, f=cap.read()
row, col, dim=f.shape
print("{0},{1}".format(row, col))

tik=0
frame2=np.zeros(f.shape, dtype=np.uint8)
while(1):
    ret, frame=cap.read()
    cv2.imshow("camera", frame)
    tik+=1
    if cv2.waitKey(1) & 0xFF==27:
        break
    if tik%5==0 or True:
        frame1=frame2.copy()
        frame2=frame.copy()
        sub=frame2-frame1
        cv2.imshow("subtrate", sub)
cap.release()
cv2.destroyAllWindows()
