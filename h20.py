import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("image1.jpg", 0)

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Apply Laplacian
lap = cv2.Laplacian(img, cv2.CV_64F)

# Convert output to 8-bit image
lap = cv2.convertScaleAbs(lap)

# Display original and Laplacian images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(lap, cmap="gray")
plt.title("Laplacian Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("laplacian_result.jpg", lap)

print("Laplacian Edge Detection successful!")
print("Output saved as laplacian_result.jpg")