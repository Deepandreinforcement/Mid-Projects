# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 20:11:52 2022

@author: desezen
"""
import cv2
# orijinal videyou yüklüyoruz. Bendeki videonun adı ve uzantısı video.mp4
kamera= cv2.VideoCapture('video.mp4')
# kaydedici için format
x=cv2.VideoWriter_fourcc(*"XVID") 
# kaydediciyi ayarladık. ters.avi oluşacak dosyanın adı, 30 fps değeri
# 1000,1000 ise videonun boyutu. Bu boyut orjinal videonun boyutu olmalı 
# Yoksa hata alabilirsiniz. Ya da oluşturulan video boş olabilir
out=cv2.VideoWriter('ters2.avi',x,30,(1000,1000)) 
ret= True
a=[]
while ret:
    ret,kare=kamera.read() 
    print('Video hazırlanıyor')
    if ret:
        a.append(kare)
b=len(a)

for i in range(b):
    yeni=a[b-i-1]
    out.write(yeni)
    print('Yeni video oluşturuluyor')
kamera.release() 
cv2.destroyAllWindows()




