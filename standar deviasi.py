import cv2
import numpy as np

# Load image
img = cv2.imread("tas.jpg")

# Convert to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Calculate standard deviation of V channel
v_std = np.std(img_hsv[:,:,2])

# Print standard deviation value
print("Standard deviation of V channel: ", v_std)