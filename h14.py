import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("image1.jpg")

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Create 5x5 averaging kernel
kernel = np.ones((5, 5), np.float32) / 25

# Apply Low Pass Filter
out = cv2.filter2D(img, -1, kernel)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
out_rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

# Display original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(out_rgb)
plt.title("Low Pass Filter")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("lowpass_result.jpg", out)

print("Low Pass Filter successful!")
print("Output saved as lowpass_result.jpg")