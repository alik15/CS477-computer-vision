import cv2
import numpy as np

robot_image = cv2.imread("lab3_robot_green_bg.bmp")
height, width = robot_image.shape[:2]


# Define the lower and upper green thresholds 
lower_green = np.array([0, 100, 0], dtype=np.uint8)  # Lower limit for green
upper_green = np.array([50, 255, 50], dtype=np.uint8)  # Upper limit for green


green_mask = cv2.inRange(robot_image, lower_green, upper_green)



list1 = list()

for y in range(height):
    for x in range(width):
        # Get the pixel value at (x, y)
        
        #check the range of green pixels
        if tuple(robot_image[y, x, :]) not in list1:
            list1.append(tuple(robot_image[y,x,:]))
        
        if green_mask[y, x] == 255:
            robot_image[y, x, :] = (0,0,255)
        
cv2.imshow("image", robot_image)
cv2.waitKey(0)
cv2.destroyAllWindows()