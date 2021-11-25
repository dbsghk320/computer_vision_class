import cv2
import numpy as np


img = cv2.imread('./images/taekwonv1.jpg')
rows, cols = img.shape[:2]
img_draw = img.copy()

marker = np.zeros((rows, cols), np.int32)
marker_id = 1
colors = []
is_dragging = False


def on_mouse(event, x, y, flags, param):
    global img_draw, marker, marker_id, is_dragging

    if event == cv2.EVENT_LBUTTONDOWN:
        is_dragging = True
        colors.append((marker_id, img[y, x]))
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_dragging:
            marker[y, x] = marker_id
            cv2.circle(img_draw, (x, y), 3, (0, 0, 255), -1)
            cv2.imshow('watershed', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if is_dragging:
            is_dragging = False
            marker_id += 1
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.watershed(img, marker)
        img_draw[marker == -1] = (0,255,0)
        for mid, color in colors:
            img_draw[marker == mid] = color
        cv2.imshow('watershed', img_draw)


cv2.imshow('watershed', img)
cv2.setMouseCallback('watershed', on_mouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
