import pygame as pg
from juego import *
from juego.pantalla import Partida1, Menu, Controles


class Control:
    
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pantalla_principal_Menu = pg.display.set_mode((ANCHO, ALTO))
        pantalla_principal_Contr = pg.display.set_mode((ANCHO, ALTO))
        RELOJ = pg.time.Clock()
        
        self.pantallas = [Menu(pantalla_principal_Menu, RELOJ), Controles(pantalla_principal_Contr, RELOJ), Partida1(pantalla_principal, RELOJ, MAX_PARTIDA1,), Partida1(pantalla_principal, RELOJ, WIN)]

        #self.menu = Menu(pantalla_principal_Menu, RELOJ)
        #self.contr = Controles(pantalla_principal_Contr, RELOJ)
        #self.partida1 = Partida1(pantalla_principal, RELOJ, MAX_PARTIDA1)
        #self.partida2 = Partida1(pantalla_principal, RELOJ, WIN)
        
    def jugar(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        RELOJ = pg.time.Clock()
        salida = False
        game_over = False
        ix = 0
        nivel = 0
        while not salida and not game_over:
            #if nivel == 1:
                #Partida1(pantalla_principal, RELOJ)
            #if nivel == 2:
               # Partida2(pantalla_principal, RELOJ)
            salida = self.pantallas[ix].bucle_ppal()
            ix += 1
            #nivel += 1
            if ix >= len(self.pantallas):
                ix = 0
               # nivel = 0
    
    
    