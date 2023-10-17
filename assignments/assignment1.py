import cv2
import numpy as np




def box_kernel(image, kernel_size = 7):

    image = cv2.imread(image)
    
    kernel_value = 1 / (kernel_size * kernel_size)

    kernel = np.full((kernel_size, kernel_size), kernel_value, dtype=np.float32)
    kernel_output = cv2.filter2D(image, -1, kernel)
    cv2.imshow("image",kernel_output)


def gaussian_func(image, kernel_size = 3):
    
    sigma = 0
    kernel = np.zeros(kernel_size)
    
    gaussian_function_output = cv2.filter2d(image, -1, kernel)
    
    cv2.imshow("gaussian filtering", gaussian_function_output)
    
    

def median(image,kernel_size):
    height, width = image.shape[:2]
    kernel = np.zeros(kernel_size)
    
    
    for y in range(height):
        for x in range(width):
            
            #image[y,x] = np.median(kernel) 

    pass


def sobel(image, kernel_size):
    pass

def perwitt(image, kernel_size):
    pass


def grayscale(image, kernel_size):
    pass

def binary(image, kernel_size):
    pass


box_kernel("walle.jpg")







cv2.waitKey(0)
cv2.destroyAllWindows()
