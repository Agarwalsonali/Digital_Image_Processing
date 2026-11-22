import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("9_black_and_white.jpg", cv2.IMREAD_GRAYSCALE)

bw_img = np.zeros_like(img)

for i in range(len(img)):
    for j in range(len(img[0])):
        if(img[i][j] > 128):
            bw_img[i][j] = 255
        else:
            bw_img[i][j] = 0

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

plt.subplot(1, 2, 2)
plt.imshow(bw_img, cmap="gray", vmin=0, vmax=255)

plt.show()