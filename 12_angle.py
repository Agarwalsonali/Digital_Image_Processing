import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import atan, pi

# img = cv2.imread("12_angle.jpg", cv2.IMREAD_GRAYSCALE)

# img = [
#     [0,  0, 10, 10, 10],
#     [0,  0, 10, 10, 10],
#     [0,  0, 10, 10, 10],
#     [0,  0, 10, 10, 10],
#     [0,  0, 10, 10, 10]
# ]

img = [
    [0,  0,  0,  0,  10],
    [0,  0,  0,  10, 10],
    [0,  0,  10, 10, 10],
    [0,  10, 10, 10, 10],
    [10, 10, 10, 10, 10]
]

n = len(img)
m = len(img[0])

Gx = np.zeros_like(img, dtype=np.int32)
Gy = np.zeros_like(img, dtype=np.int32)
angle = np.zeros_like(img, dtype=np.float32)

for i in range(n):
    for j in range(m):

        _sum = 0

        if((i - 1) >= 0 and (j - 1) >= 0):
            _sum += img[i - 1][j - 1] * 1
        if((i - 1) >= 0):
            _sum += img[i - 1][j] * 0
        if((i - 1) >= 0 and (j + 1) < m):
            _sum += img[i - 1][j + 1] * -1
        
        if((j - 1) >= 0):
            _sum += img[i][j - 1] * 2
        _sum += img[i][j] * 0
        if((j + 1) < m):
            _sum += img[i][j + 1] * -2
        
        if((i + 1) < n and (j - 1) >= 0):
            _sum += img[i + 1][j - 1] * 1
        if((i + 1) < n):
            _sum += img[i + 1][j] * 0
        if((i + 1) < n and (j + 1) < m):
            _sum += img[i + 1][j + 1] * -1

        
        Gx[i][j] = _sum
        
        _sum = 0

        if((i - 1) >= 0 and (j - 1) >= 0):
            _sum += img[i - 1][j - 1] * -1
        if((i - 1) >= 0):
            _sum += img[i - 1][j] * -2
        if((i - 1) >= 0 and (j + 1) < m):
            _sum += img[i - 1][j + 1] * -1
        
        if((j - 1) >= 0):
            _sum += img[i][j - 1] * 0
        _sum += img[i][j] * 0
        if((j + 1) < m):
            _sum += img[i][j + 1] * 0
        
        if((i + 1) < n and (j - 1) >= 0):
            _sum += img[i + 1][j - 1] * 1
        if((i + 1) < n):
            _sum += img[i + 1][j] * 2
        if((i + 1) < n and (j + 1) < m):
            _sum += img[i + 1][j + 1] * 1

        
        Gy[i][j] = _sum


for i in range(n):
    for j in range(m):
        if Gx[i][j] != 0:
            angle[i][j] = atan(Gy[i][j] / Gx[i][j]) * (180/pi)
        else:
            angle[i][j] = 90

for i in range(n):
    for j in range(m):
        print(angle[i][j], end = " ")
    print()