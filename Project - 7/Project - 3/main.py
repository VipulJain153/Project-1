import pygame as pg, random, numpy as np, cvzone.PoseModule as HTM, cv2

pg.init()


class SnakeGameClass:
    def __init__(self):
        pass


class Runner:
    def __init__(self):
        self.SCREEN = pg.display.set_mode((1280, 720))
        pg.display.set_caption("Snake Game")
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        self.cap.set(cv2.CAP_PROP_FPS, 80)
        self.cap.set(10, 0)
        self.detector = HTM.PoseDetector(detectionCon=0.85)

    def cam(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            _, img = self.cap.read()
            img = cv2.flip(img, 1)
            self.detector.findPose(img)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgRGB = np.rot90(imgRGB)
            surface = pg.transform.flip(pg.surfarray.make_surface(imgRGB), True, False)
            self.SCREEN.blit(surface,(0,0))
            pg.display.update()


if __name__ == "__main__":
    run = Runner()
    run.cam()
