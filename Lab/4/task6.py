import cv2
import numpy as np

robot_image = cv2.imread("lab3_robot_green_bg.bmp")
background_image = cv2.imread("lab4_road.jpg")

#reading heights and widths 
height, width = robot_image.shape[:2]
height1, width1 = background_image.shape[:2]

if (height == height1) and (width ==  width1):
    print("images are of the same size")
    
    


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
            
        if green_mask[y, x] != 255:
            background_image[y, x, :] = robot_image[y, x, :]
            
        
cv2.imwrite("robot_image_red_bg.jpg", robot_image)


cv2.imshow("image",background_image)


cv2.waitKey(0)
cv2.destroyAllWindows()