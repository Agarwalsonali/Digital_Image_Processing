import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("8_smoothing_filter.jpg", cv2.IMREAD_GRAYSCALE)

n = len(img)
m = len(img[0])
f = 5

smooth_img = np.zeros_like(img)

for i in range(n):
    for j in range(m):

        x = i - (f - 1)//2
        y = j - (f - 1)//2

        _sum = 0
        for p in range(f):
            x_r = x + p
            for q in range(f):
                y_r = y + q

                if((x_r >= 0 and x_r < n) and (y_r >= 0 and y_r < m)):
                    _sum += int(img[x_r][y_r])
        

        _sum /= (f * f)
        smooth_img[i][j] = _sum

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

plt.subplot(1, 2, 2)
plt.imshow(smooth_img, cmap="gray", vmin=0, vmax=255)

plt.show()