import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("image1.jpg", 0)

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Apply FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Get image dimensions
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

# Create mask
mask = np.zeros((rows, cols), np.uint8)

# Create Low Pass Filter mask
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# Apply Low Pass and High Pass filters
low = fshift * mask
high = fshift * (1 - mask)

# Calculate magnitude spectrum
low_magnitude = np.log(np.abs(low) + 1)
high_magnitude = np.log(np.abs(high) + 1)

# Display results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(low_magnitude, cmap="gray")
plt.title("Low Pass Filter")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(high_magnitude, cmap="gray")
plt.title("High Pass Filter")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save outputs
plt.imsave("low_frequency.png", low_magnitude, cmap="gray")
plt.imsave("high_frequency.png", high_magnitude, cmap="gray")

print("Frequency filtering successful!")
print("Outputs saved successfully!")