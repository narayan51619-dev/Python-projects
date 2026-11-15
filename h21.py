import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("image1.jpg", 0)

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Apply Canny Edge Detection
edges = cv2.Canny(img, 100, 200)

# Display original and edge-detected images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap="gray")
plt.title("Canny Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("canny_result.jpg", edges)

print("Canny Edge Detection successful!")
print("Output saved as canny_result.jpg")