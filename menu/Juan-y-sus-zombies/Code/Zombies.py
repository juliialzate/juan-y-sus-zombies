import pygame
import sys
import random
from pygame.sprite import Sprite
from pygame.locals import *
from Constantes import *
from Jugador import *


screen = pygame.display.set_mode(Tamaño_pantalla)
blanco = (255, 255, 255)


class Zombie(Sprite):
    def __init__(self, contenedor):
        self.vida = 100
        self.vel = [random.randint(-15, -4), 0]
        self.imagenes = [pygame.image.load("../imagenes/zombie_1.png"),
                         pygame.image.load("../imagenes/zombie_2.png"),
                         pygame.image.load("../imagenes/zombie_3.png"),
                         pygame.image.load("../imagenes/zombie_4.png"),
                         pygame.image.load("../imagenes/zombie_5.png"),
                         pygame.image.load("../imagenes/zombie_6.png"),
                         pygame.image.load("../imagenes/zombie_7.png"),
                         pygame.image.load("../imagenes/zombie_8.png")]
        self.muricion = pygame.mixer.Sound("../Sonidos/die_zombie.mp3")
        self.daño_jugador = pygame.mixer.Sound("../Sonidos/daño_jugador1.mp3")
        self.cont = 0
        self.contenedor = contenedor
        self.imagen = pygame.transform.flip(
            self.imagenes[self.cont], True, False)
        self.rect = self.imagen.get_rect()
        self.rect.move_ip(Tamaño_pantalla[0], 350)

    def update(self):
        self.rect = self.rect.move(self.vel)
        self.cont = (self.cont+1) % 8
        self.imagen = pygame.transform.flip(
            self.imagenes[self.cont], True, False)


def si(juanito, zombies):
    final = True
    live = 0
    fuente_go = pygame.font.Font(None, 100)
    texto_fin = fuente_go.render("FIN DEL JUEGO", 1, (250, 0, 0))

    if random.randint(0, 100) % 20 == 0 and len(zombies) < 3:
        zombies.append(Zombie(Tamaño_pantalla))
    for zombie in zombies:
        if juanito.rect.colliderect(zombie.rect):
            zombie.daño_jugador.play()
            juanito.vida -= 1
            screen.blit(zombie.imagen, zombie.rect)
            zombie.muricion.play()
            zombies.remove(zombie)

        live = juanito.vida
        fuente = pygame.font.Font(None, 36)
        t_vida = fuente.render("Vidas: " + str(live), 1, (255, 255, 255))
        screen.blit(t_vida, (800, 10))

        for bala in juanito.balas:
            # for espada in juanito.espadas
            if zombie.rect.colliderect(bala.rect):
                zombie.vida -= 50
                zombie.muricion.play()
                juanito.balas.draw(screen)
                juanito.balas.remove(bala)
        for espada in juanito.espadas:
            if zombie.rect.colliderect(espada.rect):
                zombie.vida -= 50
                zombie.muricion.play()
                juanito.espadas.draw(screen)
                juanito.espadas.remove(espada)
        if zombie.vida <= 0:
            screen.blit(zombie.imagen, zombie.rect)
            zombie.muricion.play()
            zombies.remove(zombie)
        if juanito.vida <= 0:
            screen.blit(texto_fin, (200, Tamaño_pantalla[1]/2))
            final = False
            return False

        if final:
            screen.blit(zombie.imagen, zombie.rect)
            zombie.update()

        return True


def main():
    pygame.init()
    background_image = pygame.image.load("../imagenes/negro.jpg")
    background_rect = background_image.get_rect()
    juanito = Juan(Tamaño_pantalla)
    zombies = []

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        juanito.animar()
        screen.blit(background_image, background_rect)
        screen.blit(juanito.imagen, juanito.rect)
        juanito.balas.draw(screen)
        juanito.espadas.draw(screen)
        si(juanito, zombies)
        pygame.display.update()


if __name__ == "__main__":
    main()
