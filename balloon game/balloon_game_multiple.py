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


imgBalloon1=pygame.image.load('balon1.png').convert_alpha()
imgBalloon1 = pygame.transform.scale(imgBalloon1, (100,100 ))
rectBalloon1=imgBalloon1.get_rect()
rectBalloon1.y=1500
rectBalloon1.x=500

imgBalloon2=pygame.image.load('balon2.png').convert_alpha()
imgBalloon2 = pygame.transform.scale(imgBalloon2, (100,100 ))
rectBalloon2=imgBalloon2.get_rect()
rectBalloon2.y=2000
rectBalloon2.x=random.randint(100,width-100)

imgBalloon3=pygame.image.load('balon3.png').convert_alpha()
imgBalloon3 = pygame.transform.scale(imgBalloon3, (100,100 ))
rectBalloon3=imgBalloon3.get_rect()
rectBalloon3.y=2300
rectBalloon3.x=random.randint(100,width-100)

imgBalloon4=pygame.image.load('balon4.png').convert_alpha()
imgBalloon4 = pygame.transform.scale(imgBalloon4, (100,100 ))
rectBalloon4=imgBalloon4.get_rect()
rectBalloon4.y=2700
rectBalloon4.x=random.randint(100,width-100)

imgBalloon5=pygame.image.load('balon5.png').convert_alpha()
imgBalloon5 = pygame.transform.scale(imgBalloon5, (100,100 ))
rectBalloon5=imgBalloon5.get_rect()
rectBalloon5.y=3000
rectBalloon5.x=random.randint(100,width-100)


imgBalloon6=pygame.image.load('balon6.png').convert_alpha()
imgBalloon6 = pygame.transform.scale(imgBalloon6, (100,100 ))
rectBalloon6=imgBalloon6.get_rect()
rectBalloon6.y=3400
rectBalloon6.x=random.randint(100,width-100)




imgBalloon7=pygame.image.load('balon7.png').convert_alpha()
imgBalloon7 = pygame.transform.scale(imgBalloon7, (100,100 ))
rectBalloon7=imgBalloon7.get_rect()
rectBalloon7.y=3700
rectBalloon7.x=random.randint(100,width-100)



imgBalloon8=pygame.image.load('balon8.png').convert_alpha()
imgBalloon8 = pygame.transform.scale(imgBalloon8, (100,100 ))
rectBalloon8=imgBalloon8.get_rect()
rectBalloon8.y=4000
rectBalloon8.x=random.randint(100,width-100)


imgBalloon9=pygame.image.load('balon9.png').convert_alpha()
imgBalloon9 = pygame.transform.scale(imgBalloon9, (100,100 ))
rectBalloon9=imgBalloon9.get_rect()
rectBalloon9.y=4400
rectBalloon9.x=random.randint(100,width-100)


imgBalloon10=pygame.image.load('balon10.png').convert_alpha()
imgBalloon10 = pygame.transform.scale(imgBalloon10, (100,100 ))
rectBalloon10=imgBalloon10.get_rect()
rectBalloon10.y=4800
rectBalloon10.x=random.randint(100,width-100)










speed1=10
speed2=10
speed3=10
speed4=10
speed5=10
speed6=10
speed7=10
speed8=10
speed9=10
speed10=10







detector=HandDetector(maxHands=1)



def resetBalloon1():
    rectBalloon1.x=random.randint(100,width-100)
    rectBalloon1.y=height-50


def resetBalloon2():
    rectBalloon2.x=random.randint(100,width-100)
    rectBalloon2.y=height-50
    

def resetBalloon3():
    rectBalloon3.x=random.randint(100,width-100)
    rectBalloon3.y=height-50


def resetBalloon4():
    rectBalloon4.x=random.randint(100,width-100)
    rectBalloon4.y=height-50


def resetBalloon5():
    rectBalloon5.x=random.randint(100,width-100)
    rectBalloon5.y=height-50


def resetBalloon6():
    rectBalloon6.x=random.randint(100,width-100)
    rectBalloon6.y=height-50


def resetBalloon7():
    rectBalloon7.x=random.randint(100,width-100)
    rectBalloon7.y=height-50


def resetBalloon8():
    rectBalloon8.x=random.randint(100,width-100)
    rectBalloon8.y=height-50


