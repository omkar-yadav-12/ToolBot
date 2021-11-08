import cv2


def has_image(haystack, needle):
    haystack = cv2.cvtColor(haystack, cv2.COLOR_BGR2GRAY)
    needle = cv2.cvtColor(needle, cv2.COLOR_BGR2GRAY)
    w, h = needle.shape[::-1]
    res = cv2.matchTemplate(haystack, needle, cv2.TM_CCOEFF_NORMED)
    threshold = 0.99
    loc = np.where(res >= threshold)
    try:
        assert loc[0][0] > 0
        assert loc[1][0] > 0
        return (loc[1][0], loc[0][0])
    except:
        return (-1, -1)


fruits = cv2.imread("mixed-fruits.jpg")
strawberry = cv2.imread("strawberry.jpg")

x, y = has_image(fruits, strawberry)

if x >= 0 and y >= 0:
    w, h, _ = strawberry.shape
    cv2.rectangle(fruits, (x, y), (x+h, y+w), (255, 0, 0), 2)
    cv2.imshow("Found the strawberry at (%d,%d)" % (x, y), fruits)
    cv2.waitKey(0xFFFF)