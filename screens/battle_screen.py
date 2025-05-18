import pygame, sys
from data.screen import SCREEN

class BattleScreen:
    def __init__(self, game_state):
        context = game_state
        self.fighter1 = context["player1"]
        self.fighter2 = context["player2"]
        self.background = context["selected_map"]

    def run(self):
        clock = pygame.time.Clock()
        while True:
            SCREEN.blit(self.background, (0, 0))

            # Atualiza lógica dos personagens aqui (a implementar)
            self.fighter1.draw(SCREEN)
            self.fighter2.draw(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            clock.tick(60)
