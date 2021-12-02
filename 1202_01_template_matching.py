import cv2
import numpy as np


img = cv2.imread('./images/figures.jpg')
template = cv2.imread('./images/taekwonv1.jpg')
# 90도로 회전시키기
template = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)
# np.rot90()
th, tw = template.shape[:2]
cv2.imshow('template', template)

methodes = ['cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_CCOEFF_NORMED']

for i, method_name in enumerate(methodes):
    img_draw = img.copy()
    method = eval(method_name)
    # 차원의 배열, 즉 마스크
    res = cv2.matchTemplate(img, template, method)

    # TM_SQDIFF : 최소값이 좋음?
    # 상관관계 : 1에 가까울수록 좋음

    # 마스크를 기준으로 4가지 값을 내뱉음
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
        top_left = min_loc
        match_val = min_val
    else:
        top_left = max_loc
        match_val = max_val

    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(img_draw, top_left, bottom_right, (0, 0, 255), 2)
    cv2.putText(
        img_draw, str(match_val), top_left,
        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv2.LINE_AA
    )
    cv2.imshow("result", img_draw)

cv2.waitKey(0)
cv2.destroyAllWindows()
