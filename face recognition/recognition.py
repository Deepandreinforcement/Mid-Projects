# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:46:29 2021

@author: desezen
"""

import cv2
import face_recognition
 



mtc=cv2.imread("rm.jpg") # test resminin opencv ile yüklenmesi
#3mtc=cv2.resize(mtc,(1000, 1000))
m1=face_recognition.load_image_file("messi1.jpg")
#mt=face_recognition.load_image_file("messin1.jpg")

enm1=face_recognition.face_encodings(m1)[0] # m1 resmindeki yüzlerin encoding hali 
# sadece 1 yüz olduğu için bir tene liste var ama birden fazla olursa kodun sonuna [0] eklemek lazım 1.yüz için

fmt=face_recognition.face_locations(mtc) # test resmindeki yüzün konumları

enmt=face_recognition.face_encodings(mtc,fmt)




matchedfaces=face_recognition.compare_faces(enm1,enmt)


a=0
for i in matchedfaces:
    
    if i:
        for (y,x2,y2,x) in [fmt[a]]:
            cv2.rectangle(mtc,(x,y),(x2,y2),(0,255,0),2)
            cv2.putText(mtc, "He is Messi",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 200, 255), 2)
        print("He is messi")
        cv2.imshow("test",mtc)
    else:
        for (y3,x4,y4,x3) in [fmt[a]]:
            cv2.rectangle(mtc,(x3,y3),(x4,y4),(0,255,0),2)
            cv2.putText(mtc, "He is not Messi",(x3,y3), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 220, 255), 2)
        print("He is not messi")
        cv2.imshow("test",mtc)
    a=a+1
#cv2.imwrite('saving.jpg', mtc)

cv2.waitKey(0)
cv2.destroyAllWindows()