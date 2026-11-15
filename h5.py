import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image1.jpg")

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Perform Bitwise NOT
result = cv2.bitwise_not(img)

# Convert BGR to RGB
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Display image
plt.imshow(result_rgb)
plt.title("Bitwise NOT")
plt.axis("off")
plt.show()

# Save output
cv2.imwrite("not_result.jpg", result)

print("Bitwise NOT operation successful!")
print("Output saved as not_result.jpg")