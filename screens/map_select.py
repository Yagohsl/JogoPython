import pygame, sys
from data.Maps import MAPS
from data.colors import WHITE, YELLOW
from data.screen import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH

from utils.fonts import get_font
from utils.draw import draw_text


def map_select_screen(game_state):
    background = pygame.image.load("assets/images/menu/fundo_selecao.png")
    map_images = {key: pygame.image.load(data["imagem"]) for key, data in MAPS.items()}

    while True:
        SCREEN.blit(background, (0, 0))
        draw_text("Selecione o Mapa", get_font(30), WHITE, SCREEN_HEIGHT//1.8, 50)
        mouse_pos = pygame.mouse.get_pos()

        x = 200
        for key, data in MAPS.items():
            image_scaled = pygame.transform.scale(map_images[key], (300, 190))
            rect = image_scaled.get_rect(center=(x, SCREEN_HEIGHT//2))
            SCREEN.blit(image_scaled, rect.topleft)
            draw_text(data["nome"], get_font(20), WHITE, x-50, rect.bottom)
            x += 250

            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(SCREEN, YELLOW, rect, 3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for key, data in MAPS.items():
                        image_scaled = pygame.transform.scale(map_images[key], (150, 250))
                        rect = image_scaled.get_rect(center=(150 + list(MAPS.keys()).index(key) * 250, SCREEN_HEIGHT//2))
                        if rect.collidepoint(event.pos):
                            pygame.time.wait(300)
                            game_state["selected_map"] = map_images[key]
                            return


        pygame.display.update()
