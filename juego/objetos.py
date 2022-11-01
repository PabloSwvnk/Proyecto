
from cmath import rect
from enum import Enum
import pygame as pg
import random 

from juego import ALTO, ANCHO, BLANCO, NEGRO


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
        
        self.rect.centery = ALTO // 2
        self.vy = 0
        self.life = 3
        self.invencible = 180
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

    #def explotando(self):
        if self.status == EstNave.Jugando: 
            self.image = pg.image.load("juego/imagenes/navee.png").convert()
            self.image.set_colorkey(NEGRO)   
            self.life = 3
        else:
            if self.status == EstNave.Explotando:
             self.image = pg.image.load("juego/imagenes/explosion.png").convert()
             self.image.set_colorkey(NEGRO)
             
        
        
            
         
                   
    def vida(self):
        nave = Nave()
        self.vida = pg.image.load("juego/imagenes/vida.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        life = 3

        if  life == 2:
            self.image = pg.image.load("juego/imagenes/vida2.png").convert()
            self.image.set_colorkey(NEGRO) 
            nave.kill()
            
            pg.sprite.add(nave)
            life = 1
                
        if  life == 1:
            self.vida = pg.image.load("juego/imagenes/vida.png").convert()
            self.image.set_colorkey(NEGRO)
            nave.kill()
            pg.sprite.add(nave)
            life = 0
        if  life <= 0:
            nave.kill()
            
            return True  
                          
    def aterrizando(self):
        self.image = pg.image.load("juego/imagenes/navee.png").convert()
        self.image = pg.image.transform.scale(self, ANCHO, ALTO)
        self.image = pg.image.transform.rotate(self, self.rotate)
        self.image.set_colorkey(NEGRO)
        
        

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

    

        
        