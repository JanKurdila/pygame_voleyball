import pygame
from Config import config
import sys

def move_player(player, keys):
    """Funkcia rieši pohyb hráča nahor alebo nadol"""
    if keys[pygame.K_UP]:
       if player.top > 0:
           player.top -= config.STEP

    if keys[pygame.K_DOWN]:
        if player.bottom < config.ROZLISENIE[1]:
            player.bottom += config.STEP

if __name__ == "__main__":
    pygame.init()

    window = pygame.display.set_mode(config.ROZLISENIE)
    pygame.display.set_caption("Volejbal")

    clock = pygame.time.Clock()

    hrac1 = pygame.Rect(config.ROZLISENIE[0] - 110, config.ROZLISENIE[1] // 2 - 50, 10, 100)
    hrac2 = pygame.Rect(110, config.ROZLISENIE[1] // 2 - 50, 10, 100)

    lopta = pygame.Rect(config.ROZLISENIE[0]/2 -10, config.ROZLISENIE[1]/2 -10, 20, 20)

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Vypnutie pygamu
                sys.exit()  # Vypnutie celého programu
        
        lopta.x += config.RYCHLOST_LOPTY[0] * 3
        lopta.y += config.RYCHLOST_LOPTY[1] * 3


        keys = pygame.key.get_pressed()
        move_player(hrac1, keys)

        window.fill(config.FARBA_POZADAIA)  # Premazanie obrazovky

        pygame.draw.rect(window, "white", hrac1)
        pygame.draw.rect(window, "white", hrac2)
        pygame.draw.circle(window, config.FARBA_LOPTY, lopta.center, config.POLOMER_LOPTY)

        pygame.display.update()

        # Spomalenie cyklu
        clock.tick(config.FPS)  # Obnova obrázkov
