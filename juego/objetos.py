
from cmath import rect
import pygame as pg

from juego import ALTO, ANCHO


class Nave(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/nave.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 60
        
        self.rect.centery = ALTO // 2
        self.y_max = 600
        self.vy = 0
        
    

    def update(self):  
        self.vy = 0
        teclas = pg.key.get_pressed()
        
        if teclas[pg.K_UP]:
            self.vy = -5
           #self.rect.centery -= self.vy
        #if self.rect.centery < 0 + ALTO // 2:
            #self.rect.centery = ALTO // 2

        if teclas[pg.K_DOWN]:
            self.vy = 5
            #self.rect.centery += self.vy
        #if self.rect.centery > self.y_max - ALTO // 2:
           # self.rect.centery = self.y_max - ALTO // 2

        self.rect.y += self.vy
        if self.rect.top > ALTO:
            self.rect.top = ALTO
        if self.rect.bottom < 0:
            self.rect.bottom = 0