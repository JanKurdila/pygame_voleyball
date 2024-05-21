import pygame
from Config import config
import sys

if __name__ == "__main__":
    pygame.init()

    window = pygame.display.set_mode(config.ROZLISENIE)
    pygame.display.set_caption("Volejbal")

    clock = pygame.time.Clock()

    hrac1 = pygame.Rect(config.ROZLISENIE[0]- 110, config.ROZLISENIE[1]//2 - 50, 10, 100)
    hrac2 = pygame.Rect(110, config.ROZLISENIE[1]//2 - 50, 10, 100)

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu

        window.fill(config.FARBA_POZADAIA) # Premazanie obrazovky

        pygame.draw.rect(window, "white", hrac1)
        pygame.draw.rect(window, "white", hrac2)

        pygame.display.update()

        # Spomalenie cyklu
        clock.tick(config.FPS) # Obnova obrázkov