import cv2


import numpy as np
shapes = cv2.imread("lab4_shapes.bmp")
# cv2_imshow(shapes)
shapes_hsv = cv2.cvtColor(shapes,cv2.COLOR_BGR2HSV)

# cv2_imshow(shapes_hsv)
rectangle = cv2.inRange(shapes_hsv, np.array([150,50,50]), np.array([179,255,255]))
circle = cv2.inRange(shapes_hsv, np.array([100,50,50]),np.array([120,255,255]))
octagon = cv2.inRange(shapes_hsv, np.array([90,50,50]), np.array([100,255,255]))
triangle = cv2.inRange(shapes_hsv, np.array([30,50,50]), np.array([70,255,255])) 


new_image = rectangle + circle + octagon + triangle


cv2.imshow("new", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
