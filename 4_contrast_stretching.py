import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("4_contrast_stretching.jpg", cv2.IMREAD_GRAYSCALE)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

plt.subplot(2, 2, 2)
plt.hist(img.ravel(), bins=256, range=[0, 256], color = "purple")


x1 = 0
x2 = 30
y1 = 0
y2 = 150

for i in range(len(img)):
    for j in range(len(img[0])):

        if(img[i][j] >= x1 and img[i][j] <= x2):
            img[i][j] = (((y2 - y1)/(x2 - x1)) * (img[i][j] - x1)) + y1

plt.subplot(2, 2, 3)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

plt.subplot(2, 2, 4)
plt.hist(img.ravel(), bins=256, range=[0, 256], color="purple")
plt.show()
