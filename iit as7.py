# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:01:34 2019

@author: Akash
"""
import cv2

import numpy as np 


img = cv2.imread('m1.jpg')
img_g = cv2.imread('m1.jpg',0)
test_g = cv2.imread('m23.jpg',0)
h,w,d=img.shape

brightLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

def sd(in_img):
	k=5
	temp=z=1
	for t in range(1,100):
		temp=temp+2
		if temp==k:
			z=t
			break
	print(z)
	h,w=in_img.shape
	out=np.zeros((h+2*z,w+2*z),np.uint8)
	sdarray=np.zeros((h,w),np.float32)
	for i in range(h):#padding
		for j in range(w):
			out[i+z,j+z]=in_img[i,j]
	for i in range(h):
		for j in range(w):
			cnt=0
			s=[]
			for a in range(z,z*2+1):
				for b in range(z,z*2+1):
					s.append(out[i+a,j+b])

			sdarray[i,j]=np.std(np.array(s))
	return sdarray


#ipimg is 2
def paint(ipimg,base,rgbbase):
	m,n=ipimg.shape 
	m2,n2=base.shape
	temp=np.zeros((m,n,3),np.uint8)
	sdi=sd(ipimg)
	sdt=sd(base)
	print(m,n)
	for i in range(m):
		print(i)
		for j in range(n):
			f=0
			for k in range(m2):
				for l in range(n2):
					if ipimg[i,j]==base[k,l]:
						if f==0:
							sm=abs(sdt[k,l]-sdi[i,j])  
							K=k
							L=l
							f=1
						else:
							if abs(sdt[k,l]-sdi[i,j])<sm:
								sm=abs(sdt[k,l]-sdi[i,j])
								K=k
								L=l


			temp[i,j]=rgbbase[K,L]

	return temp

test=paint(test_g,img_g,img) 

cv2.imshow("Original",img)
cv2.imshow("Test",test)
cv2.waitKey(0)