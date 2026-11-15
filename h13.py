import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("image2.jpg")

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Apply Median Blur
out = cv2.medianBlur(img, 3)

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
plt.title("Median Blur (3)")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("median3_result.jpg", out)

print("Median Blur successful!")
print("Output saved as median3_result.jpg")