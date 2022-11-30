# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:20:57 2022

@author: desezen
"""
import cv2
kamera= cv2.VideoCapture(0)
# Takip algoritmasını dahil ediyoruz.
trackers= cv2.legacy.MultiTracker_create()
while True:
    ret,kare=kamera.read()
    # burada görüntüde takip algoritmasını uygulayıp sonuçları alıyoruz.
    # fakat ilk başta çalışmaz çünkü takip edilecek nesne belli değil
    # burada boxes ile nesneyi kare içine alacağız.
    success,boxes=trackers.update(kare)
    # her bir nesne için bir kare olacak
    for box in boxes:
        # koordinatları integer veri tipine çevirdik 
        x,y,w,h=int(box[0]),int(box[1]),int(box[2]),int(box[3])
        # kutuyu çizdirdik
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,255),3,1)
    # burada 1 ms bekler ve kullanıcıdan bir giriş bekler.
    key=cv2.waitKey(1)
    # eğer a harfine basılırsa takip edilmesi istenen nesneyi kare içine almak 
    # için video durur
    if key==ord('a'):  
        # bununla istenen nesneyi kare içine alıyoruz.
        bbox=cv2.selectROI("kamera",kare)
        # bir tane takip algoritması oluşturduk.
        tracker= cv2.legacy.TrackerKCF_create()
        # bunları asıl takip algoritmasının içine ekliyoruz
        trackers.add(tracker,kare,bbox)
    # q harfine basınca videodan çıkar 
    elif key==ord('q'):
        break
    cv2.imshow("kamera",kare)
kamera.release()
cv2.destroyAllWindows()
