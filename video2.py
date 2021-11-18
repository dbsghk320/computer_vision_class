import cv2
import numpy as np

cap = cv2.VideoCapture('./images/cctv.mp4')
thresh = 50
max_diff = 5
a = None
b = None
c = None

if cap.isOpened():
    ret, a = cap.read()
    ret, b = cap.read()
    while ret:
        ret, c = cap.read()
        frame = c.copy()

    
        #컬러 사진을 비교할 이유가 없음.
        gray_a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        gray_c = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

        #마이너스 값이 나오지 않도록 절대값 처리
        diff1 = cv2.absdiff(gray_a, gray_b)
        diff2 = cv2.absdiff(gray_b, gray_c)
        
        ret, diff1_thresh = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
        ret, diff2_thresh = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)

        diff = cv2.bitwise_and(diff1_thresh, diff2_thresh)
        diff_cnt = cv2.countNonZero(diff)

        if diff_cnt > max_diff:
            non_zero = np.nonzero(diff)
            x1 = min(non_zero[1])
            y1 = min(non_zero[0])
            x2 = max(non_zero[1])
            y2 = max(non_zero[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        stacked = np.hstack((frame, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
        cv2.imshow('cctv', stacked)

        a = b
        b = c
        
        if cv2.waitKey(1) & 0xFF == 27:
            break      
else:
    print("Can't open video")

cap.release()
cv2.destroyAllWindows()