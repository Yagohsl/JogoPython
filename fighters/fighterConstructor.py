import pygame
from fighters.fighter import Fighter
from fighters.fighter_player import FighterPlayer;

class FighterConstructor():
    def Anakin():
        fighter1_animation_steps = [3, 8, 1, 8, 8, 3, 7, 5, 3] #usando metade dos ataques
        figther1_sheet = pygame.image.load("assets/images/jogo/fighters/fighterAnakin.png").convert_alpha()
        player1_icon = pygame.image.load("assets/images/jogo/fighters/icons/fighter1.png").convert_alpha()
        fighter1_data = [162, 3, [72,40]] #size, scale, offset
        return Fighter(1, 200, 310, False, fighter1_data, figther1_sheet, fighter1_animation_steps)
    
    def Obiwan():
        fighter2_animation_steps = [8, 8, 1, 8, 8, 3, 7, 5, 4]
        fighter2_sheet = pygame.image.load("assets/images/jogo/fighters/fighter2.png").convert_alpha()
        player2_icon = pygame.image.load("assets/images/jogo/fighters/icons/fighter2.png").convert_alpha()
        fighter_data = [250, 3, [112, 106]] #size, scale, offset
        return Fighter(2, 700, 310, True, fighter_data, fighter2_sheet, fighter2_animation_steps)
    
    def General():
        fighter2_animation_steps = [8, 8, 1, 8, 8, 3, 7, 5, 4]
        fighter2_sheet = pygame.image.load("assets/images/jogo/fighters/general.png").convert_alpha()
        player2_icon = pygame.image.load("assets/images/jogo/fighters/icons/fighter2.png").convert_alpha()
        fighter_data = [250, 3, [112, 106]] #size, scale, offset
        return Fighter(2, 700, 310, True, fighter_data, fighter2_sheet, fighter2_animation_steps)
    
    def Female_jedi():
        fighter2_animation_steps = [8, 8, 1, 8, 8, 3, 7, 5, 4]
        fighter2_sheet = pygame.image.load("assets/images/jogo/fighters/female_jedi_spritesheet").convert_alpha()
        player2_icon = pygame.image.load("assets/images/jogo/fighters/icons/fighter2.png").convert_alpha()
        fighter_data = [250, 3, [112, 106]] #size, scale, offset
        return Fighter(2, 700, 310, True, fighter_data, fighter2_sheet, fighter2_animation_steps)