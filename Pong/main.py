import random
import pygame
from pygame.locals import QUIT
from pelota import*
from Raqueta import*
pygame.mixer.init()




VENTANA_HORI = 1200  
VENTANA_VERT = 600  
FPS = 160  
BLANCO = (255, 255, 255) 
NEGRO = (0, 0, 0)

fondo= pygame.image.load("fondo.png")
pantalla = pygame.display.set_mode((VENTANA_HORI,VENTANA_VERT))


def main():

    pygame.init()
    pantalla.blit(fondo,(0,0))



    sonido_fondo = pygame.mixer.Sound("theme.mp3")
    pygame.mixer.Sound.play(sonido_fondo, -1)
    
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong ")

  
    fuente = pygame.font.Font(None, 60)

    pelota = PelotaPong("ball.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho


    jugando = True
    while jugando:
        
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_ia(pelota)
        ventana.blit(pygame.image.load("fondo.png"),(0,0))
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        texto = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        if(pelota.puntuacion>=10):
            ventana.blit(pygame.image.load("win.png"),(300,100))

        if(pelota.puntuacion_ia>=10):
            ventana.blit(pygame.image.load("lose.png"),(300,100))
            
        
          
        letrero = fuente.render(texto, False, BLANCO)
        ventana.blit(letrero, (VENTANA_HORI / 2 - fuente.size(texto)[0] / 2, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
