# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:55:34 2022

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
window= pygame.display.set_mode((width,height))
pygame.display.set_caption("Balon oyunu")
fps=30
clock=pygame.time.Clock()






cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)


imgBalloon=pygame.image.load('balon.png').convert_alpha()
imgBalloon = pygame.transform.scale(imgBalloon, (100,100 ))
rectBalloon=imgBalloon.get_rect()
rectBalloon.y=500
rectBalloon.x=500

speed=10
detector=HandDetector(maxHands=1)

def resetBalloon():
    rectBalloon.x=random.randint(100,width-100)
    rectBalloon.y=height-50

bekleme=0
score=0
life=10
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

        
    rectBalloon.y-=speed
    if rectBalloon.y<0:
        resetBalloon()
        speed=speed+1
        life-=1
    if life==0:
        break

    if hands:
        hand=hands[0]
        x,y,z=hand['lmList'][8]
        if rectBalloon.collidepoint(x,y):
            score+=1
            speed=speed+1
            resetBalloon()
        
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgRGB=np.rot90(imgRGB)
    frame=pygame.surfarray.make_surface(imgRGB).convert()
    frame=pygame.transform.flip(frame,True,False)
    window.blit(frame,(0,0))
    
    
    window.blit(imgBalloon, rectBalloon)
    font1=pygame.font.Font('freesansbold.ttf',50)
    lifeScore=font1.render(f'Life: {life}', True, (255,50,50))
    window.blit(lifeScore,(900,50))
    font=pygame.font.Font('freesansbold.ttf',50)
    textScore=font.render(f'Score: {score}', True, (255,50,50))
    window.blit(textScore,(50,50))
    if bekleme==0:
        bekleme=5
        pygame.display.update()
       
    
    pygame.display.update()
    
    
    
    clock.tick(fps)
    
finish_image=pygame.image.load('a1.jpg')
finish_image = pygame.transform.scale(finish_image, (width,height ))

window.blit(finish_image,(0,0))
fontf1=pygame.font.Font('freesansbold.ttf',80)
finish_text=fontf1.render(f'Game Over', True, (255,50,50))        
window.blit(finish_text,(400,400))
fontf2=pygame.font.Font('freesansbold.ttf',80)
finish_score=fontf2.render(f'Score: {score}', True, (255,200,50))        
window.blit(finish_score,(450,500))
pygame.display.update()
time.sleep(5)
        
pygame.quit()