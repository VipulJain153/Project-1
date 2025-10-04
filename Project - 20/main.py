import pyautogui as controller
import time
from PIL import ImageGrab,Image
import numpy as np
import keyboard

def getFrame():
    frame = ImageGrab.grab()
    framen = np.array(frame)
    catus_frame =framen[600:723,220:385].ravel()
    if any(catus_frame < np.full_like(catus_frame,100)):
        controller.press("up")
    # for i in range(600,720):
    #     for j in range(220,340):
    #         framen[i,j]=0
    # Image.fromarray(framen).show()

if __name__ == "__main__":
    time.sleep(3)
    while not keyboard.is_pressed("alt"):   
        getFrame()     