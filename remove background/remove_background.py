# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:04:37 2022

@author: desezen
"""

import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation

img=cv2.imread('messi.jpg') #orjinal resim
h,w,_=img.shape
segmentor=SelfiSegmentation()
h=900
w=1000
img=cv2.resize(img,(w,h))

imgBg=cv2.imread('i1.jpg') # yeni arka plan olması istenen resim
imgBg=cv2.resize(imgBg,(w,h))

thresh=0.8
segmentor=SelfiSegmentation()


new1=segmentor.removeBG(img,imgBg,threshold=thresh)# arka planda yeni resim olur

beyaz=(255,255,255) #beyaz rengin BGR kodu
new2=segmentor.removeBG(img,beyaz,threshold=thresh) # arka plan  beyaz olur

mavi=(255,0,0) # mavi rengin BGR kodu
new3=segmentor.removeBG(img,mavi,threshold=thresh)#arka plan mavi olur
    
# resimleri gösterme
cv2.imshow('image',img)
cv2.imshow('New Image 1',new1)
cv2.imshow('New Image 2',new2)
cv2.imshow('New Image 3',new3)

#yeni resimleri .jpg formatında kaydetme
cv2.imwrite('img1.jpg',new1)
cv2.imwrite('img2.jpg',new2)
cv2.imwrite('img3.jpg',new3)
cv2.imwrite('img4.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



