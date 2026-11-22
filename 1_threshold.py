import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import log2, ceil

img = cv2.imread("1_threashold.png", cv2.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1), plt.title("Original")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

print(img.min(), img.max())
_max = int(img.max())
k = ceil(log2(_max + 1))
L = int(2 ** k)

threashold = 130
for i in range(len(img)):
    for j in range(len(img[0])):

        if(img[i][j] > threashold):
            img[i][j] = L - 1
        else:
            img[i][j] = 0

plt.subplot(1, 2, 2), plt.title("Threshold")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.show()
