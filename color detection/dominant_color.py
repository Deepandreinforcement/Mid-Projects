# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:26:16 2022

@author: desezen
"""

import cv2
from sklearn.cluster import KMeans
import numpy as np
# burada denetimsiz bir makine öğremesi tekniği kullanarak resimdeki baskın 
# rengi buluyoruz. Burada Kmenas algoritması kullanılarak benzer değerlere
# sahip renkler bir araya getiriliyor.
def getdcolor(img,n):
    img = img.reshape((img.shape[0] * img.shape[1], 3))
    kmeans = KMeans(n_clusters = n)
    kmeans.fit(img)
    colors = kmeans.cluster_centers_
    return colors.astype(int)

img = cv2.imread('resim2.jpg')
# Bu değer  kaç tane  renk bulunacağını gösteriyor.
cluster=5
colors =getdcolor(img,cluster)
print(colors)
# Bulunan renkleri kullanarak 500*500 boyutunda bir
# colorbar oluşturuyoruz.
yeni=np.zeros((500,500,3),dtype=np.uint8)
yeni[:,:100]=colors[0]
yeni[:,100:200]=colors[1]
yeni[:,200:300]=colors[2]
yeni[:,300:400]=colors[3]
yeni[:,400:]=colors[4]
cv2.imshow("kamera",img)
cv2.imshow("Colorbar",yeni)
cv2.waitKey()
cv2.destroyAllWindows()

