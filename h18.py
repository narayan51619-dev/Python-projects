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

# Shift zero frequency to centre
fshift = np.fft.fftshift(f)

# Apply inverse shift
ishift = np.fft.ifftshift(fshift)

# Apply Inverse FFT
img_back = np.fft.ifft2(ishift)

# Get absolute values
img_back = np.abs(img_back)

# Display original and reconstructed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_back, cmap="gray")
plt.title("Reconstructed Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save output
plt.imsave("reconstructed.png", img_back, cmap="gray")

print("Image Reconstruction successful!")
print("Output saved as reconstructed.png")