# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:59:43 2022

@author: desezen
"""

import cvzone
import cv2
import numpy as np
import math
import random
from cvzone.HandTrackingModule import HandDetector
import time


detector=HandDetector(maxHands=1)

cap=cv2.VideoCapture(0)

width=1280
height=720

cap.set(3,width)
cap.set(4,height)


class SnakeGameClass:
    def __init__(self,pathFood):
        self.points=[]
        self.lengths=[]
        self.currentLength=0
        self.allowedLength=150
        self.previousHead=0,0
        self.score=0
        self.gameover=False
        
        self.tic=False
        self.imgFood=cv2.imread(pathFood,cv2.IMREAD_UNCHANGED)
        self.imgFood=cv2.resize(self.imgFood,(80,80))
        self.hfood,self.wfood,_=self.imgFood.shape
        self.foodpoint=0,0
        self.randomFoodLocation()
        
    def randomFoodLocation(self):
        self.foodpoint=random.randint(100,1000),random.randint(100,600)
        
        
        
        
    def update(self, imgMain, currentHead,zaman):
        self.gameover=False
        self.tic=False
        imgMain[10:60,10:250,:]=imgMain[10:60,10:250,:]*0+255
        scr="Score: " +str(self.score)
        
        cv2.putText(imgMain,scr,(10,50),cv2.FONT_HERSHEY_SIMPLEX, 1.5,(0,150,255),2)
        zaman=zaman*10
        zaman=float(int(zaman))
        zaman=zaman/10
        
        
       
        if zaman<0:
            self.randomFoodLocation()
            self.tic=True
        imgMain[10:60,1040:1260,:]=imgMain[10:60,1040:1260,:]*0+255
        srct='Time: '+str(zaman)
        cv2.putText(imgMain,srct,(1040,50),cv2.FONT_HERSHEY_SIMPLEX, 1.5,(255,100,255),2)
        px,py=self.previousHead
        cx,cy=currentHead
        
        self.points.append([cx,cy])
        distance=math.hypot(cx-px,cy-py)
        self.lengths.append(distance)
        self.currentLength+=distance
        self.previousHead=cx,cy
        
        
        
        
        
        if self.currentLength> self.allowedLength:
            for i,length in enumerate(self.lengths):
                self.currentLength-=length
                self.lengths.pop(i)
                self.points.pop(i)
                if self.currentLength< self.allowedLength:
                    break
                
        rx,ry=self.foodpoint
        if rx-self.wfood//2<cx<rx+self.wfood//2 and ry-self.hfood//2<cy<ry+self.hfood//2:
            self.randomFoodLocation()
            self.allowedLength+=50
            self.score+=1
            self.tic=True
        

        
                
        
        if self.points:
            for i, point in enumerate(self.points):
               
                if i !=0:
                    cv2.line(imgMain,self.points[i-1],self.points[i],(0,0,255),20)
                    
            
            cv2.circle(imgMain,self.points[-1],20,(200,0,200),cv2.FILLED)   
        rx,ry=self.foodpoint
        imgMain=cvzone.overlayPNG(imgMain,self.imgFood,(rx-self.wfood//2,ry-self.hfood//2))             
        
    
    
    
    
        pts=np.array(self.points[:-2],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(imgMain,[pts],False,(0,200,0),3)
        minDist=cv2.pointPolygonTest(pts,(cx,cy), True)
        #print(minDist)
        if -1< minDist <1 and minDist!=0.0:
            
                
            self.gameover=True
        
        
        return self.gameover,imgMain,self.tic,self.score
    
    
    
game=SnakeGameClass('ci.png')
start=False
say=0
sure=3

skor=0
prev_frame_time = 0
new_frame_time = 0

timeout=False
while True:
    success,kare=cap.read()
    kare=cv2.flip(kare,1)
    kare=cv2.resize(kare,(width,height))
    img=np.copy(kare)
    hands,kare=detector.findHands(kare,flipType=False)
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    if fps>1:
        
        sure=sure-1/fps
        #print(sure)
    if hands:
        lmlist=hands[0]['lmList']
        pointIndex=lmlist[8][0:2]
        start,img,timeout,skor= game.update(img,pointIndex,sure)
    if timeout:
        sure=3
    if start:
        say=say+1
        #print('say: ',say)

    #fps = int(fps)
    #print(fps)

    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
new_img=cv2.imread('a3.jpg')
new_img=cv2.resize(new_img,(1280,720))

new_img[300:380,450:880,:]=new_img[300:380,450:880,:]*0+255
cv2.putText(new_img,'Game over',(450,365),cv2.FONT_HERSHEY_SIMPLEX, 2.5,(0,0,255),3)

skorsr='Score: '+str(skor)
new_img[500:600,450:920,:]=new_img[500:600,450:920,:]*0+255

cv2.putText(new_img,skorsr,(450,580),cv2.FONT_HERSHEY_SIMPLEX, 3,(0,150,255),3)

cv2.imshow('Image',new_img)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()















































    
    
    
    
    
    