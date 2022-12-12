import cv2
import numpy as np


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def preprocess(img):
    height = img.shape[0]
    width = img.shape[1]
    roi_vertices = [(0, height), (5 * width / 10, 6 * height / 10), (width, height)]
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray, 100, 150)
    cropped = roi(canny, np.array([roi_vertices], np.int32))
    return cropped


def draw_hough_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 0, 255), thickness=10)
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


vid = cv2.VideoCapture('cut.mp4')
ramka = 0
while True:
    ret, frame = vid.read()
    if frame is None:
        break
    cropped = preprocess(frame)
    lines = cv2.HoughLinesP(cropped, rho=6, threshold=60, theta=np.pi / 180, minLineLength=50, maxLineGap=150,
                            lines=np.array([]))
    img = draw_hough_lines(frame, lines)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "DAMIAN SCHRODER", (1600, 1040), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.imshow('Detekcja linii', img)
    ramka += 1
    if cv2.waitKey(1) & 0xFF == 27:
        break

print ("Liczba ramek:", ramka)
vid.release()
cv2.destroyAllWindows()
