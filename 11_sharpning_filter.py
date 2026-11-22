import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("11_sharpning_filter.jpg", cv2.IMREAD_GRAYSCALE)

n = len(img)
m = len(img[0])

sharp_img = np.zeros_like(img, dtype=np.int32)

for i in range(n):
    for j in range(m):

        x = i - 1
        y = j - 1

        _sum = 0
        for p in range(3):
            x_r = x + p
            for q in range(3):
                y_r = y + q

                if((x_r >= 0 and x_r < n) and (y_r >= 0 and y_r < m)):

                    if(p == q == 1):
                        _sum -= int(img[x_r][y_r]) * 8
                    else:
                        _sum += int(img[x_r][y_r])
                        
        sharp_img[i][j] = _sum

sharp_img = np.clip(sharp_img, 0, 255)
sharp_img = sharp_img.astype(np.uint8)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

plt.subplot(1, 2, 2)
plt.imshow(sharp_img, cmap="gray", vmin=0, vmax=255)

plt.show()