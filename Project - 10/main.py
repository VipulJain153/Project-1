import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read() ,cv2.COLOR_BGR2GRAY
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    success, img1 = cap.read()
    # diff = cv2.absdiff(img,img1)

    cv2.imshow('Security Camera', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break