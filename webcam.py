import cv2
from PIL import ImageColor

imcap = cv2.VideoCapture(0)
imcap.set(3, 640) # set width as 640
imcap.set(4, 480) # set height as 480


# def calculate_gray(hex):
    

def thresh_callback(val):
    threshold = val
    # Detect edges using Canny
    canny_output = cv2.Canny(src_gray, threshold, threshold * 2)
    # Find contours
    x, contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Draw contours
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv2.drawContours(drawing, contours, i, color, 2, cv2.LINE_8, hierarchy, 0)
    # Show in a window
    cv2.imshow('Contours', drawing)

while True:
    success, src = imcap.read() # capture frame from video
    # converting image from color to grayscale 

    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    src_gray = cv2.blur(src_gray, (3,3))
    # Create Window
    source_window = 'Source'
    cv2.namedWindow(source_window)
    cv2.imshow(source_window, src)
    max_thresh = 255
    thresh = 100 # initial threshold
    cv2.createTrackbar('Canny Thresh:', source_window, thresh, max_thresh, thresh_callback)
    thresh_callback(thresh)
    cv2.waitKey()