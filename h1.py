import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

if img1 is None or img2 is None:
    print("Image not found. Check the file names.")
    exit()

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

result = cv2.subtract(img1, img2)

# Convert BGR to RGB for Matplotlib
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

plt.imshow(result)
plt.title("Image Subtraction")
plt.axis("off")
plt.show()

print("hello")
cv2.imwrite("subtraction.jpg", result)
print("Image subtraction successful!")