import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

if img1 is None or img2 is None:
    print("Image not found. Check the file names.")
    exit()

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Perform Bitwise OR
result = cv2.bitwise_or(img1, img2)

# Convert BGR to RGB
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Display image
plt.imshow(result_rgb)
plt.title("Bitwise OR")
plt.axis("off")
plt.show()

# Save output
cv2.imwrite("or_result.jpg", result)

print("Bitwise OR operation successful!")
print("Output saved as or_result.jpg")