import cv2
import numpy as np
kamera= cv2.VideoCapture('video5.mp4')
while True:
    ret,frame=kamera.read()
    frame=cv2.resize(frame,None,fx=0.2,fy=0.2)
   
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_red = np.array([160, 70, 50])
    high_red = np.array([180, 255, 255])
    mask = cv2.inRange(hsv_frame, low_red, high_red)
    #mask = cv2.erode(mask,None,iterations=2)
    mask = cv2.dilate(mask,None,iterations=2)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    print(cnts)
    maxw=0
    m1=0
    m2=0
    m3=0
    for cnt in cnts:
        (x, y, w, h) = cv2.boundingRect(cnt)
        if w>maxw:
            maxw=w
            m1=x
            m2=y
            m3=h
            
    cv2.rectangle(frame,(m1,m2),(m1+maxw,m2+m3),(255,0,0),3)
    
    cv2.imshow("kamera",frame)
  
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kamera.release() 
cv2.destroyAllWindows()