
import cv2
import numpy as np
import face_recognition
import time
import pickle

with open("fut.pkl", "rb") as fp:   # Unpickling
    images = pickle.load(fp)


with open("futn.pkl", "rb") as fp:   # Unpickling
    names = pickle.load(fp)

print('kalibrasyon yapılıyor')


enc=[]

for i in range(50):
    m1=images[i]
    m1=cv2.resize(m1,None,fx=0.5,fy=0.5)
    enm=face_recognition.face_encodings(m1)
    enc.append(enm)
    print(i)
    print("k")
print('kalibrasyon bitti')



kamera= cv2.VideoCapture('video.mp4')



name=''

matchedfaces=[]
while True:
    
   
    ret,kare=kamera.read()
    wi,he,_=kare.shape
    kare=kare[0:wi*4//5,0:he]
    kare=cv2.resize(kare,None,fx=0.7,fy=0.7)
    faceloc=face_recognition.face_locations(kare)
    enmt=face_recognition.face_encodings(kare,faceloc)
            
            
    
    for i in range(50):
        enm1=enc[i]
        if enmt==[] or enm1==[]:
            pass
        else:
            matchedfaces=face_recognition.compare_faces(enm1[0],enmt)
            if True in matchedfaces:
               
                
                print(names[i])
                name=names[i]
                break
           
            else:
                pass
                #print(i)
        
        
        
    for (y,x2,y2,x) in faceloc:
             
        
        cv2.rectangle(kare,(x,y),(x2,y2),(255,0,0),2)
        cv2.putText(kare, name,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 220, 255), 2)
    
    cv2.imshow("kamera",kare)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()

cv2.destroyAllWindows()