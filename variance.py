import cv2
import numpy as np

# Load image
img = cv2.imread("tas.jpg")

# Convert to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Calculate variance of V channel
v_var = np.var(img_hsv[:,:,2])

# Print variance value
print("Variance of V channel: ", v_var)