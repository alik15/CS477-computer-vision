import cv2 
import numpy as np
img = cv2.imread("lab4_persp.jpg")

cv2.imshow("image",img)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image