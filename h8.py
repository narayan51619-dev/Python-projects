import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("image1.jpg")

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Define translation matrix
M = np.float32([[1, 0, 20],
                [0, 1, 30]])

# Perform image translation
out = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
out_rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

# Display original and translated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(out_rgb)
plt.title("Translated Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("translated.jpg", out)

print("Image Translation successful!")
print("Output saved as translated.jpg")