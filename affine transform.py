import cv2
import numpy as np

img = cv2.imread('./images/cat-01.jpg')
h, w = img.shape[:2]

pts1 = np.array([
    [100, 50], [200, 50], [100, 200]
], dtype=np.float32)

pts2 = np.array([
    [80, 70], [210, 60], [250, 120]
], dtype=np.float32)

cv2.circle(img, (100, 50), 5, (255,0,0),-1 )
cv2.circle(img, (200, 50), 5, (0,255,0),-1 )
cv2.circle(img, (100, 200), 5, (0,0,255),-1 )

matrix = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, matrix, (int(w*1.5),h))

cv2.imshow('original', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
