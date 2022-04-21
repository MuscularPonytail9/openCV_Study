import cv2

bgImg = cv2.imread("images/ssu.jpg")
logo = cv2.imread("images/ssu_logo1.jpg")
logo2 = cv2.imread("images/ssu_logo2.jpg")
if bgImg is None or logo is None or logo2 is None: raise Exception("err")

logo[0:87,220:700] = logo2
masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

bg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
bg_pass_mask = cv2.bitwise_or(masks[2], bg_pass_mask)
fg_pass_mask = cv2.bitwise_not(bg_pass_mask)
(H, W), (h, w) = bgImg.shape[:2], logo.shape[:2]
x, y = (W-w)//2, 100
roi = bgImg[y:y+h, x:x+w]

fg = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
bg = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

dst = cv2.add(bg, fg)
bgImg[y:y+h, x:x+w] = dst


cv2.imshow("logo", logo)
cv2.imshow("fgmask", fg_pass_mask)
cv2.imshow("bgmask", bg_pass_mask)
cv2.imshow("fg", fg)
cv2.imshow("bg", bg)
cv2.imshow("dst", dst)
cv2.imshow("bgImg", bgImg)
cv2.waitKey(0)