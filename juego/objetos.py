
from cmath import rect
import pygame as pg

from juego import ALTO, ANCHO, NEGRO


class Nave(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/nave.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.top = 600
        self.rect.bottom = 0
       
        self.rect.centery = ALTO // 2
        
        self.vy = 0
        
    

    def update(self):  
        self.vy = 0
        teclas = pg.key.get_pressed()

        if teclas[pg.K_UP]:
            self.vy = -5
        if teclas[pg.K_DOWN]:
            self.vy = 5
            
        self.rect.centery += self.vy
        if self.rect.centery > ALTO - 30:
            self.rect.centery = ALTO - 30
        if self.rect.centery < 30:
            self.rect.centery = 30