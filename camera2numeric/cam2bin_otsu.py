#
# camera画像を大津の2値化する
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

# Read image
print("reading image")
img = cv2.imread('puzzle.png',cv2.IMREAD_GRAYSCALE)

# 単純閾値
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#　大津処理
ret, th_ot = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

titles = ['Original Image', 'Global Thresholding (v = 127)','Otsu Image']
images = [img, th1, th_ot]

for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.savefig("bin_otsu_all.png")
plt.show()
