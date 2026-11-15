import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("image1.jpg", 0)

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Apply Sobel X
sx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel Y
sy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert results to displayable format
sx = cv2.convertScaleAbs(sx)
sy = cv2.convertScaleAbs(sy)

# Display original, Sobel X and Sobel Y
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(sx, cmap="gray")
plt.title("Sobel X")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(sy, cmap="gray")
plt.title("Sobel Y")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save outputs
cv2.imwrite("sobel_x.jpg", sx)
cv2.imwrite("sobel_y.jpg", sy)

print("Sobel Edge Detection successful!")
print("Outputs saved as sobel_x.jpg and sobel_y.jpg")