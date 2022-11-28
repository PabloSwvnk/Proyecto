from marshal import load
from string import punctuation
from time import time
import pygame as pg
from juego.objetos import Cometa, EstNave, Nave, Asteroide_G, Asteroide_M, Asteroide_P, Planeta,  Planeta2
from juego import ANCHO, ALTO, BLANCO, FPS, NEGRO, MAX_PARTIDA1, WIN

import sys
#from juego.gameover import GameOver
#from juego.sonido import Sonidos



pg.init()
pg.mixer.init()

class Partida1:
    
    def __init__(self, pantalla, tiempo, PuntuacionMax, velocidad, bonus):
        self.pantalla_principal = pantalla
        self.RELOJ = tiempo
        self.puntuacionMax = PuntuacionMax
        self.bonus = bonus 
        self.velocidad = velocidad
        self.life = 3
        pg.display.set_caption("Nivel 1")
        

        self.imagenFondoGO = pg.image.load("juego/imagenes/gameover.png")
        self.fondoPantalla1 = pg.image.load("juego/imagenes/fondo1.png")
        self.imagenFondoMenu = pg.image.load("juego/imagenes/fondoM.png")
        self.nave = Nave()
        self.asteroide1 = Asteroide_G(self.velocidad)
        self.asteroide2 = Asteroide_M(self.velocidad * 2)
        self.asteroide3 = Asteroide_P(self.velocidad * 2)
        self.cometa = Cometa(self.velocidad * 3)
        self.planeta = Planeta()
        
        self.puntuacion = 0
        self.fuenteTemp = pg.font.Font("juego/fonts/silkscreen.ttf", 20)
        self.fuenteComenzar = pg.font.Font("juego/fonts/silkscreen.ttf", 25)
        self.asteroides_list = pg.sprite.Group()
        
        
        self.contadorFoto = 0
    
    def fondo(self):
        self.contadorFoto += 1

    def bucle_ppal(self):
            #musica
            self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
            self.fuente = pg.font.Font("juego/fonts/silkscreen.ttf", 25)
            self.cancion = pg.mixer.music.load("juego/sonido/Mjuego.wav")
            pg.mixer.music.set_volume(0.4)
            #self.explosion = pg.mixer.Sound("juego/sonido/explosion.wav")
            #pg.mixer.Sound.set_volume(0.3)

            all_sprites = pg.sprite.Group()
            nave = Nave()
            self.puntuacion = 0
            self.temp = MAX_PARTIDA1
            
            planeta = Planeta()
            all_sprites.add(planeta, nave, self.asteroide1, self.asteroide2, self.asteroide3, self.cometa)
            nave.vy = 0 
            
            
            
            asteroides_list = [self.asteroide1, self.asteroide2, self.asteroide3, self.cometa]
            self.asteroides_list = pg.sprite.Group()
            
            self.status = EstNave.Jugando
            self.RELOJ = pg.time.Clock()
            self.puntuacion = 0
            self.puntuacion = self.puntuacion + self.bonus
            
            fondo = self.fondoPantalla1 
            self.life = 3
            #EXPLOSION_SONIDO = pg.mixer.music.load("juego/sonido/explosion.wav")
            

            invencible = 180
            x = 0
            self.final = False
            self.game_over = False
            running = False
            pg.mixer.music.play()
            
            while not running:
                
                self.RELOJ.tick(FPS) 
                self.game_over = False
                #key = pg.key.get_pressed()
               # self.puntuacion < MAX_PARTIDA1 and self.temp > 0
                
                #self.temp -= tiempo
                
                
                for evento in pg.event.get():
                    if evento.type == pg.QUIT:
                        return True
                    
                    if evento.type == pg.KEYDOWN:
                        if evento.key == pg.K_p:
                            if self.game_over:
                                GameOver()
                            else:

                             running = True
                
                            
                #FONDO MOVIENDOSE
                x_rel = x % fondo.get_rect().width
                self.pantalla_principal.blit(fondo, (x_rel - fondo.get_rect().width, 0))
                if x_rel < ANCHO:
                  self.pantalla_principal.blit(fondo, (x_rel, 0))
                x -= 1
                           
                self.puntuacion += 1
                 

                all_sprites.update()

                #tiempo
                self.RELOJ.tick(FPS)
                
                #VIDAS
                if self.life == 3:
                    vida = pg.image.load("juego/imagenes/vida3.png")    
                if self.life == 2:
                   vida = pg.image.load("juego/imagenes/vida_2.png")    
                if self.life == 1:
                   vida = pg.image.load("juego/imagenes/vida_1.png") 
                #COLISIONES
                golpe = pg.sprite.groupcollide([nave], asteroides_list, False, False)    
                                    
                if golpe and invencible >= 120:       
                    nave.image = pg.image.load("juego/imagenes/explosion.png").convert()
                    nave.image.set_colorkey(NEGRO)
                    
                    #pg.mixer.Sound.play()
                    #EXPLOSION_SONIDO.play()
                    #EXPLOSION_SONIDO.set_volume(0, 3)
                    self.life -=1

                    print(self.RELOJ)

                    if self.puntuacion >= 100:
                        self.puntuacion -= 100
                    else: 
                        self.puntuacion = 0
                        
                    invencible = 0
                    self.contadorFoto = 0
                    self.nave.vy = 0     
                            
                if  invencible >= 140:
                    
                    nave.image = pg.image.load("juego/imagenes/navee.png").convert()



                    nave.image.set_colorkey(NEGRO)
                    
                else:
                    invencible += 1 
                    self.contadorFoto += 1
                    print(invencible)
                    
                if self.life <= 0:
                    self.game_over = True
                    
                    #Guardar en bbdd el valor de puntuacion actual
                    GameOver.bucle_ppal(self)

                if not self.game_over:
                    all_sprites.update()
                if self.puntuacion >= self.puntuacionMax:
                    
                    self.puntuacion = self.puntuacionMax
                    self.contadorFoto = 0
                    invencible = 1
                    x = 0  
                    nave.aterrizando() 
                    planeta.update() 
                    
                    self.asteroide1.kill()
                    self.asteroide2.kill()
                    self.asteroide3.kill()
                    self.cometa.kill()
                    next = self.fuente.render("¡Has llegado al primer planeta!", True, BLANCO)
                    pulsa = self.fuente.render("Pulsa P para el siguiente nivel", True, BLANCO)
                    self.pantalla_principal.blit(next, (70, 100))
                    self.pantalla_principal.blit(pulsa, (40, 500))
                    
                #PANTALLA  
                puntuacion = self.fuenteTemp.render(str(self.puntuacion), True, BLANCO)          
                all_sprites.draw(self.pantalla_principal)
                self.pantalla_principal.blit(vida, (600,0)) 
                self.pantalla_principal.blit(puntuacion, (50, 35, ANCHO // 2,  40))
                
               
                
                
                  
                
                pg.display.flip()
            
                

#----------------------------------------- PARTIDA 2 --------------------------------------------------------




class Partida2:
    
    def __init__(self, pantalla, tiempo, PuntuacionMax, velocidad, bonus ):
        self.pantalla_principal = pantalla
        self.RELOJ = tiempo
        self.puntuacionMax = PuntuacionMax
        self.bonus = bonus 
        self.velocidad = velocidad
        
        pg.display.set_caption("Nivel 2")
        


        self.fondoPantalla1 = pg.image.load("juego/imagenes/fondo1.png")
        self.imagenFondoGO = pg.image.load("juego/imagenes/gameover.png")
        self.nave = Nave()
        self.asteroide1 = Asteroide_G(self.velocidad * 2)
        self.asteroide2 = Asteroide_M(self.velocidad * 3)
        self.asteroide3 = Asteroide_P(self.velocidad * 3)
        self.cometa = Cometa(self.velocidad * 4)
        self.planeta2 = Planeta2()
        self.puntuacion = 0
        self.fuenteTemp = pg.font.Font("juego/fonts/silkscreen.ttf", 20)
        self.asteroides_list = pg.sprite.Group()
        
        
        self.contadorFoto = 0
    
    def fondo(self):
        self.contadorFoto += 1

    def bucle_ppal(self):
        self.fuente = pg.font.Font("juego/fonts/silkscreen.ttf", 25)
        #musica
        #self.explosion = pg.mixer.Sound("juego/sonido/explosion.wav")
        #pg.mixer.Sound.set_volume(0.3)

        all_sprites = pg.sprite.Group()
        nave = Nave()
        self.puntuacion = 0
        self.temp = MAX_PARTIDA1
          
        planeta2 = Planeta2()
        all_sprites.add(planeta2, nave, self.asteroide1, self.asteroide2, self.asteroide3, self.cometa)
        nave.vy = 0 
           
        game_over = False
            
        asteroides_list = [self.asteroide1, self.asteroide2, self.asteroide3, self.cometa]
        self.asteroides_list = pg.sprite.Group()
            
        self.status = EstNave.Jugando
        self.RELOJ = pg.time.Clock()
        self.puntuacion = 0
        self.puntuacion = self.puntuacion + self.bonus
            
        fondo = self.fondoPantalla1 
        life = 3
        #EXPLOSION_SONIDO = pg.mixer.music.load("juego/sonido/explosion.wav")
            

        invencible = 180
        x = 0
        
            
        #while not game_over:
                
            #self.cancion.set_volume(0, 3)
            # self.puntuacion < MAX_PARTIDA1 and self.temp > 0
            #self.RELOJ.tick(FPS) 
            #self.temp -= tiempo
                
                
            #for evento in pg.event.get():
               # if evento.type == pg.QUIT:
                    #return True

                #if evento.type == pg.KEYDOWN:
                    #if evento.key == pg.K_p:
                        #game_over = True
        
        running = False
        pg.mixer.music.play()
            
        while not running:
                
            self.RELOJ.tick(FPS) 
            self.game_over = False
                #key = pg.key.get_pressed()
               # self.puntuacion < MAX_PARTIDA1 and self.temp > 0
                
                #self.temp -= tiempo
                
                
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                    
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_p:
                        if self.game_over:
                            GameOver()
                        else:

                            running = True
                        
            #FONDO MOVIENDOSE
            x_rel = x % fondo.get_rect().width
            self.pantalla_principal.blit(fondo, (x_rel - fondo.get_rect().width, 0))
            if x_rel < ANCHO:
                self.pantalla_principal.blit(fondo, (x_rel, 0))
            x -= 1
                           
            self.puntuacion += 1
                 

            all_sprites.update()

            #tiempo
            self.RELOJ.tick(FPS)
                
            #VIDAS
            if life == 3:
                vida = pg.image.load("juego/imagenes/vida3.png")    
            if life == 2:
                vida = pg.image.load("juego/imagenes/vida_2.png")    
            if life == 1:
                vida = pg.image.load("juego/imagenes/vida_1.png") 
            #COLISIONES
            golpe = pg.sprite.groupcollide([nave], asteroides_list, False, False)    
                                    
            if golpe and invencible >= 120:       
                nave.image = pg.image.load("juego/imagenes/explosion.png").convert()
                nave.image.set_colorkey(NEGRO)
                    
                #pg.mixer.Sound.play()
                #EXPLOSION_SONIDO.play()
                #EXPLOSION_SONIDO.set_volume(0, 3)
                life -=1

                print(self.RELOJ)

                if self.puntuacion >= 100:
                    self.puntuacion -= 100
                else: 
                    self.puntuacion = 0
                        
                invencible = 0
                self.contadorFoto = 0
                self.nave.vy = 0     
                            
            if  invencible >= 120:
                    
                nave.image = pg.image.load("juego/imagenes/navee.png").convert()



                nave.image.set_colorkey(NEGRO)
                    
            else:
                invencible += 1 
                self.contadorFoto += 1
                print(invencible)
                    
            if life <= 0:
                self.game_over = True
                GameOver.bucle_ppal(self)
            if not self.game_over:
                    all_sprites.update()

            if self.puntuacion >= self.puntuacionMax:
                    
                self.puntuacion = self.puntuacionMax
                self.contadorFoto = 0
                invencible = 1
                x = 0  
                nave.aterrizando() 
                planeta2.update() 
                    
                self.asteroide1.kill()
                self.asteroide2.kill()
                self.asteroide3.kill()
                self.cometa.kill()
                next = self.fuente.render("¡Has llegado al último planeta!", True, BLANCO)
                pulsa = self.fuente.render("Pulsa P para salir", True, BLANCO)
                self.pantalla_principal.blit(next, (70, 100))
                self.pantalla_principal.blit(pulsa, (30, 500))
                    
            #PANTALLA     
            puntuacion = self.fuenteTemp.render(str(self.puntuacion), True, BLANCO)          
            all_sprites.draw(self.pantalla_principal)
            self.pantalla_principal.blit(vida, (600,0)) 
            self.pantalla_principal.blit(puntuacion, (50, 35, ANCHO // 2,  40))
                
               

                
                
                 
            pg.display.flip()
                         
class GameOver:
    def __init__(self, pantalla):
        self.pantalla_principal_GO = pg.display.set_mode((ANCHO, ALTO))
        self.pantalla_principal = pantalla
        self.imagenFondoGO = pg.image.load("juego/imagenes/gameover.png")   
        #puntuacion = self.puntuacion 
        pg.display.set_caption("Game_Over")
                  
    
    def bucle_ppal(self):
        running = False

        while not running:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.game_over = True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_p:
                        #if self.game_over == True:
                            running = True
                            return  True
                
            self.pantalla_principal.blit(self.imagenFondoGO, (0, 0))
            #puntuacion = self.fuenteTemp.render(str(puntuacion), True, BLANCO)
            #self.pantalla_principal.blit(puntuacion, (50, 35, ANCHO // 2,  40))
                
            pg.display.flip()            
                
class Menu:
    def __init__(self, pantalla):
        
        self.pantalla_principal = pantalla
        pg.display.set_caption("Menu")
        self.imagenFondoMenu = pg.image.load("juego/imagenes/fondoM.png")
        self.fuenteComenzar = pg.font.Font("juego/fonts/silkscreen.ttf", 25)
        self.cancion = pg.mixer.music.load("juego/sonido/Menu.wav")
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(0.3)
    
    def bucle_ppal(self):
        game_over = False
        pg.mixer.music.play()
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                
            self.pantalla_principal.blit(self.imagenFondoMenu, (0, 0))
            menu = self.fuenteComenzar.render("Pulsa ENTER para comenzar", True, BLANCO)
            self.pantalla_principal.blit(menu, (220, ALTO - 400))
            
            pg.display.flip()


class Controles:
    def __init__(self, pantalla):
        
        self.pantalla_principal = pantalla
        pg.display.set_caption("Controles")
        self.imagenFondoContr = pg.image.load("juego/imagenes/controlesJ.png")           
    
    def bucle_ppal(self):
        game_over = False
        
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                
            self.pantalla_principal.blit(self.imagenFondoContr, (0, 0))
            
            
            pg.display.flip()

