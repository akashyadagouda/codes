# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:35:01 2019

@author: Akash
"""
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\Akash\\Desktop\\black12.png,1",1)

#x1=int(input("enter x1"))
#y1=int(input("enter y1"))
#x2=int(input("enter x2"))
#y2=int(input("enter y2"))
#slope=int(0)
#dx=int(0)
#dy=int(0)
#newx=int(0)
#newy=int(0)
#slope=(y2-y1)/(x2-x1)
#for i in range(x1,x2+1):
#    if(slope<=1):
#        dx=1
#        dy=slope*dx
#    else:
#        dy=1
#        dx=dy/slope
#    x1=x1+dx
#    y1=y1+dy
#    img[x1][y1][0]=255
#    img[x1][y1][1]=255
#    img[x1][y1][2]=255
    
cv2.imshow("line",img)
    
        
    
    
    