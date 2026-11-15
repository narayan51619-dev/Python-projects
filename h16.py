import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("image1.jpg", 0)

if img is None:
    print("Image not found. Check the file name.")
    exit()

# Apply 2D FFT
f = np.fft.fft2(img)

# Shift zero frequency to the centre
fshift = np.fft.fftshift(f)

# Calculate magnitude spectrum
magnitude = 20 * np.log(np.abs(fshift) + 1)

# Display magnitude spectrum
plt.imshow(magnitude, cmap="gray")
plt.title("FFT Magnitude Spectrum")
plt.axis("off")
plt.show()

# Save output
plt.imsave("fft_magnitude.png", magnitude, cmap="gray")

print("FFT operation successful!")
print("Output saved as fft_magnitude.png")