import pygame as pg
from juego import ANCHO, ALTO
from juego.pantalla import Partida1, Menu, Controles

class Control:
    
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pantalla_principal_Menu = pg.display.set_mode((ANCHO, ALTO))
        pantalla_principal_Contr = pg.display.set_mode((ANCHO, ALTO))
        RELOJ = pg.time.Clock()

        self.pantallas = [Menu(pantalla_principal_Menu, RELOJ), Controles(pantalla_principal_Contr, RELOJ), Partida1(pantalla_principal, RELOJ)]

        self.menu = Menu(pantalla_principal_Menu, RELOJ)
        self.contr = Controles(pantalla_principal_Contr, RELOJ)
        self.partida1 = Partida1(pantalla_principal, RELOJ)

    def jugar(self):
        salida = False
        ix = 0
        while not salida:
        #while bool(salida) == False:
            salida = self.pantallas[ix].bucle_ppal()
            ix += 1
            if ix >= len(self.pantallas):
                ix = 0

    
    
    