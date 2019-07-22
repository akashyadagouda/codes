
import cv2
import numpy as np
import matplotlib.pyplot as plt 
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
img=cv2.imread("C:\\Users\\Akash\\Desktop\\Dataset\\4.2.07.tiff",0)
cv2.imshow("original",img)
m,n=img.shape
arr=np.zeros(256)
imgnew=np.zeros([m,n],np.uint8)
di=np.zeros([m,n],np.uint8)


res=m*n


for i in range(m):
	for j in range(n):
		p=img[i][j]
		arr[p]+=1
#hist
plt.bar(range(256),arr)
plt.show()
plt.hist(img.ravel(),256,[0,256])
plt.show()



pmfl = np.zeros(256)



for i in range(256):
	pmfl[i] = arr[i]/res



cdfl = np.zeros(256)  

cdfl[0] = pmfl[0]
for i in range(1,256):
    cdfl[i] = (cdfl[i-1] + pmfl[i])


for i in range(1,256):
    cdfl[i] = cdfl[i] * 255
#plt.show()
for i in range(m):
    for j in range(n):
        g=img[i][j]
        imgnew[i][j]=cdfl[g]

plt.bar(range(256),cdfl)
plt.show()
cv2.imshow("new",imgnew)
cv2.waitKey(0)

'''pixel diff'''

imgnew1=np.zeros([m,n],np.uint8)
#using in built function 
imgnew1=cv2.equalizeHist(img)


cv2.imshow("inbuilthist",imgnew1)
cv2.waitKey(0)


print(error_rms(img,imgnew1))

''''histogram of final output image'''

arr2=np.zeros(256)

mm,nn=imgnew.shape
for i in range(mm):
    for j in range(nn):
        p=imgnew[i][j]
        arr2[p]+=1

plt.bar(range(256),arr2)
plt.show
        








