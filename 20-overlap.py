import cv2
import numpy as np

h, w = 400, 400

# 1. Still use FILLED masks to compute the overlapping region
tri_mask = np.zeros((h, w), dtype=np.uint8)
circ_mask = np.zeros((h, w), dtype=np.uint8)

pts = np.array([[200, 60], [80, 300], [320, 300]], dtype=np.int32)
center, radius = (240, 220), 100

cv2.fillPoly(tri_mask, [pts], 255)
cv2.circle(circ_mask, center, radius, 255, -1)

overlap_mask = cv2.bitwise_and(tri_mask, circ_mask)

# 2. Start with a white canvas and fill the overlap in grey
canvas = np.full((h, w, 3), 255, dtype=np.uint8)
canvas[overlap_mask > 0] = (150, 150, 150)  # Grey

# 3. Draw black outlines on top
cv2.polylines(canvas, [pts], isClosed=True, color=(0, 0, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.circle(canvas, center, radius, color=(0, 0, 0), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow("Overlapping Outlines", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()