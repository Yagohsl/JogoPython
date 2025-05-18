import pygame, sys

from buttons.button import Button
from data.screen import SCREEN, SCREEN_WIDTH

def credit_screen():
    background = pygame.image.load("assets/images/menu/FUNDO CREDITO.png")
    exit_button = Button(image=pygame.image.load("assets/images/menu/sair.png"), pos=(SCREEN_WIDTH//2.5, 450))
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.blit(background, (0, 0))
        exit_button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.checkForInput(mouse_pos):
                        return
        pygame.display.update()