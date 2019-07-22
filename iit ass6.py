import cv2
import numpy as np 
import math
img1= cv2.imread("C:\\Users\\Akash\\Desktop\\download12.png")	

img2=cv2.resize(img1,(500,500))
cv2.imshow("original",img2)

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

def down(img2):
	m,n,c=img2.shape
	x=int(m/2)
	y=int(n/2)
	b=2
	out2=np.zeros((int(m/2),int(n/2),c),np.uint8)

	arr0=[]
	arr1=[]
	arr2=[]
	for i in range(x):
	    
	    for j in range(y):
	        
	        for l in range(i*b,i*b+b):
	            for m in range(j*b,j*b+b):
	                arr0.append(img2[l][m][0])
	                arr1.append(img2[l][m][1])
	                arr2.append(img2[l][m][2])
	        out2[i][j][0]=np.average(arr0)
	        out2[i][j][1]=np.average(arr1)
	        out2[i][j][2]=np.average(arr2)
	        arr0=[]
	        arr1=[]
	        arr2=[]
	return out2

img3=down(img2)
img4=down(img3) 
cv2.imshow('l1',img3)  
cv2.imshow('l2',img4)
a=cv2.waitKey(0)

def up(img2):
	a=2
	m,n,c=img2.shape
	out1=np.zeros((m*a,n*a,c),np.uint8)
	
	ker=np.zeros((a,a,c))
	for i in range(m):
	    for j in range(n):
	        for k in range(a):
	            for l in range(a):
	                out1[i*a+k][j*a+l][0]=img2[i][j][0]
	                out1[i*a+k][j*a+l][1]=img2[i][j][1]
	                out1[i*a+k][j*a+l][2]=img2[i][j][2]

	return out1
img5=up(img3)
img6=up(img4)
#cv2.imshow('image3',out1)   
 
cv2.imshow('l3',img5)  
a=cv2.imshow('l4',img6)
a=cv2.waitKey(0)
img7=img5-img2
cv2.imshow('l555',img7) 
a=cv2.waitKey(0)
img8=img6-img3
cv2.imshow('l6',img8) 
a=cv2.waitKey(0)
cv2.destroyAllWindows() 

