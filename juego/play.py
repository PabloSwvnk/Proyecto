import pygame as pg
from juego import *
from juego.pantalla import Partida1, Partida2, Menu, Controles


class Control:
    
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO)) 
        RELOJ = pg.time.Clock()
        self.ix = 0
        self.pantallas = [Menu(pantalla_principal), Controles(pantalla_principal), Partida1(pantalla_principal, RELOJ, MAX_PARTIDA1, VELOCIDAD1, 0), Partida2(pantalla_principal, RELOJ, WIN, VELOCIDAD2, 500)]
        
    def jugar(self):
        salida = False
        game_over = False
        
        
        while not salida and not game_over:
            pg.init()
            
            salida = self.pantallas[self.ix].bucle_ppal()
            self.ix += 1
            
            if self.ix >= len(self.pantallas):
                self.ix = 0
              
    