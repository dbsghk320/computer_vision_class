import cv2


cap = cv2.VideoCapture('./images/walking.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

fgbg = cv2.createBackgroundSubtractorMOG2()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    # 배경이 있는 영상에서 움직임이 있는 부분만 빼면됨. 그게 배경
    # 배경에서 객체들을 없앤뒤, 객체를 빼기 더하기 하다보면 마스크
    # min max location으로 객체들을 머시기하면 사람들 머시기
    # cv2.imshow('frame', fgmask)
    # cv2.imshow('bg', fgbg.getBackgroundImage())
    cv2.imshow('frame', frame)
    cv2.imshow('bg', fgmask)
    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
