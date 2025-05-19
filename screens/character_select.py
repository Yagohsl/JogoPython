import pygame
import sys
from data.screen import SCREEN, SCREEN_HEIGHT
from data.colors import WHITE, YELLOW
from data.avaliable_caracters import AVALIABLE_CARACTERS
from fighters.fighterPlayer import FighterPlayer
from utils.fonts import get_font
from utils.draw import draw_text

def character_select(game_state):
    selected = []
    background = pygame.image.load("assets/images/menu/fundo_selecao.png")
    waiting_for_mouse_release = True

    while True:
        SCREEN.blit(background, (0, 0))
        draw_text("Selecione os Personagens (Clique nos dois)", get_font(25), WHITE, 200, 50)
        mouse_pos = pygame.mouse.get_pos()
        x = 150
        
        # Loop para renderização de possiveis personagens
        for key, data in AVALIABLE_CARACTERS.items():
            image_scaled = pygame.transform.scale(data["icon"], (150, 250))
            rect = image_scaled.get_rect(center=(x, SCREEN_HEIGHT//2))
            SCREEN.blit(image_scaled, rect.topleft)

            draw_text(data["name"], get_font(20), WHITE, x, rect.bottom)
            x += 250

            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(SCREEN, YELLOW, rect, 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for key, data in AVALIABLE_CARACTERS.items():
                    image_scaled = pygame.transform.scale(data["icon"], (150, 250))
                    rect = image_scaled.get_rect(center=(150 + list(AVALIABLE_CARACTERS.keys()).index(key) * 250, SCREEN_HEIGHT//2))
                    if rect.collidepoint(event.pos):
                        if key not in selected:
                            selected.append(key)

        if len(selected) == 2:
                # Construindo lutadores
                char_config = AVALIABLE_CARACTERS[selected[0]]
                game_state["player1"] = FighterPlayer(
                    name=char_config["name"],animation_steps=char_config["animation_steps"],
                    sprite_sheet=char_config["sheet_path"],icon=char_config["icon"],
                    data=char_config["data"],player=1,x=200,y=310,flip=False)
                
                char_config = AVALIABLE_CARACTERS[selected[1]]
                game_state["player2"] = FighterPlayer(
                    name=char_config["name"],animation_steps=char_config["animation_steps"],
                    sprite_sheet=char_config["sheet_path"],icon=char_config["icon"],
                    data=char_config["data"], player=2, x=700, y=310, flip=True)
                
                return  # Avança para a próxima tela

        pygame.display.update()