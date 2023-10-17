import cv2
import numpy as np

# Load the image (update the file path)
shapes = cv2.imread("path_to_lab4_shapes.bmp")

# Convert the image to HSV
shapes_hsv = cv2.cvtColor(shapes, cv2.COLOR_BGR2HSV)

# Define color range thresholds for each shape
rectangle = cv2.inRange(shapes_hsv, np.array([150, 50, 50]), np.array([179, 255, 255]))
circle = cv2.inRange(shapes_hsv, np.array([100, 50, 50]), np.array([120, 255, 255]))
octagon = cv2.inRange(shapes_hsv, np.array([90, 50, 50]), np.array([100, 255, 255]))
triangle = cv2.inRange(shapes_hsv, np.array([30, 50, 50]), np.array([70, 255, 255]))

# Display the results (use cv2.imshow instead of cv2_imshow)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle", circle)
cv2.imshow("Octagon", octagon)
cv2.imshow("Triangle", triangle)

# Combine all the shapes
all_shapes = rectangle + circle + octagon + triangle

# Display the combined shapes
cv2.imshow("All Shapes", all_shapes)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
