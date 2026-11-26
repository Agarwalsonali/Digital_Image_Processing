import cv2
import numpy as np

img = cv2.imread("image.jpg")
if img is None:
    raise FileNotFoundError("Put a valid 'input.jpg' in your working directory.")

# 1. Convert to grayscale and apply Otsu's automatic thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 2. Convert to float [0, 1] and feather edges for clean blending
fg_mask = (mask.astype(np.float32) / 255.0)
fg_mask = cv2.GaussianBlur(fg_mask, (7, 7), 0)[:, :, None]

# 3. Blur background and alpha-blend
blurred_bg = cv2.GaussianBlur(img, (35, 35), 0)
output = (img * fg_mask + blurred_bg * (1.0 - fg_mask)).astype(np.uint8)

cv2.imshow("Threshold Mask", mask)
cv2.imshow("Blurred Background", output)
cv2.waitKey(0)
cv2.destroyAllWindows()