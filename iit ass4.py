# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 05:13:59 2019

@author: Akash
"""

import cv2
import numpy as np
import math
import random
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
img = cv2.imread('C:\\Users\\Akash\\Desktop\\salt.png',0)
cv2.imshow("real",img)
a1,b1 = img.shape
noise_rem = cv2.medianBlur(img,3)

k=3
#
#for i in range(7000):
#    x = random.randint(0,a1-1)
#    y = random.randint(0,b1-1)
#    if(img[x][y]>128):
#        img[x][y] = 0
#    else:
#        img[x][y] = 255



kernal = np.zeros([k,k],np.uint8)
img1 = np.zeros([a1-k+1,b1-k+1], np.uint8)


for i in range(a1-k+1):
    for j in range(b1-k+1):
        for a in range(k):
            for b in range(k):
                kernal[a][b] = img[i+a][j+b]

        img1[i][j] = np.median(kernal)


cv2.imshow("noisy",img)
cv2.imshow("NOnoiseimage",img1)
cv2.imshow("inbulitNOiseREmoval", noise_rem)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
print(error_rms(img1,noise_rem))