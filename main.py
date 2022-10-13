import pygame as pg
from objetos import Nave


pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("The Quest")


game_over = False
nave = Nave(30, 300, w = 20, h = 20)
nave.vy = 0.5

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    teclas = pg.key.get_pressed()
    if teclas[pg.K_UP]:
        nave.center_y -= nave.vy
    if teclas[pg.K_DOWN]:
        nave.center_y += nave.vy


    pantalla_principal.fill((255,0,255))
    nave.dibujar(pantalla_principal)



    pg.display.flip()