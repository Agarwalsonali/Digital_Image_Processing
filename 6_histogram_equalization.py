import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import ceil, log2
from sortedcontainers import SortedDict

def get_pixel_mapping(img):

    N = len(img) * len(img[0])

    _max = int(img.max())
    k = ceil(log2(_max + 1))
    L = int(2 ** k)

    occr_dict = SortedDict()
    for i in range(len(img)):
        for j in range(len(img[0])):

            if(img[i][j] not in occr_dict):
                occr_dict[img[i][j]] = 1/N
            else:
                occr_dict[img[i][j]] += 1/N

    _sum = 0    
    mapping_dict = dict()

    for px, pr in occr_dict.items():
        _sum += pr
        mapping_dict[px] = round(_sum * (L - 1)) 

    return mapping_dict

img = cv2.imread("6_histogram_equalization.jpg", cv2.IMREAD_GRAYSCALE)
mapping_dict = get_pixel_mapping(img)

equalized_img = np.zeros_like(img)

for i in range(len(img)):
    for j in range(len(img[0])):
        equalized_img[i][j] = mapping_dict[img[i][j]]

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

plt.subplot(2, 2, 2)
plt.hist(img.ravel(), bins=256, range=[0, 256], color = "purple")

plt.subplot(2, 2, 3)
plt.imshow(equalized_img, cmap="gray", vmin=0, vmax=255)

plt.subplot(2, 2, 4)
plt.hist(equalized_img.ravel(), bins=256, range=[0, 256], color = "purple")

plt.show()