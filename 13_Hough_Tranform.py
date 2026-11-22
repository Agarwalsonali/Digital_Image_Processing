import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("13_Hough_Transform.png", 0)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

edges = cv2.Canny(img, 30, 100)
lines = cv2.HoughLinesP(edges,
                        rho=1,
                        theta=np.pi/180,
                        threshold=20,   
                        minLineLength=30,    
                        maxLineGap=10) 

# print(edges)
# print(lines)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
else:
    print("No lines were detected!")



plt.subplot(1, 2, 2)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.show()