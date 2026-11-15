import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("image1.jpg", 0)

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot histogram
plt.plot(hist)

plt.title("Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])
plt.grid()

# Save histogram
plt.savefig("histogram.png")

# Display histogram
plt.show()

print("Histogram generated successfully!")
print("Output saved as histogram.png")