

b = 0
w = 255

print(b | b)






"""
from PIL import Image, ImageFilter
import cv2


#reading the image using cv2
image = cv2.imread("lab4_square1.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# Apply a threshold to create a binary (monochrome) image
_, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)

# Display the filtered image
cv2.imshow("Filtered Image", image)
# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()



height, width = image.shape[:2]

list1 = list()

for y in range(height):
    for x in range(width):
        # Get the pixel value at (x, y)
        pixel_value = image[y, x]
        
        if pixel_value not in list1:
            list1.append(pixel_value)



























#reading image
image1 = Image.open("lab4_square1.jpg").convert("1")
image2 = Image.open("lab4_square2.jpg").convert("1")


 
#getting pixel data 
pixel_data1 = image1.load()
pixel_data2 = image2.load()
width, height = image1.size

image1 = image1.filter(ImageFilter.MedianFilter(size=3))

#image2 = image2.filter(ImageFilter.MedianFilter(size=5))

image2 = image2.filter(ImageFilter.GaussianBlur(radius=2))

list1 = list()

for y in range(height):
    for x in range(width):
        # Access the pixel at (x, y)
        pixel = pixel_data1[x, y]
        
        if pixel not in list1:
            list1.append(pixel)
        
        
#image2.show()

print(list1)









"""




