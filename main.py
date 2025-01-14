import pygame
import sys
import random
from Config import config

def move_player(player, keys):
    """Funkcia rieši pohyb hráča nahor alebo nadol"""
    if keys[pygame.K_UP]:
        if player.top > 0:
            player.top -= config.STEP

    if keys[pygame.K_DOWN]:
        if player.bottom < config.ROZLISENIE[1]:
            player.bottom += config.STEP

def move_ai(player, ball):
    """Funkcia riadi pohyb AI hráča nahor alebo nadol"""
    target_y = ball.centery  # Cieľová výška lopty pre AI
    if abs(player.centery - target_y) > config.STEP:  # Kontrola, či je potrebné sa pohnúť
        if player.centery < target_y and player.bottom < config.ROZLISENIE[1]:
            player.top += config.STEP * 1.5  # Pohyb nadol
        elif player.centery > target_y and player.top > 0:
            player.top -= config.STEP * 1.5  # Pohyb nahor

def check_collision(ball, player):
    """Kontrola kolízie lopty s hráčom a odrazenie lopty"""
    if ball.colliderect(player):
        return True
    return False

def draw_score(window, font, score):
    """Funkcia na vykreslenie skóre"""
    text = font.render(f"{score[0]} : {score[1]}", True, (255, 255, 255))
    window.blit(text, (config.ROZLISENIE[0] // 2 - text.get_width() // 2, 20))

def game_over(score):
    """Funkcia zistí, či je hra ukončená"""
    return abs(score[0] - score[1]) >= 2 and max(score) >= 15

if __name__ == "__main__":
    pygame.init()

    window = pygame.display.set_mode(config.ROZLISENIE)
    pygame.display.set_caption("Volejbal")

    clock = pygame.time.Clock()

    # Inicializácia fontu
    font = pygame.font.Font(None, 50)

    hrac1 = pygame.Rect(config.ROZLISENIE[0] - 110, config.ROZLISENIE[1] // 2 - 50, 10, 100)
    hrac2 = pygame.Rect(110, config.ROZLISENIE[1] // 2 - 50, 10, 100)

    lopta = pygame.Rect(config.ROZLISENIE[0] / 2 - 10, config.ROZLISENIE[1] / 2 - 10, 20, 20)

    rychlost_lopty_x = random.choice([1, -1]) * 4
    rychlost_lopty_y = random.choice([1, -1]) * 4

    # Počiatočné skóre
    score = config.SCORE

    game_over_flag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        move_player(hrac1, keys)
        move_ai(hrac2, lopta)

        if not game_over_flag:
            if lopta.top <= 0 or lopta.bottom >= config.ROZLISENIE[1]:
                rychlost_lopty_y *= -1

            if lopta.left <= 0:
                score[1] += 1
                lopta.center = (config.ROZLISENIE[0] / 2, config.ROZLISENIE[1] / 2)
                rychlost_lopty_x *= random.choice([1, -1])
                rychlost_lopty_y *= random.choice([1, -1])

            if lopta.right >= config.ROZLISENIE[0]:
                score[0] += 1
                lopta.center = (config.ROZLISENIE[0] / 2, config.ROZLISENIE[1] / 2)
                rychlost_lopty_x *= random.choice([1, -1])
                rychlost_lopty_y *= random.choice([1, -1])

            if lopta.colliderect(hrac1) or lopta.colliderect(hrac2):
                rychlost_lopty_x *= -1

            lopta.x += rychlost_lopty_x
            lopta.y += rychlost_lopty_y

        window.fill(config.FARBA_POZADIA)

        pygame.draw.rect(window, "white", hrac1)
        pygame.draw.rect(window, "white", hrac2)
        pygame.draw.circle(window, config.FARBA_LOPTY, lopta.center, config.POLOMER_LOPTY)

        # Vykreslenie skóre
        draw_score(window, font, score)

        # Kontrola konca hry
        if game_over(score):
            game_over_flag = True
            text_end = font.render("Game Over", True, (255, 255, 255))
            window.blit(text_end, (config.ROZLISENIE[0] // 2 - text_end.get_width() // 2, config.ROZLISENIE[1] // 2 - text_end.get_height() // 2))

        pygame.display.update()
        clock.tick(config.FPS)
