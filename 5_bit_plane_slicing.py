import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("5_bit_plane_slicing.jpg", cv2.IMREAD_GRAYSCALE)

p1 = np.zeros_like(img)
p2 = np.zeros_like(img)
p3 = np.zeros_like(img)
p4 = np.zeros_like(img)
p5 = np.zeros_like(img)
p6 = np.zeros_like(img)
p7 = np.zeros_like(img)
p8 = np.zeros_like(img)


for i in range(len(img)):
    for j in range(len(img[0])):

        px = img[i][j]

        p1[i][j] = px & 1
        p2[i][j] = px & 2
        p3[i][j] = px & 4
        p4[i][j] = px & 8
        p5[i][j] = px & 16
        p6[i][j] = px & 32
        p7[i][j] = px & 64
        p8[i][j] = px & 128

r1 = np.zeros_like(img)
r2 = np.zeros_like(img)
r3 = np.zeros_like(img)

for i in range(len(img)):
    for j in range(len(img[0])):
        r1[i][j] = p8[i][j] | p7[i][j]
        r2[i][j] = p8[i][j] | p7[i][j] | p6[i][j]
        r3[i][j] = p8[i][j] | p7[i][j] | p6[i][j] | p5[i][j]
        

plt.subplot(2, 4, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")

plt.subplot(2, 4, 2)
plt.imshow(p8, cmap="gray", vmin=0, vmax=255)
plt.title("Bit Plane 8")

plt.subplot(2, 4, 3)
plt.imshow(p7, cmap="gray", vmin=0, vmax=255)
plt.title("Bit Plane 7")

plt.subplot(2, 4, 4)
plt.imshow(p6, cmap="gray", vmin=0, vmax=255)
plt.title("Bit Plane 6")

plt.subplot(2, 4, 5)
plt.imshow(p5, cmap="gray", vmin=0, vmax=255)
plt.title("Bit Plane 5")

plt.subplot(2, 4, 6)
plt.imshow(r1, cmap="gray", vmin=0, vmax=255)
plt.title("Reconstruction (p8, p7)")

plt.subplot(2, 4, 7)
plt.imshow(r2, cmap="gray", vmin=0, vmax=255)
plt.title("Reconstruction (p8, p7, p6)")

plt.subplot(2, 4, 8)
plt.imshow(r3, cmap="gray", vmin=0, vmax=255)
plt.title("Reconstruction (p8, p7, p6, p5)")

plt.show()