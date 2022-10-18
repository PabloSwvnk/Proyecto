import pygame as pg
from juego import ANCHO, ALTO
from juego.pantalla import Partida, Menu

class Control:
    
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pantalla_principal_Menu = pg.display.set_mode((ANCHO, ALTO))
        metron = pg.time.Clock()

        self.pantallas = [Menu(pantalla_principal_Menu, metron), Partida(pantalla_principal, metron)]

        self.menu = Menu(pantalla_principal_Menu, metron)
        self.partida = Partida(pantalla_principal, metron)

    def jugar(self):
        salida = False
        ix = 0
        while not salida:
        #while bool(salida) == False:
            salida = self.pantallas[ix].bucle_ppal()
            ix += 1
            if ix >= len(self.pantallas):
                ix = 0

    
    