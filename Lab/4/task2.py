import cv2
import numpy as np
 

def not_function(val):
    if val == 0:
        return 255
    elif(val ==255):
        return 0
 
 
#reading the images using cv2
image1 = cv2.imread("lab4_square1.jpg")
image2 = cv2.imread("lab4_square2.jpg")

#check if the size of the two images are same 
height1, width1 = image1.shape[:2]
height2, width2 = image2.shape[:2]


if(width1 == width2):
    print("same size")
  

#converting to grayscale
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


# Apply a threshold to create a binary (monochrome) image
_, image1 = cv2.threshold(image1, 150, 255, cv2.THRESH_BINARY)
_, image2 = cv2.threshold(image2, 150, 255, cv2.THRESH_BINARY)





#creating two opencv objects
octagon = np.zeros((height1, width1), dtype=np.uint8)
star = np.zeros((height1, width1), dtype=np.uint8)





for x in range(height1):
    for y in range(width1):
        #pixel of image 1
        pixel_1 = image1[x,y]
        pixel_2 = image2[x,y]
        
        #function for the octagon 
        octagon[x,y]= not_function(pixel_1) & pixel_2
        star[x,y] = not_function(pixel_1) | pixel_2
     
       

# Display the filtered image
cv2.imshow("octagon", octagon)
cv2.imshow("star",star)
# Wait for a key press and close the window

cv2.imwrite("octagon.png",octagon)
cv2.imwrite("star.png",star)

cv2.waitKey(0)
cv2.destroyAllWindows()
