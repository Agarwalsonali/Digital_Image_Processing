import cv2
import numpy as np

# 1. Create a synthetic binary image with disconnected strokes for 'I' and 'A'
img = np.zeros((200, 350), dtype=np.uint8)

# Disconnected 'I' (top bar, vertical stem, bottom bar with gaps)
cv2.line(img, (40, 40), (100, 40), 255, 4)
cv2.line(img, (70, 52), (70, 148), 255, 4)
cv2.line(img, (40, 160), (100, 160), 255, 4)

# Disconnected 'A' (left slant, right slant, crossbar with gaps)
cv2.line(img, (215, 50), (170, 160), 255, 4)
cv2.line(img, (225, 50), (270, 160), 255, 4)
cv2.line(img, (195, 115), (245, 115), 255, 4)

# 2. Link nearby strokes using Morphological Closing
# Kernel size MUST be larger than the intra-letter gap, but smaller than the inter-letter gap.
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
linked = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 3. Group linked strokes via Connected Components
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(linked, connectivity=8)

# 4. Visualize detected letters
output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
for i in range(1, num_labels):  # Skip label 0 (background)
    x, y, w, h, area = stats[i]
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(output, f"Letter {i}", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow("Original (Disconnected)", img)
cv2.imshow("Linked Mask", linked)
cv2.imshow("Grouped Letters", output)
cv2.waitKey(0)
cv2.destroyAllWindows()