import cv2

# Load an image
image = cv2.imread("your_image.jpg")  # Replace with the path to your image

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# You can now work with the `hsv_image` in the HSV color space



cv2.imshow("fds",hsv_image)
# Save the HSV image (if needed)
#cv2.imwrite("hsv_image.jpg", hsv_image)
