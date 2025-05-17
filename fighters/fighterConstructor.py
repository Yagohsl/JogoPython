import pygame
from fighters.fighterPlayer import FighterPlayer;

class FighterConstructor():
    def Anakin(player, position_x, position_y, flip):
        animation_steps = [3, 8, 1, 8, 8, 3, 7, 5, 3] #usando metade dos ataques
        sheet = pygame.image.load("assets/images/jogo/fighters/general.png").convert_alpha()
        icon = pygame.image.load("assets/images/jogo/fighters/icons/fighter1.png").convert_alpha()
        name = "Anakin Skywalker"
        data = [162, 3, [72,40]] #size, scale, offset
        return FighterPlayer(player, position_x, position_y, flip, data, sheet, animation_steps, name, icon)
    
    def Obiwan(player, position_x, position_y, flip):
        animation_steps = [8, 8, 1, 8, 8, 3, 7, 5, 4]
        sheet = pygame.image.load("assets/images/jogo/fighters/fighter2.png").convert_alpha()
        icon = pygame.image.load("assets/images/jogo/fighters/icons/fighter2.png").convert_alpha()
        data = [250, 3, [112, 106]] #size, scale, offset
        name = "Obi-Wan Kenobi"
        return FighterPlayer(player, position_x, position_y, flip, data, sheet, animation_steps, name, icon)
    
    def General(player, position_x, position_y, flip):
        animation_steps = [8, 8, 1, 8, 8, 3, 7, 5, 4]
        sheet = pygame.image.load("assets/images/jogo/fighters/general.png").convert_alpha()
        icon = pygame.image.load("assets/images/jogo/fighters/icons/fighter2.png").convert_alpha()
        data = [250, 3, [112, 106]] #size, scale, offset
        name = "Grievous"
        return FighterPlayer(player, position_x, position_y, flip, data, sheet, animation_steps, name, icon)
    
    def Female_jedi(player, position_x, position_y, flip):
        animation_steps = [8, 8, 1, 8, 8, 3, 7, 5, 4]
        sheet = pygame.image.load("assets/images/jogo/fighters/female_jedi_spritesheet").convert_alpha()
        icon = pygame.image.load("assets/images/jogo/fighters/icons/fighter2.png").convert_alpha()
        data = [250, 3, [112, 106]] #size, scale, offset
        name = "Maria Jedi"
        return FighterPlayer(player, position_x, position_y, flip, data, sheet, animation_steps, name, icon)