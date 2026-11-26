import cv2
import numpy as np

img = cv2.imread("input.jpg")
if img is None:
    raise FileNotFoundError("Put a valid 'input.jpg' in your working directory.")

h, w = img.shape[:2]

# 1. Initialize GrabCut structures
mask = np.zeros((h, w), dtype=np.uint8)
bgd_model = np.zeros((1, 65), dtype=np.float64)
fgd_model = np.zeros((1, 65), dtype=np.float64)

# Rough bounding box (x, y, width, height) assuming the subject is roughly centered
rect = (int(w * 0.1), int(h * 0.1), int(w * 0.8), int(h * 0.8))

# 2. Separate foreground and background via GrabCut
cv2.grabCut(img, mask, rect, bgd_model, fgd_model, iterCount=5, mode=cv2.GC_INIT_WITH_RECT)

# 3. Build foreground mask (1 & 3 = foreground, 0 & 2 = background)
fg_mask = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 1.0, 0.0).astype(np.float32)

# 4. Feather the mask edges to avoid jagged MS-Paint cutouts
fg_mask = cv2.GaussianBlur(fg_mask, (7, 7), 0)[:, :, None]

# 5. Blur the entire image and alpha-blend foreground over blurred background
blurred_bg = cv2.GaussianBlur(img, (35, 35), 0)
output = (img * fg_mask + blurred_bg * (1.0 - fg_mask)).astype(np.uint8)

cv2.imshow("Blurred Background", output)
cv2.waitKey(0)
cv2.destroyAllWindows() 