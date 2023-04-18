import cv2
import numpy as np
from scipy.stats import skew

# Load image
img = cv2.imread("tas.jpg")

# Convert to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Calculate skewness of V channel
v_skewness = skew(img_hsv[:,:,2].flatten())

# Print skewness value
print("Skewness of V channel: ", v_skewness)