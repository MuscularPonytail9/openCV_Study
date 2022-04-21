import cv2
import numpy as np

image1 = np.zeros((300, 300), np.uint8)
image2 = image1.copy()

h, w = image1.shape[:2]
cx, cy = w // 2, h // 2
cv2.circle(image1, (cx, cy), 100, 255, -1)
cv2.rectangle(image2, (0, 0, cx, h), 255, -1)

image3 = cv2.bitwise_or(image1, image2)
image4 = cv2.bitwise_and(image1, image2)
image5 = cv2.bitwise_xor(image1, image2)
image6 = cv2.bitwise_not(image1)

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("or", image3)
cv2.imshow("and", image4)
cv2.imshow("xor", image5)
cv2.imshow("not", image6)

cv2.waitKey(0)