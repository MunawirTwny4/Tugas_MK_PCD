import cv2

# Load image
img = cv2.imread("tas.jpg")

# Convert image to HSV format
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Extract Hue, Saturation, and Value channels
hue = hsv_img[:,:,0]
saturation = hsv_img[:,:,1]
value = hsv_img[:,:,2]

# Display extracted channels
cv2.imshow("Hue Channel", hue)
cv2.imshow("Saturation Channel", saturation)
cv2.imshow("Value Channel", value)

# Wait for user to close window
cv2.waitKey(0)

# Clean up resources
cv2.destroyAllWindows()