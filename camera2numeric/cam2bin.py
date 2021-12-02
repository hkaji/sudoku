#
# camera画像を単純な閾値処理で2値化する
# 
import numpy as np
import cv2
from matplotlib import pyplot as plt

# define a video capture object
vid = cv2.VideoCapture(0)

# Capture a video frame
ret, frame = vid.read()
# Display the resulting frame
print("starting camera...")
cv2.imshow('frame', frame)
if not ret:
	print("failed to grab frame")
	exit()
else:
	print("capturing image...")
	cv2.imwrite("puzzle.png",frame)

vid.release()

# Read image **読み込み画像は必ずグレー画像
print("reading image")
img = cv2.imread('puzzle.png',cv2.IMREAD_GRAYSCALE)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.savefig("bin_all.png")
plt.show()
