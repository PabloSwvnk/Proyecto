import pygame as pg
import pygame.mixer

pg.mixer.init()

class Sonidos():

 def explosion():

    explosion = pg.mixer.Sound("juego/sonido/explosion.wav")
    pg.mixer.music.load("juego/sonido/explosion.wav")
    #EXPLOSION.play()
    #EXPLOSION.set_volume()
 def principal():
   princi = pg.mixer.Sound("juego/sonido/CancionPrinci.wav")
   pg.mixer.music.load("juego/sonido/CancionPrinci.wav")