import random
import pygame
from pygame.locals import QUIT
from main import*

VENTANA_HORI = 1200  
VENTANA_VERT = 600  

class PelotaPong:
    def __init__(self, fichero_imagen):
       

        
        self.imagen = pygame.image.load("ball.png").convert_alpha()

       
        self.ancho, self.alto = self.imagen.get_size()

        
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

        
        self.puntuacion = 0
        self.puntuacion_ia = 0

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= VENTANA_HORI:
            self.reiniciar()
            self.puntuacion += 1
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])

