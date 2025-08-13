#FILE NAME: basic_edge_detection_image_processing.py
#CREATOR: Zachary Petrogeorge
#LAST UPDATED; 8/12/2025

# Import OpenCV, numpy, and matplotlib.pyplot for
# Open CV includes image processing libraries
# Numpy inlcludes numerical operations
# matplotlib.pyplot for visualization

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('input.jpeg')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.Canny applies non-maximum suppression and hysteresis thresholding to detect edges
image_edges = cv2.Canny(image_rgb, 100, 700)

fig, axs = plt.subplots(1, 2, figsize = (7, 4))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(image_edges)
axs[1].set_title('Image Edges')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()

# Press 0 to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()