#FILE NAME: basic_grayscale_image_processing.py
#CREATOR: Zachary Petrogeorge
#LAST UPDATED; 8/12/2025

# Import OpenCV, numpy, and matplotlib.pyplot for
# Open CV includes image processing libraries
# Numpy inlcludes numerical operations
# matplotlib.pyplot for visualization

import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Load image to be processed
# Loads image into NumPy array
image = cv2.imread('input.jpeg')
# Verify that image loaded correctly
if image is None:
    print("Erro: Could not load image")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# save the converted grayscale image
cv2.imwrite('gray_output.jpeg', gray)

# Apply sepia filter
# First, convert image to 64 bit float for calculations
sepia = np.array(image, dtype=np.float64)
cv2.imshow('sepia', sepia)
# apply the sepia transformation to adjust BGR channels
sepia = cv2.transform(sepia, np.matrix([[0.272, 0.534, 0.131],
                                        [0.349, 0.686, 0.168],
                                        [0.393, 0.769, 0.189]]))
# Clip the values of sepia so pixel values are valid for images
sepia = np.clip(sepia, 0, 255)
# Convert image back to unsigned 8 bit
cv2.imshow('sepia', sepia)
sepia = sepia.astype(np.uint8)
cv2.imshow('sepia', sepia)

# Display image results
# first convert all images to RGB for proper matplot use
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
sepia = cv2.cvtColor(sepia, cv2.COLOR_BGR2RGB)

fig, axs = plt.subplots(1, 3, figsize = (10, 4))
axs[0].imshow(image)
axs[0].set_title('Original Image')
axs[1].imshow(gray)
axs[1].set_title('Gray Scaled Image')
axs[2].imshow(sepia)
axs[2].set_title('Sepia Filter Image')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()

# Press 0 to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()