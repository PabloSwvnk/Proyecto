#import pygame as pg

#pg.init()

#class GameOver:
 #   def __init__(self, pantalla):
        
  #      self.pantalla_principal_GO = pantalla
  #      pg.display.set_caption("Game_Over")
  #      self.imagenFondoContr = pg.image.load("juego/imagenes/gameover.png")           
    
 #   def bucle_ppal(self):
 #       game_over = False
 #       
 #       while not game_over:
 #           for evento in pg.event.get():
 #               if evento.type == pg.QUIT:
 #                   game_over = True
                
#                if evento.type == pg.KEYDOWN:
#                    if evento.key == pg.K_RETURN:
 #                       game_over = True
                
#            self.pantalla_principal_GO.blit(self.imagenFondoContr, (0, 0))
#            
 #           
 #           pg.display.flip()