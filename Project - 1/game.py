import pygame as pg
from sys import exit as close
from abc import abstractmethod,ABC
from random import choice
from time import time
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-p1",default="Player 1", type=str ,help="player name")
parser.add_argument("-p2",default="Player 2", type=str ,help="player name")

args = parser.parse_args()

pg.init()

width = 1280
height = 720
timer = time()
title = "Mohan Ping-Pong Game"
icon_image = pg.image.load("Sprites/ball/Ball.png")
bg_music = pg.mixer.Sound("Audio/music.wav")
bounce_music = pg.mixer.Sound("Audio/bounce.mp3")
bg_music.play(loops = -1)

SCREEN = pg.display.set_mode((width,height), pg.RESIZABLE)
pg.display.set_caption(title)
pg.display.set_icon(icon_image)

CLOCK = pg.time.Clock()
FPS = 60

class Mover(pg.sprite.Sprite, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def update(self):
        pass

class Bar(Mover):
    def __init__(self, type = 1):
        super().__init__()
        self.type= type
        if self.type == 1:
            location = "Sprites/bar/bat1.png"
            pos_x = 10
            self.text = args.p1 + ":"
        else:
            self.text = args.p2 + ":"
            location = "Sprites/bar/bat2.png"
            pos_x = width - 10
        self.image = pg.image.load(location).convert_alpha()
        if type == 1:
            self.rect = self.image.get_rect(midleft = (pos_x, height // 2))
        else:
            self.rect = self.image.get_rect(midright = (pos_x, height // 2))
        self.score = 0
        self.font = pg.font.Font(None, 100)
        self.speed = 7

    def showRect(self):
        if self.type != 1:
            pos_x = width - 10
            self.rect = self.image.get_rect(midright = (pos_x, self.rect.midright[1]))

    def display_score(self):
        if self.type == 1:
            score_pos = width // 2 - 300
            text_score_pos = width // 2 - 500
        else:
            score_pos = width // 2 + 300
            text_score_pos = width // 2 + 100
        self.score_loc = (score_pos, 80)
        self.text_score_loc = (text_score_pos, 80)
        self.score_text = self.font.render(str(self.score), True, "White")
        self.score_text_name = self.font.render(self.text, True, "White")
        self.score_text_name = pg.transform.smoothscale(self.score_text_name, (120,60))
        SCREEN.blit(self.score_text, self.score_loc)
        SCREEN.blit(self.score_text_name, self.text_score_loc)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and (self.rect.y - 1 > 0) and self.type != 1:
            self.rect.y -= self.speed
        elif keys[pg.K_w] and (self.rect.y - 1 > 0) and self.type == 1:
            self.rect.y -= self.speed
        elif keys[pg.K_DOWN] and (self.rect.bottom + 1 < height) and self.type != 1:
            self.rect.y += self.speed
        elif keys[pg.K_s] and (self.rect.bottom + 1 < height) and self.type == 1:
            self.rect.y += self.speed    

    def reset(self):
        self.score = 0
        self.__init__(self.type)

    def update(self):
        self.showRect()
        self.display_score()
        self.move()
    
class Ball(Mover):
    def __init__(self):
        super().__init__()
        self.pos = (width // 2 + choice([-30, 30, -30, 30]), height // 2)
        self.image = pg.image.load("Sprites/ball/Ball.png").convert_alpha()
        self.rect = self.image.get_rect(center = self.pos)
        self.speed_x = 7
        self.speed_y = 7

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed_y *= -1

    def reset(self):
        self.pos = (width // 2 + choice([-30, 30, -30, 30]), height // 2)
        self.rect.center = self.pos

    def update(self):
        self.move()

class Manager:
    @staticmethod
    def collision(sprite, group, kill = False):
        global timer
        if (collided := pg.sprite.spritecollide(sprite, group, kill)) and time() - timer > 1.2:
            collided[0].score += 1
            sprite.speed_x *= -1
            bounce_music.play()
            timer = time()
        if sprite.rect.x<=-100 or sprite.rect.x>=width+100:
            sprite.reset()
            for player in group.sprites():
                player.reset()
            timer = time()

player = pg.sprite.Group()
player.add(Bar())
player.add(Bar(type = 0))

ball = pg.sprite.GroupSingle()
ball.add(Ball())

# Game Loop
while True:

    # Event Loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            close()
        elif event.type == pg.VIDEORESIZE:
            width, height = event.size
            if width < 1280:
                width = 1280
            if height < 720:
                height = 720
            SCREEN = pg.display.set_mode((width,height),pg.RESIZABLE)

    SCREEN.fill("#2C3A47")
    player.draw(SCREEN)
    player.update()
    ball.draw(SCREEN)
    ball.update()
    Manager.collision(ball.sprite, player)
    pg.draw.line(SCREEN, 'White', (width // 2, 0), (width // 2, height), 8)

    pg.display.update()
    CLOCK.tick(FPS)