import cv2, os
from cvzone.HandTrackingModule import HandDetector
from cvzone import putTextRect, stackImages
from random import randint
from time import time,strftime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 80)
detector = HandDetector(maxHands = 1, detectionCon = 0.85)
p = None
ais=0
ps=0
now=time()
os.chdir("Resources")
aiImgs = list(map(lambda x: cv2.resize(x,(640,480)),list(map(cv2.imread,["paper.png","rock.jpg", "scissors.jpg"]))))
initialImg = 0
result=None

def checkWin(p, key):
        global ais,ps
        if p==key:
            return -1
        elif key==1 and p==2:
            ais+=1
            return 1
        elif key==1 and p==0:
            ps+=1
            return 0
        elif key==0 and p==1:
            ais+=1
            return 1
        elif key==0 and p==2:
            ps+=1
            return 0
        elif key==2 and p==0:
            ais+=1
            return 1
        elif key==2 and p==1:
            ps+=1
            return 0

def generate():
    key = randint(0,2)
    return key

while True:
    _, img =  cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType = False)
    if hands and ((time()-now)>4):
        fingers = detector.fingersUp(hands[0])
        fingers[0] = int(not fingers[0])
        if all([i==0 for i in fingers]):
            p = 1
        elif all(fingers):
            p = 0
        elif fingers[1] and fingers[2]:
            p = 2
        else:
            p = None
        if p is not None:
            initialImg = generate()
            result = checkWin(p, initialImg)
            now = time()
    img = stackImages([img,aiImgs[initialImg]],2,1)
    if result!=None:
        if result==-1:
            img,_ = putTextRect(img,'Draw!',pos=(1280//2-70,390))
        elif result==1:
            img,_ = putTextRect(img,f'AI Wins!',pos=(1280//2-100,390))
        elif result==0:
            img,_ = putTextRect(img,f'Player Wins!',pos=(1280//2-120,390))
    putTextRect(img,f"AI Score: {ais}",pos=(650,50))
    putTextRect(img,f"Player Score: {ps}",pos=(0,50))
    cv2.imshow("Rock Paper Scissors", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite(strftime("../img_%Y_%m_%d_%H_%M-%S.png"),img)
        break

cap.release()
cv2.destroyAllWindows()