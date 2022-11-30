import cv2
import numpy as np

img = cv2.imread ( "istanbul.jpg" ) 
slic = cv2.ximgproc.createSuperpixelSLIC ( img , region_size = 10 )  
slic.iterate ( 10 )      
mask_slic = slic.getLabelContourMask ( )
mask_inv_slic = cv2.bitwise_not ( mask_slic )   

img_slic = cv2.bitwise_and ( img , img , mask =  mask_inv_slic )
cv2.imshow ( "img_slic" , img_slic ) 

cv2.waitKey ( ) 
cv2.destroyAllWindows()

