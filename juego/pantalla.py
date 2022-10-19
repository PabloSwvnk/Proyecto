import pygame as pg
from juego.objetos import Nave
from juego import ANCHO, ALTO, BLANCO, FPS


pg.init()

class Partida:
    def __init__(self, pantalla, metron):
        self.pantalla_principal = pantalla
        
        self.metron = metron
        pg.display.set_caption("The Quest")
        
        self.fondoPantalla = pg.image.load("juego/imagenes/fondoP.png")
        self.nave = Nave()
        


    def bucle_ppal(self):
            
            all_sprites = pg.sprite.Group()
            nave = Nave()
            
            all_sprites.add(nave)
            self.nave.vy = 1 
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
            
    
