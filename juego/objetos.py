from cmath import rect
from enum import Enum
import pygame as pg
import random 

from juego import ALTO, ANCHO, BLANCO, NEGRO, MAX_PARTIDA1, WIN


class EstNave(Enum):

     
     Jugando = 1
     Explotando = 2
     
     
class Nave(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pg.image.load("juego/imagenes/navee.png").convert()

        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.top = 600
        self.rect.bottom = 0
        self.rect.x = 0
        self.rect.centery = ALTO // 2
        self.puntuacion = 0
        self.vy = 0
        self.vx = 0
        self.life = 3
        self.invencible = 120
        self.status = EstNave.Jugando
        
    
    def update(self):  
        self.vy = 0
        
        teclas = pg.key.get_pressed()
          
        if teclas[pg.K_UP]:
            self.vy = -10
        if teclas[pg.K_DOWN]:
            self.vy = 10
            
        self.rect.centery += self.vy
        if self.rect.centery > ALTO - 30:
            self.rect.centery = ALTO - 30
        if self.rect.centery < 30:
            self.rect.centery = 30

                        
                          
    def aterrizando(self):
       
        self.nave = self.image 
        self.image = pg.image.load("juego/imagenes/navee.png").convert()
        self.image.set_colorkey(NEGRO)
        self.vx = 3

        #if MAX_PARTIDA1:
           
        self.rect.centery = ALTO // 2
        self.rect.x += self.vx
        if self.rect.x > ANCHO - 150:
              self.rect.x = ANCHO - 150
              if self.rect.x <= ANCHO - 150: 
                 self.image = pg.transform.rotate(self.image, 180)
              else:
                 if self.rect.x <= ANCHO - 150:  
                    self.image.set_colorkey(NEGRO)
            
       
        

class Asteroide_G(pg.sprite.Sprite):
    def __init__(self, velocidad):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/asteroideG.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 800)
        self.rect.y = random.randint(30, 600)
        self.vx = velocidad
        
    def update(self): 
        self.rect.x += self.vx
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.rect.y = random.randint(0, 600)
            self.rect.x = random.randint(700, 800)


class Asteroide_M(pg.sprite.Sprite):
    def __init__(self, velocidad):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/asteroideM.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 800)
        self.rect.y = random.randint(0, 600)
        self.vx = velocidad
        
    def update(self): 
        self.rect.x += self.vx
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.rect.y = random.randint(0, 600)
            self.rect.x = random.randint(700, 800)
        

class Asteroide_P(pg.sprite.Sprite):
    def __init__(self, velocidad):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/asteroideP.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 800)
        self.rect.y = random.randint(0, 600)
        self.vx = velocidad
    def update(self): 
        self.rect.x += self.vx
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.rect.y = random.randint(0, 600)
            self.rect.x = random.randint(700, 800)
        
class Cometa(pg.sprite.Sprite):
    def __init__(self, velocidad):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/cometa.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 800)
        self.rect.y = random.randint(0, 600)
        self.vx = velocidad
    def update(self): 
        self.rect.x += self.vx
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600:
            self.rect.y = random.randint(0, 600)
            self.rect.x = random.randint(700, 800)

        
class Planeta(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/jupiter.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 100
        self.vx = -2
        self.puntuacion = 0
    def update(self): 
        if MAX_PARTIDA1 or WIN:
            self.rect.x += self.vx
            if self.rect.x <= 450:
                self.rect.x = 450
                self.vx -= 0
           
class Planeta2(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("juego/imagenes/planeta2.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 100
        self.vx = -2
        self.puntuacion = 0
    def update(self): 
        if MAX_PARTIDA1 or WIN:
            self.rect.x += self.vx
            if self.rect.x <= 450:
                self.rect.x = 450
                self.vx -= 0        