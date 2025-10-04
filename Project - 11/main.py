import pygame as pg
from sys import exit as close

pg.init()
FPS=60
CLOCK = pg.time.Clock()
WIDTH = 1280
HEIGHT = 720
SCREEN= pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("AutoDraw")
drawArr = []
colorArr = []
draw = False

colors = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(255,255,255)]
index = 0

def drawing():
    for i,pos in enumerate(drawArr):
        if colorArr[i] != (255,255,255):
            pg.draw.circle(SCREEN,colorArr[i],pos,4,8)
        else:
            pg.draw.circle(SCREEN,colorArr[i],pos,20,46)

while True:
    SCREEN.fill("white")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            drawing()
            pg.image.save(SCREEN,"img.png")
            pg.quit()
            close()
        if event.type == pg.MOUSEBUTTONDOWN:
            draw=True
        if event.type == pg.MOUSEBUTTONUP:
            draw=False
        if event.type == pg.MOUSEMOTION and draw:
                drawArr.append(event.pos)
                colorArr.append(colors[index])
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                drawArr.clear()
                colorArr.clear()
            if event.key == pg.K_s:
                index+=1
                if index>=len(colors):index=0
    drawing()
    pg.display.update()
    CLOCK.tick(FPS)