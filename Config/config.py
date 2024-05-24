import random
import pygame

ROZLISENIE = (800, 600)
FARBA_POZADIA = (0, 0, 0)
FARBA_LOPTY = (255, 255, 255)
POLOMER_LOPTY = 10
RYCHLOST_LOPTY = [random.choice([1, -1]), random.choice([1, -1])]
STEP = 5
FPS = 60

HRAC1_SCORE = 0
HRAC2_SCORE = 0

pygame.init()
FONT_SCORE = pygame.font.Font(None, 74)

# Počiatočné skóre
SCORE = [0, 0]