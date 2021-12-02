import cv2
import numpy as np


img = cv2.imread('./images/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detector = cv2.GFTTDetector_create()
# Blob : 큰 파일을 옮길때 시간이 오래 걸림
# 바이너리로 표현된 단위. 청크로 파일을 쪼갤 수 있음
# 100메가를 10개의 구간으로 나눠서 전송
# 10개로 모두 받으면 하나로 합쳐줌
# Blob detector : 구역을 군데군데 나눠서 해당 구역에서 특징을 찾음
# detector = cv2.SimpleBlobDetector_create()
# 이러한 특징을 이용해서 머신러닝을 사용해서 학습.
# 현재로써는 잘 쓰이지 않음. 과거에는 이렇게씀. 성능 괜찮.
detector = cv2.SIFT_create()
keypoints = detector.detect(gray, None)
img_draw = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow('GFTT', img_draw)
cv2.waitKey()
cv2.destroyAllWindows()
