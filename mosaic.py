import cv2

rate = 15
win_name = 'mosaic'
src = cv2.imread('./images/cat-01.jpg')


while True:
    x, y, w, h = cv2.selectROI(win_name, src, False)
    if w and h:
        roi = src[y:y+h, x:x+w]
        roi = cv2.resize(roi, (w//rate, h//rate))
        roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)

        src[y:y+h,x:x+w] = roi
        cv2.imshow(win_name, src)
    else:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()