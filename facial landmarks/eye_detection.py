# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:21:53 2022

@author: desezen
"""

import cv2
import numpy as np
import dlib





detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

img=cv2.imread('eye1.jpg')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
faces=detector(imgGray)
    
    
for face in faces:
    x1,y1=face.left(),face.top()
    x2,y2=face.right(),face.bottom()
    #img=cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
landmarks=predictor(imgGray,face)
mypoints=[]
for n in range(68):
            
    x=landmarks.part(n).x
    y=landmarks.part(n).y
    mypoints.append([x,y])
#for x,y in mypoints[36:41]:
x,y=mypoints[40]
#cv2.circle(img,(x,y),5,(50,50,255),cv2.FILLED)

x1,y1=mypoints[37]
x2,y2=mypoints[40]
yeni=img[y1:y2,x1:x2]      
w1=x2-x1
h1=y2-y1

yeni=cv2.resize(yeni,(4*w1,4*h1))
cv2.imshow('original',img)
cv2.imshow('yeni',yeni)
cv2.waitKey(0)
cv2.destroyAllWindows()
