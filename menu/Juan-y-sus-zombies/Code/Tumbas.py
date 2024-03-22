
import pygame
import random
from pygame.sprite import Sprite

from Constantes import *
from Jugador import *
from Pantalla import *
from Zombies import *


class Tumbas(Sprite):
    def __init__(self, contenedor):
        Sprite.__init__(self)
        self.contenedor = contenedor
        self.cont = 0
        self.imagenes = tumba_img1
        self.imagen = self.imagenes[self.cont]
        self.image = self.imagen
        self.rect = self.image.get_rect()
        self.velocidad = 2.5
        self.rect.x = Tamaño_pantalla[0]
        self.rect.y = 425
        self.daño_jugador = pygame.mixer.Sound("../Sonidos/daño_jugador2.mp3")

    def update(self):

        self.rect.x -= self.velocidad
        if self.rect.x + 50 < 0:
            self.rect.x = Tamaño_pantalla[0]

        self.cont = (self.cont + 1) % 18
        self.imagenes = tumba_img2
        self.image = self.imagenes[self.cont]
        # pygame.time.delay(80)


def tumPlay(juanito, tumbas, puntos):
    final = True
    for tumba in tumbas:
        if juanito.vida <= 0:
            final = False

        if final:
            tumba.update()
            screen.blit(tumba.image, tumba.rect)

            if juanito.rect.colliderect(tumba.rect) and tumba.image == tumba_img2[8]:
                # para sonido de interaccion
                juanito.vida -= 1
                tumba.daño_jugador.play()

            elif juanito.rect.colliderect(tumba.rect):
                puntos += 10
                tumbas.remove(tumba)

    if random.randint(0, 1000) % 20 == 0 and len(tumbas) < 3:
        pygame.time.delay(200)
        tumbas.append(Tumbas(size))
    return puntos


size = Tamaño_pantalla
screen = pygame.display.set_mode(size)
puntos = 0
tumbas = []
juanito = Juan(Tamaño_pantalla)
