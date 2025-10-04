import cv2,os
from cvzone.HandTrackingModule import HandDetector
from cvzone import cornerRect
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(5, 80)
cap.set(10, 0)
detector = HandDetector(detectionCon=0.85,maxHands=1)
x,y,w,h,= 200,200,400,400
drag=False
prevCX=0
prevCY=0
segmentor = SelfiSegmentation()
imgBG = cv2.resize(cv2.imread("background.jpg"),(1280,720))
index = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    hands,img = detector.findHands(img,flipType=False)
    imgOut = segmentor.removeBG(img, imgBg=imgBG, threshold=.71)
    if hands:
        lmList= hands[0]['lmList']
        overlay = imgOut.copy()
        alpha = 0.4
        cv2.rectangle(overlay, (x,y,w,h), (255, 0, 255), -1) 
        imgOut = cv2.addWeighted(overlay, alpha,imgOut,1-alpha,0)
        cornerRect(imgOut,(x,y,w,h),t=15)
        length, info, imgOut=detector.findDistance(lmList[4][:-1],lmList[8][:-1],imgOut)# 45
        x1,y1,x2,y2,cx,cy = info
        conX = ((x+20<cx<(x+w-20)) and (y+20<cy<(y+h-20)))
        if conX and length<45:
            drag=True
        else:
            drag=False
        if drag:
            x+=cx-prevCX
            y+=cy-prevCY
        prevCX = cx
        prevCY = cy
        
    cv2.imshow('Image', imgOut)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break