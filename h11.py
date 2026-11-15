import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("image2.jpg")

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Apply Gaussian Blur
out = cv2.GaussianBlur(img, (5, 5), 0)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
out_rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

# Display original and blurred images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(out_rgb)
plt.title("Gaussian Blurred Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("blurred.jpg", out)

print("Gaussian Blur successful!")
print("Output saved as blurred.jpg")