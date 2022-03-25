import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt, pt_prev, isMouseClicked, tempImage

    if event == cv2.EVENT_MOUSEMOVE:
        if isMouseClicked == True:
            pt = (x, y)
            mimage = np.full((300, 500, 3), (255, 255, 255), np.uint8)
            cv2.line(mimage, pt_prev, pt, cv2.LINE_AA)
            cv2.imshow(title, mimage)

    if event == cv2.EVENT_LBUTTONDOWN:
        pt_prev = (x, y)
        isMouseClicked = True

    if event == cv2.EVENT_LBUTTONUP:
        isMouseClicked = False
        pt = (x, y)
        cv2.rectangle(image, pt_prev, pt, (255,0,0), 1)
        eCen = (int(np.abs(pt_prev[0] + pt[0])/2), int(np.abs(pt_prev[1] + pt[1])/2))
        eSize = (int(np.sqrt((np.abs(pt_prev[0] - pt[0]) / 2) ** 2 + (np.abs(pt_prev[1] - pt[1]) / 2) ** 2)))
        cv2.ellipse(image, eCen, (eSize, eSize), 0, 45, 225, (0, 165, 255), 2)
        cv2.imshow(title, image)
        pt = (-1, -1)
        pt_prev = (-1, -1)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)
pt = (-1, -1)
isMouseClicked = False
title = "deep3"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)