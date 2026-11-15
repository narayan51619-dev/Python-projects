import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image1.jpg")

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Calculate mean pixel values
print("Mean:", cv2.mean(img))

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display image
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()