
from cmath import rect
import pygame as pg
import random 

from juego import ALTO, ANCHO, BLANCO, NEGRO


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




class Asteroide_G(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/asteroideG.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 800)
        self.rect.y = random.randint(30, 600)
        self.vx = -2
    def update(self): 
        self.rect.x += self.vx
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.rect.y = random.randint(0, 600)
            self.rect.x = random.randint(700, 800)
        

class Asteroide_M(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/asteroideM.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 800)
        self.rect.y = random.randint(0, 600)
        self.vx = -3
    def update(self): 
        self.rect.x += self.vx
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.rect.y = random.randint(0, 600)
            self.rect.x = random.randint(700, 800)


class Asteroide_P(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/asteroideP.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 800)
        self.rect.y = random.randint(0, 600)
        self.vx = -3
    def update(self): 
        self.rect.x += self.vx
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.rect.y = random.randint(0, 600)
            self.rect.x = random.randint(700, 800)

class Cometa(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/cometa.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 800)
        self.rect.y = random.randint(0, 600)
        self.vx = -5
    def update(self): 
        self.rect.x += self.vx
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.rect.y = random.randint(0, 600)
            self.rect.x = random.randint(700, 800)


class Vida(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/vida.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        
        