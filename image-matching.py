import cv2
import numpy as np
import matplotlib.pyplot as plt

method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
img_rgb = cv2.imread('soldier.png')

cv2.imwrite("test.png", img_rgb)

rows,cols,_ = img_rgb.shape

print(rows)
print(cols)


imcap = cv2.VideoCapture(0)
imcap.set(3, 720) # set width as 640
imcap.set(4, 1280) # set height as 480

# load the image
method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv2.imread('soldier.png')

success, large_image = imcap.read() # capture frame from video

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)

# The image is only displayed if we call this
cv2.waitKey(0)