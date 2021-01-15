import cv2
import numpy as np

# Read First Image
img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')
img3 = cv2.imread('3.png')
img4 = cv2.imread('4.png')
img5 = cv2.imread('5.png')
img6 = cv2.imread('6.png')
img7 = cv2.imread('7.png')
img8 = cv2.imread('8.png')

# concatanate image Horizontally
Hori = np.concatenate((img1, img2,i), axis=0)

# concatanate image Vertically
#Verti = np.concatenate((img1, img2), axis=0)

cv2.imshow('Predication', Hori)
#cv2.imshow('VERTICAL', Verti)

cv2.waitKey(0)
cv2.destroyAllWindows()