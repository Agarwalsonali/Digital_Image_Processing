import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import log2, ceil

img = cv2.imread("3_negative.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

# _max = -1
# for i in range(len(img)):
#     for j in range(len(img[0])):
#         if(img[i][j] > _max):
#             _max = img[i][j]   

_max = int(img.max())     
k = ceil(log2(_max + 1))
L = int(2 ** k)

img = L - 1 - img

# for i in range(len(img)):
#     for j in range(len(img[0])):
#         img[i][j] = L - 1 - img[i][j]         

plt.subplot(1, 2, 2)
plt.title("Negative")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.show()
