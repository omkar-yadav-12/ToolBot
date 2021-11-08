import cv2


image= cv2.imread('demo-design.png')

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


edges= cv2.Canny(gray, "D5E8D4", "DAE8FC")

contours, hierarchy= cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

number_of_objects_in_image = len(contours)


print ("The number of objects in this image: ", str(number_of_objects_in_image))
