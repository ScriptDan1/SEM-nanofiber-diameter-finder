import cv2
import matplotlib.pyplot as plt


link = cv2.imread(
    r"C:\Users\danie\Desktop\Python projects\SEM image reader\Image input\WhatsApp Image 2024-02-01 at 13.09.47 (1).jpeg")

marks = False
x1, y1 = (0, 0)
x2, y2 = (0, 0)
resizeFactor = max(link.shape[0], link.shape[1]) / 900
link = cv2.resize(link, (int(link.shape[1] / resizeFactor), int(link.shape[0] / resizeFactor)))
link_copy = link.copy()


def mouse_callback(event, x, y, flags, param):
    global marks, link_copy, x1, y1, x2, y2
    if event == cv2.EVENT_LBUTTONDOWN:
        if marks is not True:
            link_copy = link.copy()
            cv2.circle(link_copy, (x, y), 5, (255, 0, 0), -1)
            x1, y1 = (x, y)
            marks = True
        else:
            link_copy = link.copy()
            cv2.rectangle(link_copy, (x1, y1), (x, y), (255, 0, 0), 3)
            x2, y2 = (x, y)
            marks = False


def Legend_selection():
    cv2.namedWindow('Set legend bar')
    cv2.setMouseCallback('Set legend bar', mouse_callback)
    while True:
        cv2.imshow('Set legend bar', link_copy)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break;

    cv2.destroyAllWindows()
    if y2 >= y1:
        return link[y1:y2, x1:x2]
    else:
        return link[y2:y1, x2:x1]
