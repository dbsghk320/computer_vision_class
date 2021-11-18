import cv2
import numpy as np


title = "Mouse event"
image = np.full((500, 500, 3), 255, dtype=np.uint8)
cv2.imshow(title, image)


colors = {
    'black' : (0,0,0),
    'red' : (0, 0, 255),
    'blue' : (255, 0, 0),
    'greem' : (0, 255, 0)
}


def onMouse(event, x, y, flags, param):
    print(event, x, y, flags, param)

    color = colors['black']

    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_CTRLKEY:
            color = colors['red']
        elif flags & cv2.EVENT_FLAG_ALTKEY:
            color = colors['blue']

        cv2.circle(image, (x,y), 30, color, -1)
        cv2.imshow(title, image)


cv2.setMouseCallback(title, onMouse)


while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break


cv2.destroyAllWindows()