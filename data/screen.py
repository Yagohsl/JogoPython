import pygame
from data.colors import RED,WHITE, YELLOW

SCREEN_WIDTH = 1000
SCREEN_HEIGHT =  600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60

VERSUS_IMAGE = pygame.image.load("assets/images/jogo/icons/versus.png").convert_alpha()
VERSUS_IMAGE= pygame.transform.scale(VERSUS_IMAGE, (VERSUS_IMAGE.get_width() // 3, VERSUS_IMAGE.get_height() // 3))
VICTORY_IMAGE = pygame.image.load("assets/images/jogo/icons/victory.png").convert_alpha()


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(SCREEN, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(SCREEN, RED, (x, y, 400, 30))
    pygame.draw.rect(SCREEN, YELLOW, (x, y, 400 * ratio, 30))