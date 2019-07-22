# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 02:30:10 2019

@author: Akash
"""

import cv2
import numpy as np
import math

def error_rms(img1, img2):
    m,n = img1.shape
    total = m*n
    sum=0
    #rms error
    for i in range(m):
        for j in range(n):
            sum+= (img1[i][j]-img2[i][j])*(img1[i][j]-img2[i][j])

    error_generated = math.sqrt(sum/total)
    return error_generated


img = cv2.imread('C:\\Users\\Akash\\Desktop\\download.jpg',0)
cv2.imshow("real",img)

#using inbuilt funciton to blur taking kernel 3*3
blur = cv2.blur(img,(3,3))

#hardcoding by averaging technique

m, n= img.shape
# Taking kernel size fixed as 3
k = 3



kernal0 = np.zeros([k,k,1],np.uint8)
img1 = np.zeros([m-k+1,n-k+1], np.uint8)



for i in range(m-k+1):
    for j in range(n-k+1):
        for a in range(k):
            for b in range(k):
                kernal0[a][b] = img[i+a][j+b]

        img1[i][j] = np.average(kernal0)

#calculation error between the inbuilt function and hardcoded img
#error = error_rms(img1, blur)
#print("Error is:",error)

cv2.imshow("blurred image",img1)
cv2.imshow("inbulitBlurring_function", blur)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
    
print(error_rms(img1,blur))