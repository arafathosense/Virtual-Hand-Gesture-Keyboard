import cv2
import numpy as np
import mediapipe as mp
import math

text = ""

# Distance Function
def find_distance(image, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    length = math.hypot(x2 - x1, y2 - y1)

    if image is not None:
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return length, image


# Button Class
class Button:
    def __init__(self, label, pos1, pos2):
        self.label = label
        self.pos1 = pos1
        self.pos2 = pos2

    def draw_rectangle(self, image, color):
        cv2.rectangle(image, self.pos1, self.pos2, color, 3)

    def puttext(self, image, x, y):
        cv2.putText(image, self.label, (x + 10, y + 40),
                    cv2.FONT_HERSHEY_PLAIN, 2, (47, 255, 173), 2)


# Hand Detection Function
def hand_detection(image, Draw, mphands, hands, draw):
    positionx = [0] * 21
    positiony = [0] * 21

    rgbimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgbimage)
    h, w, _ = image.shape

    if Draw:
        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                for index, lm in enumerate(hand.landmark):
                    positionx[index] = int(lm.x * w)
                    positiony[index] = int(lm.y * h)

                draw.draw_landmarks(image, hand, mphands.HAND_CONNECTIONS)

    # Rough area calculation (to prevent accidental presses)
    area = (positionx[9] - positionx[4]) ** 2 * 3.14

    create_buttons(image, positionx, positiony, area)


# Create Virtual Keyboard Buttons
def create_buttons(image, px, py, area):
    global text
    color = (255, 0, 0)

    keys = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
        ["Z", "X", "C", "V", "B", "N", "M"]
    ]

    # Text box
    cv2.rectangle(image, (150, 500), (700, 600), (128, 128, 128), -1)

    y = 100
    count = 0

    for row in keys:
        x = 150
        y += 55

        for key in row:
            btn = Button(key, (x, y), (x + 50, y + 50))
            btn.puttext(image, x, y)

            # Highlight button when finger hover
            if x <= px[8] <= x + 50 and y <= py[8] <= y + 50:
                btn.draw_rectangle(image, (255, 255, 10))

                length, image = find_distance(image,
                                              (px[8], py[8]),
                                              (px[12], py[12]))

                # Key Press Detection
                if area < 4000:
                    if 18 < length < 23:
                        cv2.waitKey(150)
                        text += key
            else:
                btn.draw_rectangle(image, color)

            x += 55
            count += 1

    # -------------------------------------
    # BACKSPACE / DELETE GESTURE
    # -------------------------------------
    delete_length, image = find_distance(image,
                                         (px[8], py[8]),
                                         (px[4], py[4]))  # index–thumb

    if delete_length < 25:  # threshold
        cv2.putText(image, "DEL", (600, 570),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 255), 4)
        cv2.waitKey(150)

        if len(text) > 0:
            text = text[:-1]

    # Display typed text
    cv2.putText(image, text, (160, 570),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 6)


# Main Program
video = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands(static_image_mode=False,
                      min_detection_confidence=0.8,
                      min_tracking_confidence=0.8)
draw = mp.solutions.drawing_utils

while True:
    ret, image = video.read()
    if not ret:
        break

    image = cv2.resize(image, (1000, 700))
    image = cv2.flip(image, 1)

    hand_detection(image, True, mphands, hands, draw)

    cv2.imshow("Virtual Keyboard", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
