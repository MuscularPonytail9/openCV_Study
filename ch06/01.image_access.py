import cv2
import numpy as np
import time

def pixel_access1(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i,j]
            image1[i,j] = 255 - pixel
    return image1

def pixel_access2(image):
    image2 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i, j)
            image2.itemset((i, j), 255 - pixel)
    return image2

def pixel_access3(image):
    lut = [255 - i for i in range(256)]
    lut = np.array(lut, np.uint8)
    image3 = lut[image]
    return image3

def pixel_access4(image):
    image4 = cv2.subtract(255, image)
    return image4

def pixel_access5(image):
    image5 = 255 - image
    return image5

image = cv2.imread("images/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("err")

def time_check(func, msg):
    start_time = time.perf_counter()
    ret_img = func(image)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(msg, "time: %.2f ms" % elapsed)
    return ret_img

image1 = time_check(pixel_access1, "직접")
image2 = time_check(pixel_access2, "item()")
image3 = time_check(pixel_access3, "lut")
image4 = time_check(pixel_access4, "opencv method")
image5 = time_check(pixel_access5, "ndarrary")

cv2.imshow("img - original", image)
cv2.imshow("img1", image1)
cv2.imshow("img2", image2)
cv2.imshow("img3", image3)
cv2.imshow("img4", image4)
cv2.imshow("img5", image5)
cv2.waitKey(0)
