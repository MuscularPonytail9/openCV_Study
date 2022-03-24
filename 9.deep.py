import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.ellipse(image, (145, 120), (75, 50), 0, 0, 360, (0, 165, 255), 3)
        cv2.imshow(title, image)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.ellipse(image, (345, 120), (75, 50), 0, 0, 360, (0, 165, 255), 3)
        cv2.imshow(title, image)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)
cv2.rectangle(image, (70, 70),(220, 170), (255,0,0))
cv2.rectangle(image, (270, 70),(420, 170), (255,0,0))
title = "Deep1"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)