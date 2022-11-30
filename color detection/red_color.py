# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:20:41 2022

@author: desezen
"""

import cv2
import numpy as np
img=cv2.imread('t.jpg') # resmi yükleme

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# red color
low_red=np.array([170, 50, 70])
high_red=np.array([180, 255, 255])
 
mask = cv2.inRange(hsv_img, low_red, high_red)
mask = cv2.erode(mask,None,iterations=2)
mask = cv2.dilate(mask,None,iterations=2)
mask = cv2.GaussianBlur(mask, (3, 3), 0)
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, 
                        cv2.CHAIN_APPROX_SIMPLE)[-2]

for cnt in cnts:
    (x, y, w, h) = cv2.boundingRect(cnt)
    
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

cv2.imshow("kamera",img)
cv2.waitKey(0)
cv2.destroyAllWindows()








