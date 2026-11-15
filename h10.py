import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("image1.jpg")

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Zoom the image
out = cv2.resize(img, None, fx=3, fy=3)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
out_rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

# Display original and zoomed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(out_rgb)
plt.title("Zoomed Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
cv2.imwrite("zoomed.jpg", out)

print("Image Zooming successful!")
print("Output saved as zoomed.jpg")