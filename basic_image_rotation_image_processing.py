#FILE NAME: basic_image_rotation_image_processing
#CREATOR: Zachary Petrogeorge
#LAST UPDATED; 8/12/2025

# Import OpenCV, numpy, and matplotlib.pyplot for
# Open CV includes image processing libraries
# Numpy inlcludes numerical operations
# matplotlib.pyplot for visualization

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('input.jpeg')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)
angle = 180
scale = 1
# cv2.getRotationMatrix2D generates the transformation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
# cv2.warpAffine applies the rotation from the rotation matrix
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (img.shape[1], img.shape[0]))

fig, axs = plt.subplots(1, 2, figsize=(7,4))
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(rotated_image)
axs[1].set_title('Image Rotation')
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()

# Press 0 to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()