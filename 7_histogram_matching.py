import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import ceil, log2
from sortedcontainers import SortedDict
from bisect import bisect_left

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


def get_target_pixel_mapping(img):
    
    N = len(img) * len(img[0])

    _max = int(img.max())
    k = ceil(log2(_max + 1))
    L = int(2 ** k)

    occr_dict = dict()
    i = 0
    while(i < 50):
        occr_dict[i] = 0
        i += 1

    i = 50
    while(i < 255):
        occr_dict[i] = N//206
        i += 1
    
    occr_dict[255] = N - 206 * (N // 206)

    for px, f in occr_dict.items():
        occr_dict[px] = f/N
    
    _sum = 0    
    mapping_dict = dict()

    for px, pr in occr_dict.items():
        _sum += pr
        mapping_dict[px] = round(_sum * (L - 1))
    
    return mapping_dict
    
    
img = cv2.imread("7_histogram_matching.jpg", cv2.IMREAD_GRAYSCALE)

eq = get_pixel_mapping(img)
target_eq = get_target_pixel_mapping(img)

marked = []
for px, m in target_eq.items():
    if(m == 0):
        marked.append(px)

for px in marked:
    target_eq.pop(px)

target_pixel = list(target_eq.keys())
target_mapping = list(target_eq.values())

mapping_dict = dict()

for px, m in eq.items():

    if(m in target_mapping):
        i = target_mapping.index(m)
        mapping_dict[px] = target_pixel[i]
    
    else:
        i = bisect_left(target_mapping, m)
        
        if(i == 0):
            mapping_dict[px] = target_pixel[i]
        
        elif(i == len(target_pixel)):
            mapping_dict[px] = target_pixel[i - 1]
        
        else:
            d1 = m - target_mapping[i - 1]
            d2 = m - target_mapping[i]

            if(d1 <= d2):
                mapping_dict[px] = target_pixel[i - 1]
            else:
                mapping_dict[px] = target_pixel[i]

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
