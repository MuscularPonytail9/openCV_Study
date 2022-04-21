import cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("err")
if image.ndim != 3: raise Exception("err")

bgr = cv2.split(image)

print("bgr 자료형", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소개수: ", len(bgr))

cv2.imshow("image", image)
cv2.imshow("blue channel", bgr[0])
cv2.imshow("green channel", bgr[1])
cv2.imshow("red channel", bgr[2])

cv2.waitKey()