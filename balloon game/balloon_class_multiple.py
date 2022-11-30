# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:24:03 2022

@author: desezen
"""


import pygame
import cv2
import random
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time
pygame.init()


width,height=1280 ,720
class Balon:
    def __init__(self,konum_y,balon_name):
        self.imgBalloon1=pygame.image.load(balon_name).convert_alpha()
        self.imgBalloon1 = pygame.transform.scale(self.imgBalloon1, (100,100 ))
        self.rectBalloon1=self.imgBalloon1.get_rect()
        self.rectBalloon1.y=konum_y
        self.rectBalloon1.x=500
        self.speed1=10
    
    
    def resetBalloon(self):
        self.rectBalloon1.x=random.randint(100,width-100)
        self.rectBalloon1.y=height-50
    
    
    def hiz(self):
        self.rectBalloon1.y-=self.speed1
        
        
        
        
        
        

detector=HandDetector(maxHands=1)
window= pygame.display.set_mode((width,height))
pygame.display.set_caption("Balon oyunu")
fps=30
clock=pygame.time.Clock()

cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)


balon1=Balon(1500,'balon1.png')
balon2=Balon(2000,'balon2.png')
balon3=Balon(2300,'balon3.png')
balon4=Balon(2700,'balon4.png')
balon5=Balon(3000,'balon5.png')
balon6=Balon(3400,'balon6.png')
balon7=Balon(3700,'balon7.png')
balon8=Balon(4000,'balon8.png')
balon9=Balon(4400,'balon9.png')
balon10=Balon(4800,'balon10.png')


score=0
life=40
start=True

while start:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            start=False
            pygame.quit()
    success,img=cap.read()
    img=cv2.flip(img,1)
    img=cv2.resize(img,(width,height))
    
    
    hands,img=detector.findHands(img,flipType=False)

        
    balon1.hiz()
    balon2.hiz()
    balon3.hiz()
    balon4.hiz()
    balon5.hiz()
    balon6.hiz()
    balon7.hiz()
    balon8.hiz()
    balon9.hiz()
    balon10.hiz()
    
    if balon1.rectBalloon1.y<0:
        balon1.resetBalloon()
        life-=1
        
        
    if balon2.rectBalloon1.y<0:
        balon2.resetBalloon()
        life-=1
        
        
    if balon3.rectBalloon1.y<0:
        balon3.resetBalloon()
        life-=1
        
    if balon4.rectBalloon1.y<0:
        balon4.resetBalloon()
        life-=1

    if balon5.rectBalloon1.y<0:
        balon5.resetBalloon()
        life-=1

    if balon6.rectBalloon1.y<0:
        balon6.resetBalloon()
        life-=1

    if balon7.rectBalloon1.y<0:
        balon7.resetBalloon()
        life-=1

    if balon8.rectBalloon1.y<0:
        balon8.resetBalloon()
        life-=1

    if balon9.rectBalloon1.y<0:
        balon9.resetBalloon()
        life-=1

    if balon10.rectBalloon1.y<0:
        balon10.resetBalloon()
        life-=1


  
    if life==0 or life<0:
        break

    if hands:
        hand=hands[0]
        x,y,z=hand['lmList'][8]
        
        
        if balon1.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon1.speed1 <15:
                balon1.speed1=balon1.speed1+1
            balon1.resetBalloon()

        if balon2.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon2.speed1 <15:
                balon2.speed1=balon2.speed1+1
            balon2.resetBalloon()

        if balon3.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon3.speed1 <15:
                balon3.speed1=balon3.speed1+1
            balon3.resetBalloon()

        if balon4.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon4.speed1 <15:
                balon4.speed1=balon4.speed1+1
            balon4.resetBalloon()

        if balon5.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon5.speed1 <15:
                balon5.speed1=balon5.speed1+1
            balon5.resetBalloon()

        if balon6.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon6.speed1 <15:    
                balon6.speed1=balon6.speed1+1
            balon6.resetBalloon()

        if balon7.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon7.speed1 <15:
                balon7.speed1=balon7.speed1+1
            balon7.resetBalloon()

        if balon8.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon8.speed1 <15:
                balon8.speed1=balon8.speed1+1
            balon8.resetBalloon()

        if balon9.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon9.speed1 <15:
                balon9.speed1=balon9.speed1+1
            balon9.resetBalloon()

        if balon10.rectBalloon1.collidepoint(x,y):
            score+=1
            if balon10.speed1 <15:
                balon10.speed1=balon10.speed1+1
            balon10.resetBalloon()

    
        
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgRGB=np.rot90(imgRGB)
    frame=pygame.surfarray.make_surface(imgRGB).convert()
    frame=pygame.transform.flip(frame,True,False)
    window.blit(frame,(0,0))
    
    
    window.blit(balon1.imgBalloon1, balon1.rectBalloon1)
    window.blit(balon2.imgBalloon1, balon2.rectBalloon1)
    window.blit(balon3.imgBalloon1, balon3.rectBalloon1)
    window.blit(balon4.imgBalloon1, balon4.rectBalloon1)
    window.blit(balon5.imgBalloon1, balon5.rectBalloon1)
    window.blit(balon6.imgBalloon1, balon6.rectBalloon1)
    window.blit(balon7.imgBalloon1, balon7.rectBalloon1)
    window.blit(balon8.imgBalloon1, balon8.rectBalloon1)
    window.blit(balon9.imgBalloon1, balon9.rectBalloon1)
    window.blit(balon10.imgBalloon1, balon10.rectBalloon1)
    
    
    
    
    
    font1=pygame.font.Font('freesansbold.ttf',50)
    lifeScore=font1.render(f'Life: {life}', True, (255,50,255))
    window.blit(lifeScore,(1050,20))
    font=pygame.font.Font('freesansbold.ttf',50)
    textScore=font.render(f'Score: {score}', True, (50,255,255))
    window.blit(textScore,(10,20))

       
    
    pygame.display.update()
    
    
    
    clock.tick(fps)
    
finish_image=pygame.image.load('a3.jpg')
finish_image = pygame.transform.scale(finish_image, (width,height ))

window.blit(finish_image,(0,0))
pygame.draw.rect(window,(255,255,255),(360,250,500,110),border_radius=30)
fontf1=pygame.font.Font('freesansbold.ttf',80)
finish_text=fontf1.render(f'Game Over', True, (255,5,5))        
window.blit(finish_text,(400,270))
pygame.draw.rect(window,(255,255,255),(360,430,500,110),border_radius=30)
fontf2=pygame.font.Font('freesansbold.ttf',80)
finish_score=fontf2.render(f'Score: {score}', True, (255,180,0))        
window.blit(finish_score,(450,450))
pygame.display.update()
time.sleep(5)
        
pygame.quit()
