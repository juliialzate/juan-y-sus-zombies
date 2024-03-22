import pygame
from Constantes import *


screen = pygame.display.set_mode(Tamaño_pantalla)
FPS = 60
x = 0

# Reloj para controlar la velocidad de actualización del juego
RELOJ = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('../Sonidos/sonidofondo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)


def pantalla():
    x = 0

    background_image = pygame.image.load("../imagenes/fondo.jpg").convert()

    # Calcula la posición relativa del fondo para hacer un desplazamiento continuo
    x_relativa = x % background_image.get_rect().width

    # Dibuja la imagen de fondo en la pantalla
    screen.blit(background_image, (x_relativa -
                                   background_image.get_rect().width, 0))
    pygame.display.update()

    # Dibuja la imagen de fondo nuevamente para hacer el desplazamiento continuo
    if x_relativa < Tamaño_pantalla[0]:
        screen.blit(background_image, (x_relativa, 0))

        # Desplazamiento horizontal del fondo
    x -= 1

    # Controla la velocidad del juego
    RELOJ.tick(FPS)
