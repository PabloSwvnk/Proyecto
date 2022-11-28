import pygame as pg
from juego import *
from juego.pantalla import Partida1, Partida2, Menu, Controles, GameOver


class Control:
    
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO)) 
        RELOJ = pg.time.Clock()
        #pg.time.set_timer
        self.ix = 0
        self.pantallas = [Menu(pantalla_principal), Controles(pantalla_principal), Partida1(pantalla_principal, RELOJ, MAX_PARTIDA1, VELOCIDAD1, 0), Partida2(pantalla_principal, RELOJ, WIN, VELOCIDAD2, 500)]
    def jugar(self):
        salida = False
        game_over = False
        
        
        while not salida and not game_over:
            pg.init()
            #for evento in self.pantallas[ix]:
            #for evento in pg.event.get():
                #if evento.type == pg.QUIT:
                    #game_over = True
                
                #if evento.type == pg.KEYDOWN:
                    #if evento.key == pg.K_RETURN:
                       # game_over = True
                
                
            #si la pantalla es la del record
            #recupera de la bbdd los 3 mejores

            #if GameOver == True:
                #self.ix = 0
                #GameOver = False

            salida = self.pantallas[self.ix].bucle_ppal()
            self.ix += 1
            
            if self.ix >= len(self.pantallas):
                self.ix = 0
              
    