import cv2
import numpy as np
import math

def error_rms(img1,img2):
    m,n = img1.shape
    total = m*n
    sum=0
    #rms error
    for i in range(m):
        for j in range(n):
            sum+=(img1[i][j]-img2[i][j])*(img1[i][j]-img2[i][j])

    error_generated = math.sqrt(sum/total)
    return error_generated

img = cv2.imread('C:\\Users\\Akash\\Desktop\\1508.png',0)
cv2.imshow("real",img)
m, n= img.shape

img1 = np.zeros([m-3+1,n-3+1,1], np.uint8)


#filter = [[1,0,-1],[0,0,0],[-1,0,1]]
#filter = [[1,1,0],[1,-4,1],[0,1,0]]        # 3 filters for edge detection
#filter = [[-1,-2,-1],[0,0,0],[1,2,1]]
#filter = [[1,1,1],[0,0,0],[-1,-1,-1]] #Horizontal edge detection
#filter = [[-1,0,1],[-1,0,1],[-1,0,1]] # VErtical edge detection
filter = [[-1,-2,-1],[0,0,0],[1,2,1]]  # sobel horizontel gradient
#filter = [[-1,0,1],[-2,0,+2],[-1,0,+1]]#sobe vertical gradient

sum=0
for i in range(m-3+1):
    for j in range(n-3+1):
        for a in range(3):
            for b in range(3):
                sum += img[i+a][j+b] * filter[a][b]
        img1[i][j] = sum
        sum=0


cv2.imshow("edges image",img1)
k=cv2.waitKey(0)

    
    
'''sobel using in built'''
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)  # x
#sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)  # y
cv2.imshow("sobely",sobelx) #x
#cv2.imshow("sobely",sobely) # y
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
print(error_rms(img1,sobelx))








