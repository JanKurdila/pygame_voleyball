import pygame
from Config import config
import sys

if __name__ == "__main__":
    pygame.init()
    
    window = pygame.display.set_mode(config.ROZLISENIE)
    pygame.display.set_caption("Volejbal")

    clock = pygame.time.Clock()
    
    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu

        window.fill(config.FARBA_POZADAIA) # Premazanie obrazovky

        pygame.display.update()

        # Spomalenie cyklu
        clock.tick(config.FPS) # Obnova obrázkov