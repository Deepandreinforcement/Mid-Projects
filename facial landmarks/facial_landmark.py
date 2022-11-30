# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 21:16:47 2022

@author: desezen
"""

import cv2
import numpy as np
import dlib

detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def empty(a):
    pass


cv2.namedWindow("BGR")
cv2.resizeWindow("BGR",600,200)
cv2.createTrackbar('Blue','BGR',0,255,empty)
cv2.createTrackbar('Green','BGR',0,255,empty)
cv2.createTrackbar('Red','BGR',0,255,empty)

cv2.createTrackbar('Konum','BGR',0,4,empty)

li=1
def createBox(img,points,scale=5,masked=False,cropped=True):
    if masked:
    
    
        mask=np.zeros_like(img)
        mask=cv2.fillPoly(mask,[points],(255,255,255))
        
        img=cv2.bitwise_and(img,mask)
        #cv2.imshow("mask",mask)
    if cropped:
        bbox=cv2.boundingRect(points)
        x,y,w,h=bbox
        imgCrop=img[y:y+h,x:x+w]
        imgCrop=cv2.resize(imgCrop,(0,0),None,scale,scale)
        return imgCrop
    else:
        return mask
degis=1
dem=1
while True:
    key=cv2.waitKey(1)
    if key==ord('a'):
        if degis!=1:
            degis=degis-1

            
    elif key==ord('s'):
        if degis!=3:
            degis=degis+1 
    
        
    elif key==ord('q'):
       break
    print(degis)
    
    
 
    if degis==1:
        img=cv2.imread('i1.jpg')
        img=cv2.resize(img,(800,600))
    elif degis==2:
        img=cv2.imread('i3.jpg')
        img=cv2.resize(img,(800,600))
    elif degis==3:
        img=cv2.imread('i4.jpg')
        img=cv2.resize(img,(800,600))
    imgOriginal=img.copy()
    
    
    
    
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=detector(imgGray)
    
    
    for face in faces:
        x1,y1=face.left(),face.top()
        x2,y2=face.right(),face.bottom()
        #imgOriginal=cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
        landmarks=predictor(imgGray,face)
        mypoints=[]
        for n in range(68):
            
            x=landmarks.part(n).x
            y=landmarks.part(n).y
            mypoints.append([x,y])
            #cv2.circle(imgOriginal,(x,y),5,(50,50,255),cv2.FILLED)
            #cv2.putText(imgOriginal,str(n),(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.4,(0,0,255),1)
        
        
        
        mypoints=np.array(mypoints)
        #lefteye=createBox(img,mypoints[36:42])
        li=cv2.getTrackbarPos('Konum','BGR')
        if li==0:
            lips=createBox(img,mypoints[17:22],3,masked=True,cropped=False)
        if li==1:
            lips=createBox(img,mypoints[22:27],3,masked=True,cropped=False)
        if li==2:
            lips=createBox(img,mypoints[36:42],3,masked=True,cropped=False)
        if li==3:
            lips=createBox(img,mypoints[42:48],3,masked=True,cropped=False)
        if li==4:
            lips=createBox(img,mypoints[48:61],3,masked=True,cropped=False)            
        #lips=createBox(img,mypoints[36:48],3,masked=True,cropped=False)
        #lips=createBox(img,mypoints[48:61],3,masked=True,cropped=False)
        
        
        imgcolorLips=np.zeros_like(lips)
        if dem!=degis:
            cv2.setTrackbarPos('Blue','BGR',0)
            cv2.setTrackbarPos('Red','BGR',0)
            cv2.setTrackbarPos('Green','BGR',0)
            dem=degis
        b=cv2.getTrackbarPos('Blue','BGR')
        g=cv2.getTrackbarPos('Green','BGR')
        r=cv2.getTrackbarPos('Red','BGR')
        imgcolorLips[:]=b,g,r
        
        imgcolorLips=cv2.bitwise_and(lips,imgcolorLips)
        imgcolorLips=cv2.GaussianBlur(imgcolorLips,(7,7),10)
        #imgOriginalGray=cv2.cvtColor(imgOriginal,cv2.COLOR_BGR2GRAY)
        #imgOriginalGray=cv2.cvtColor(imgOriginalGray,cv2.COLOR_GRAY2BGR)
        imgcolorLips=cv2.addWeighted(imgOriginal,1,imgcolorLips,0.6,0)
        #imgOriginal=imgcolorLips
        #cv2.imshow('lefteye',lips)
        cv2.imshow('BGR',imgcolorLips)
    
    #cv2.imshow('original',imgOriginal)

cv2.destroyAllWindows()
