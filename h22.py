import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image1.jpg', 0)

if img is None:
    print("Image not found. Check the file name.")
    exit()

kernel = np.ones((5, 5), np.uint8)

eroded = cv2.erode(img, kernel, iterations=1)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(eroded, cmap='gray')
plt.title('Erosion')
plt.axis('off')

plt.show()

cv2.imwrite('erosion_result.jpg', eroded)
print("Output saved successfully!")