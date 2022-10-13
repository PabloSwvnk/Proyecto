import pygame as pg

class Nave:
    def __init__(self, center_x, center_y, w = 10, h = 10, color=(255,255,0)):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.w = w
        self.h = h

        self.vx = 0
        self.vy = 0
        
    def dibujar(self, pantalla):

        pg.draw.rect(pantalla, self.color, (self.center_x - self.w // 2, self.center_y - self.h // 2, self.w, self.h))

        