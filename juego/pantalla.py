from marshal import load
from string import punctuation
from time import time
import pygame as pg
from juego.objetos import Cometa, EstNave, Nave, Asteroide_G, Asteroide_M, Asteroide_P, Planeta
from juego import ANCHO, ALTO, BLANCO, FPS, NEGRO, MAX_PARTIDA1




pg.init()
pg.mixer.init()

class Partida1:
    
    def __init__(self, pantalla, tiempo):
        self.pantalla_principal = pantalla
        
        RELOJ = pg.time.Clock()
        RELOJ = tiempo
        self.temp = MAX_PARTIDA1
        pg.display.set_caption("The Quest")
        
        self.fondoPantalla1 = pg.image.load("juego/imagenes/fondo1.png")
        self.nave = Nave()
        self.asteroide1 = Asteroide_G()
        self.asteroide2 = Asteroide_M()
        self.asteroide3 = Asteroide_P()
        self.cometa = Cometa()
        self.planeta = Planeta()
        self.puntuacion = 0
        self.fuenteTemp = pg.font.Font("juego/fonts/silkscreen.ttf", 20)
        self.asteroides_list = pg.sprite.Group()
        
        
        self.contadorFoto = 0
    
    def fondo(self):
        self.contadorFoto += 1

    def bucle_ppal(self):
            
            all_sprites = pg.sprite.Group()
            nave = Nave()
            
            
            
            self.puntuacion = 0
            self.temp = MAX_PARTIDA1
            asteroide1 = Asteroide_G()
            asteroide2 = Asteroide_M()
            asteroide3 = Asteroide_P()
            cometa = Cometa()
            planeta = Planeta()
            all_sprites.add(planeta, nave, asteroide1, asteroide2, asteroide3, cometa)
            nave.vy = 0 
           
            game_over = False
            
            asteroides_list = [asteroide1, asteroide2, asteroide3, cometa]
            self.asteroides_list = pg.sprite.Group()
            
            self.status = EstNave.Jugando
            RELOJ = pg.time.Clock()
            self.puntuacion = 0
            #EXPLOSION_SONIDO = pg.mixer.Sound("juego/sonido/explosion.wav")
            fondo = self.fondoPantalla1 
            life = 3
            vida = pg.image.load("juego/imagenes/vida3.png") 
            invencible = 180
            x = 0
            while not game_over:
                self.puntuacion < MAX_PARTIDA1 and self.temp > 0
                tiempo = RELOJ.tick(FPS) 
                self.temp -= tiempo
                
                for evento in pg.event.get():
                    if evento.type == pg.QUIT:
                        return True
                #FONDO MOVIENDOSE
                x_rel = x % fondo.get_rect().width
                self.pantalla_principal.blit(fondo, (x_rel - fondo.get_rect().width, 0))
                if x_rel < ANCHO:
                  self.pantalla_principal.blit(fondo, (x_rel, 0))
                x -= 1            
                self.puntuacion += 1
                
                all_sprites.update()
                RELOJ.tick(60)

                #VIDAS
                if life == 3:
                    vida = pg.image.load("juego/imagenes/vida3.png")    
                if life == 2:
                   vida = pg.image.load("juego/imagenes/vida_2.png")    
                if life == 1:
                   vida = pg.image.load("juego/imagenes/vida_1.png") 
                #COLISIONES
                golpe = pg.sprite.groupcollide([nave], asteroides_list, False, False)    
                                    
                if golpe and invencible >= 180:
                                
                    nave.image = pg.image.load("juego/imagenes/explosion.png").convert()
                    nave.image.set_colorkey(NEGRO)
                                
                        #EXPLOSION_SONIDO.play()
                        #EXPLOSION_SONIDO.set_volume(0, 3)
                    life -=1
                    self.puntuacion -= 10
                    invencible = 0
                    
                              
                            
                if  invencible >= 180:
                    
                    nave.image = pg.image.load("juego/imagenes/navee.png").convert()
                    nave.image.set_colorkey(NEGRO)
                     
                else:
                    invencible += 1 
                    
                    print(life)
                    if life <= 0:
                        nave.kill()
                        return

                if self.puntuacion >= MAX_PARTIDA1:
                    self.puntuacion == 0
                    nave.aterrizando() 
                if MAX_PARTIDA1:
                    invencible >= 600



                    

                 
                

               
                #self.pantalla_principal.blit(fondo, (0,0)) 
                puntuacion = self.fuenteTemp.render(str(self.puntuacion), True, BLANCO)          
                all_sprites.draw(self.pantalla_principal)
                self.pantalla_principal.blit(vida, (600,0)) 
                self.pantalla_principal.blit(puntuacion, (ANCHO // 2, 40))
                
               

                
                
                
                pg.display.flip()
            

                
class Menu:
    def __init__(self, pantalla, metron):
        pg.init()
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


class Controles:
    def __init__(self, pantalla, metron):
        pg.init()
        self.metron = metron
        self.pantalla_principal_Contr = pantalla
        pg.display.set_caption("Controles")
        self.imagenFondoContr = pg.image.load("juego/imagenes/controles.png")           
    
    def bucle_ppal(self):
        game_over = False
        
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                
            self.pantalla_principal_Contr.blit(self.imagenFondoContr, (0, 0))
            
            
            pg.display.flip()