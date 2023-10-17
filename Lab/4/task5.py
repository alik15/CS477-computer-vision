import cv2 
import numpy as np
img = cv2.imread("lab4_persp.jpg")

height, width = img.shape[:2]

original_image_coords = np.float32([[35,19],[217,547],[281,61],[400,280]])

transform_image_coords = np.float32([[0,0],[0,560],[420,0],[560,420]])


# Calculate the perspective transformation matrix
M = cv2.getPerspectiveTransform(original_image_coords, transform_image_coords)

# Apply the perspective transformation to the image
warped_image = cv2.warpPerspective(img, M, (width, height))


print(height,width)
cv2.imshow("image",warped_image)
cv2.imwrite("saved.jpg",warped_image)


cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image