import cv2
import numpy as np

# Load image
img = cv2.imread("tas.jpg")

# Convert to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Calculate mode of V channel
v_mode = np.argmax(np.bincount(img_hsv[:,:,2].flatten()))

# Print mode value
print("Mode of V channel: ", v_mode)