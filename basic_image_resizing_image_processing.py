#FILE NAME: basic_image_resizing_image_processing.py
#CREATOR: Zachary Petrogeorge
#LAST UPDATED; 8/12/2025

# Import OpenCV, numpy, and matplotlib.pyplot for
# Open CV includes image processing libraries
# Numpy inlcludes numerical operations
# matplotlib.pyplot for visualization

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('input.jpeg')
# convert from gbr to rgb
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
scale_1 = 4
scale_2 = 1/4

height, width = image_rgb.shape[:2]
new_height1 = int(height * scale_1)
new_width1 = int(width * scale_1)

# Creating a zoomed image
# cv2.resize resizes the image to the specified dimensions
# cv2.INTER_CUBIC provides enlargement of high quality
zoomed_image = cv2.resize(src =image_rgb, dsize=(new_width1, new_height1),interpolation=cv2.INTER_CUBIC)

new_height2 = int(height * scale_2)
new_width2 = int(width * scale_2)
#cv2.INTER_ARE is best for downscaling
scaled_image = cv2.resize(src=image_rgb, dsize=(new_width2, new_height2), interpolation=cv2.INTER_AREA)

fig,axs = plt.subplots(1, 3, figsize=(10,4))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image Shape:'+str(image_rgb.shape))
axs[1].imshow(zoomed_image)
axs[1].set_title('Zoomed Image Shape:'+str(zoomed_image.shape))
axs[2].imshow(scaled_image)
axs[2].set_title('Scaled Image Shape:'+str(scaled_image.shape))

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()

# Press 0 to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()