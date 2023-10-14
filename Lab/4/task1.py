
import cv2
import numpy
  
# read image
src = cv2.imread('lab4_house.jpg', cv2.IMREAD_UNCHANGED)
 
# apply guassian blur on src image
dst = cv2.GaussianBlur(src,(15,15),cv2.BORDER_DEFAULT)
 
# display input and output image
src_edge =  cv2.Canny(src,100,200)
dst_edge = cv2.Canny(dst,100,200)


non_edge_image = numpy.hstack((src,dst))
edge_image = numpy.hstack((src_edge,dst_edge))



cv2.imshow("Gaussian Smoothing",non_edge_image)
cv2.imshow("Edges",edge_image)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image



#applying edge detection

