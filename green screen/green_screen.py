# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 20:22:20 2022

@author: desezen
"""
import cv2
import numpy as np

frame=cv2.imread('green.jpg') # yeşil ekranlı resim
img=cv2.imread('main.jpg') #diğer resim

h,w,_=img.shape
frame=cv2.resize(frame,(w,h))

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# yeşilin hsv kodu duruma göre değişebilir
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])

mask = cv2.inRange(hsv_frame, low_green, high_green)
mask_inv = cv2.bitwise_not(mask)

frame = cv2.bitwise_and ( frame , frame , mask =  mask_inv )
imgnew=cv2.bitwise_and ( img , img , mask =  mask )
img=frame+imgnew

cv2.imshow("yeni image",img)
cv2.imwrite("merged.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()








