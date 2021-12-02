import cv2
import numpy as np


img1 = cv2.imread('./images/taekwonv1.jpg')
img2 = cv2.imread('./images/figures.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

detector = cv2.SIFT_create()
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_L1)
matches = matcher.match(desc1, desc2)

res = cv2.drawMatches(
    img1, kp1, img2, kp2, matches, None
)

cv2.imshow('SIFT', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
