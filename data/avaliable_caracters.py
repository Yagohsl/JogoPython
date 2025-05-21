import pygame

#Dados dos personagens
AVALIABLE_CARACTERS = {
        "Anakin": {
            "name": "Anakin Skywalker",
            "animation_steps": [3, 8, 1, 8, 8, 3, 7, 5, 3],
            "sheet_path": pygame.image.load("assets/images/jogo/fighters/fighterAnakin.png"),
            "icon": pygame.image.load("assets/images/jogo/fighters/icons/anakin.png"),
            "data": [162, 3, [72, 40]]
        },
        "Obiwan": {
            "name": "obi-Wan Kenobi",
            "animation_steps": [8, 8, 1, 8, 8, 3, 7, 5, 4],
            "sheet_path": pygame.image.load("assets/images/jogo/fighters/fighter2.png"),
            "icon": pygame.image.load("assets/images/jogo/fighters/icons/obiwan.png"),
            "data": [250, 3, [112, 106]]
        },
        "General": {
            "name": "General Grievous",
            "animation_steps": [3, 8, 1, 8, 8, 3, 7, 5, 3],
            "sheet_path": pygame.image.load("assets/images/jogo/fighters/general.png"),
            "icon": pygame.image.load("assets/images/jogo/fighters/icons/general_grevious_icon.png"),
            "data": [162, 3, [72, 40]]
        },
        "Female_Jedi": {
            "name": "Maria Jedi Sousa",
            "animation_steps": [5, 10, 1, 8, 8, 3, 7, 5, 3],
            "sheet_path": pygame.image.load("assets/images/jogo/fighters/female_jedi.png"),
            "icon": pygame.image.load("assets/images/jogo/fighters/icons/maria_jedi_icon.png"),
            "data": [162, 3, [72, 40]]
        }, 
        "Mestre Diogo": {
            "name": "Mestre Diogo Robles",
            "animation_steps": [5, 12, 1, 8, 8, 3, 7, 5, 3,8],
            "sheet_path": pygame.image.load("assets/images/jogo/fighters/mestre_diogo.png"),
            "icon": pygame.image.load("assets/images/jogo/fighters/icons/maria_jedi_icon.png"),
            "data": [162, 3, [72, 40]]
        }
    }
