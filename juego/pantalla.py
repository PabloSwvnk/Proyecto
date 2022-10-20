import pygame as pg
from juego.objetos import Cometa, Nave, Asteroide_G, Asteroide_M, Asteroide_P, Vida
from juego import ANCHO, ALTO, BLANCO, FPS


pg.init()

class Partida:
    def __init__(self, pantalla, metron):
        self.pantalla_principal = pantalla
        
        self.metron = metron
        pg.display.set_caption("The Quest")
        
        self.fondoPantalla = pg.image.load("juego/imagenes/fondo1.png")
        self.nave = Nave()
        self.asteroide1 = Asteroide_G()
        self.asteroide2 = Asteroide_M()
        self.asteroide3 = Asteroide_P()
        self.cometa = Cometa()
        self.vida = Vida()
        
    def bucle_ppal(self):
            
            all_sprites = pg.sprite.Group()
            nave = Nave()
            asteroide1 = Asteroide_G()
            asteroide2 = Asteroide_M()
            asteroide3 = Asteroide_P()
            cometa = Cometa()
            vida = Vida()
            all_sprites.add(nave, asteroide1, asteroide2, asteroide3, cometa, vida)
            self.nave.vy = 0 
            game_over = False
            self.metron.tick()
            
            while not game_over: 
                
                for evento in pg.event.get():
                    if evento.type == pg.QUIT:
                        return True
                
                self.pantalla_principal.blit(self.fondoPantalla, (0,0))            
                all_sprites.update()
                all_sprites.draw(self.pantalla_principal)
                
               

                
                
                
                pg.display.flip()
            

                
class Menu:
    def __init__(self, pantalla, metron):
        self.pantalla_principal_Menu = pantalla
        self.metron = metron
        pg.display.set_caption("Menu")
        self.imagenFondoMenu = pg.image.load("juego/imagenes/fondoM.png")
        self.fuenteComenzar = pg.font.Font("juego/fonts/silkscreen.ttf", 25)
        
    
    def bucle_ppal(self):
        game_over = False
        
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                
            self.pantalla_principal_Menu.blit(self.imagenFondoMenu, (0, 0))
            menu = self.fuenteComenzar.render("Pulsa ENTER para comenzar", True, BLANCO)
            self.pantalla_principal_Menu.blit(menu, (300, ALTO - 400))
            
            pg.display.flip()
            
    
