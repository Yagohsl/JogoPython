import pygame, sys
from data.screen import SCREEN
from buttons.button import Button
from screens.credit_screen import credit_screen

class MenuScreen:
    def __init__(self):
        self.play_button = Button(image=pygame.image.load("assets/images/menu/jogar.png"), pos=(850, 200))
        self.credits_button = Button(image=pygame.image.load("assets/images/menu/creditos.png"), pos=(850, 325))
        self.exit_button = Button(image=pygame.image.load("assets/images/menu/sair.png"), pos=(850, 450))
        self.background = pygame.image.load("assets/images/menu/FUNDO MENU.png")

        pygame.mixer.music.load("assets/audio/musicmenu.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.play(-1)

    def run(self):
        while True:
            SCREEN.blit(self.background, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            for button in [self.play_button, self.credits_button, self.exit_button]:
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(mouse_pos):
                        pygame.time.delay(1000)
                        return
                    if self.credits_button.checkForInput(mouse_pos):
                        credit_screen()
                    if self.exit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        sys.exit()
                        
            pygame.display.update()