def resetBalloon9():
    rectBalloon9.x=random.randint(100,width-100)
    rectBalloon9.y=height-50


def resetBalloon10():
    rectBalloon10.x=random.randint(100,width-100)
    rectBalloon10.y=height-50







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

        
    rectBalloon1.y-=speed1
    rectBalloon2.y-=speed2
    rectBalloon3.y-=speed3
    rectBalloon4.y-=speed4
    rectBalloon5.y-=speed5
    rectBalloon6.y-=speed6
    rectBalloon7.y-=speed7
    rectBalloon8.y-=speed8
    rectBalloon9.y-=speed9
    rectBalloon10.y-=speed10
    
    if rectBalloon1.y<0:
        resetBalloon1()
        #speed1=speed1+1
        life-=1
        
        
    if rectBalloon2.y<0:
        resetBalloon2()
        #speed2=speed2+1
        life-=1
        
        
    if rectBalloon3.y<0:
        resetBalloon3()
        #speed3=speed3+1
        life-=1
        
    if rectBalloon4.y<0:
        resetBalloon4()
        #speed4=speed4+1
        life-=1

    if rectBalloon5.y<0:
        resetBalloon5()
        #speed5=speed5+1
        life-=1

    if rectBalloon6.y<0:
        resetBalloon6()
        #speed6=speed6+1
        life-=1

    if rectBalloon7.y<0:
        resetBalloon7()
        #speed7=speed7+1
        life-=1

    if rectBalloon8.y<0:
        resetBalloon8()
        #speed8=speed8+1
        life-=1

    if rectBalloon9.y<0:
        resetBalloon9()
        #speed9=speed9+1
        life-=1

    if rectBalloon10.y<0:
        resetBalloon10()
        #speed10=speed10+1
        life-=1


  
    if life==0 or life<0:
        break

    if hands:
        hand=hands[0]
        x,y,z=hand['lmList'][8]
        
        
        if rectBalloon1.collidepoint(x,y):
            score+=1
            if speed1 <15:
                
                speed1=speed1+1
            resetBalloon1()

        if rectBalloon2.collidepoint(x,y):
            score+=1
            if speed2 <15:
                speed2=speed2+1
            resetBalloon2()

        if rectBalloon3.collidepoint(x,y):
            score+=1
            if speed3 <15:
                speed3=speed3+1
            resetBalloon3()

        if rectBalloon4.collidepoint(x,y):
            score+=1
            if speed4 <15:
                speed4=speed4+1
            resetBalloon4()

        if rectBalloon5.collidepoint(x,y):
            score+=1
            if speed4 <15:
                speed5=speed5+1
            resetBalloon5()

        if rectBalloon6.collidepoint(x,y):
            score+=1
            if speed6 <15:    
                speed6=speed6+1
            resetBalloon6()

        if rectBalloon7.collidepoint(x,y):
            score+=1
            if speed7 <15:
                speed7=speed7+1
            resetBalloon7()

        if rectBalloon8.collidepoint(x,y):
            score+=1
            if speed8 <15:
                speed8=speed8+1
            resetBalloon8()

        if rectBalloon9.collidepoint(x,y):
            score+=1
            if speed9 <15:
                speed9=speed9+1
            resetBalloon9()

        if rectBalloon10.collidepoint(x,y):
            score+=1
            if speed10 <15:
                speed10=speed10+1
            resetBalloon10()

    
        
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgRGB=np.rot90(imgRGB)
    frame=pygame.surfarray.make_surface(imgRGB).convert()
    frame=pygame.transform.flip(frame,True,False)
    window.blit(frame,(0,0))
    
    
    window.blit(imgBalloon1, rectBalloon1)
    window.blit(imgBalloon2, rectBalloon2)
    window.blit(imgBalloon3, rectBalloon3)
    window.blit(imgBalloon4, rectBalloon4)
    window.blit(imgBalloon5, rectBalloon5)
    window.blit(imgBalloon6, rectBalloon6)
    window.blit(imgBalloon7, rectBalloon7)
    window.blit(imgBalloon8, rectBalloon8)
    window.blit(imgBalloon9, rectBalloon9)
    window.blit(imgBalloon10, rectBalloon10)
    
    
    
    
    
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