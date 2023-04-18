import cv2
import numpy as np

# Load image
img = cv2.imread("tas.jpg")

# Convert to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Calculate mean value of V channel
v_mean = np.mean(img_hsv[:,:,2])

# Print mean value
print("Mean value of V channel: ", v_mean)