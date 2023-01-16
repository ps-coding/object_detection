import cv2
import numpy as np

# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    # mask = cv2.inRange(frame, np.array([0, 160, 225]), np.array([30,255,255]))
    cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frame, np.array([40, 100, 100]), np.array([75,255,255]))
    

    ret,thresh = cv2.threshold(mask, 40, 255, 0)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if len(contours) != 0:
        c = max(contours, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        cv2.rectangle(frame, (x,y), (x + w, y+h), (0, 0, 255), 5)

    for con in contours:
        x, y, w, h = cv2.boundingRect(con)

        if (w * h > 3000):
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


vid.release()
cv2.destroyAllWindows()

