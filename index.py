import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

if img1 is None or img2 is None:
    print("Image not found")
    exit()

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

result = cv2.add(img1, img2)

cv2.imwrite("addition.jpg", result)

result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

plt.imshow(result_rgb)
plt.axis("off")
plt.show()

print("Program started")

print("Image addition successful!")

print("Output saved as addition.jpg")