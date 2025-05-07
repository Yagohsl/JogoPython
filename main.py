import pygame, sys
from button import Button
from pygame import mixer
from fighter import Fighter

mixer.init()
pygame.init()

#tela de jogo
screen_widht = 1000
screen_heigth = 600

icone = pygame.image.load ("assets/images/icons/icone.ico")
pygame.display.set_icon(icone)

screen = pygame.display.set_mode((1000, 600))

screen = pygame.display.set_mode((screen_widht, screen_heigth))
pygame.display.set_caption("Star Jedi Battleforce")

#velocidade de freimes
clock = pygame.time.Clock()
FPS = 60

#definindo cores
red = (247,93,0)
yellow = (0, 255, 255)
white = (255, 255, 255)

def jogo(): 
  #variaveis do jogo
  intro_count = 3
  last_count_update = pygame.time.get_ticks()
  score = [0, 0]
  round_over = False
  round_over_cooldown = 2000

  #lutador 1
  fighter1_size = 162
  fighter1_scale = 3
  fighter1_offset = [72, 40]
  fighter1_data = [fighter1_size, fighter1_scale, fighter1_offset]
  
  #lutador 2
  fighter2_size = 250
  fighter_scale = 3
  fighter_offset = [112, 106]
  fighter_data = [fighter2_size, fighter_scale, fighter_offset]

  #musicas e sons
  pygame.mixer.music.load("assets/audio/music.mp3")
  pygame.mixer.music.set_volume(0.5)
  pygame.mixer.music.play(-1, 0.0, 5000)
  sword_fx = pygame.mixer.Sound("assets/audio/sword.mp3")
  sword_fx.set_volume(2.0)
  sword2_fx = pygame.mixer.Sound("assets/audio/sword2.mp3")
  sword2_fx.set_volume(0.3)

  #imagens
  bg_image = pygame.image.load("assets/images/jogo/background.png").convert_alpha()
  versus_image = pygame.image.load("assets/images/icons/versus.png").convert_alpha()
  player1_icon = pygame.image.load("assets/images/icons/fighter1.png").convert_alpha()
  player2_icon = pygame.image.load("assets/images/icons/fighter2.png").convert_alpha()
  figther1_sheet = pygame.image.load("assets/images/jogo/fighter1.png").convert_alpha()
  fighter2_sheet = pygame.image.load("assets/images/jogo/fighter2.png").convert_alpha()
  victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

  #velocidade de animacao
  fighter1_animation_steps = [10, 8, 1, 7, 7, 3, 7, 5]
  fighter2_animation_steps = [8, 8, 1, 8, 8, 3, 7, 5]

  #fonte
  count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
  score_font = pygame.font.Font("assets/fonts/turok.ttf", 25)
  name_font = pygame.font.Font("assets/fonts/turok.ttf", 25)

  #texto
  def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

  #background
  def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_widht, screen_heigth))
    screen.blit(scaled_bg, (0, 0))

  #barra de vida
  def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, white, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, red, (x, y, 400, 30))
    pygame.draw.rect(screen, yellow, (x, y, 400 * ratio, 30))


  #introduzindo lutadores
  fighter_1 = Fighter(1, 200, 310, False, fighter1_data, figther1_sheet, fighter1_animation_steps, sword_fx)
  fighter_2 = Fighter(2, 700, 310, True, fighter_data, fighter2_sheet, fighter2_animation_steps, sword2_fx)

  #redimensionando imagem
  player1_icon = pygame.transform.scale(player1_icon, (player1_icon.get_width() // 5, player1_icon.get_height() // 5))
  player2_icon = pygame.transform.scale(player2_icon, (player2_icon.get_width() // 5, player2_icon.get_height() // 5))
  versus_image = pygame.transform.scale(versus_image, (versus_image.get_width() // 3, versus_image.get_height() // 3))
  
  #loop
  run = True
  while run:
    
    clock.tick(FPS)
    #background
    draw_bg()
   
    #icones
    screen.blit(player1_icon, (20, 5))
    screen.blit(player2_icon, (890, 5))
    screen.blit(versus_image, (410, 40))

    #status de jogador
    draw_health_bar(fighter_1.health, 20, 100)
    draw_health_bar(fighter_2.health, 580, 100)

    #inserindo nomes
    draw_text("anakin skywalker ", name_font, white, 110, 50)
    draw_text("obi-wan kenobi" , name_font, white, 660, 50)
    draw_text("p1: " + str(score[0]), score_font, white, 20, 130)
    draw_text("p2: " + str(score[1]), score_font, white, 580, 130)

    #recontagem
    if intro_count <= 0:
      fighter_1.move(screen_widht, screen_heigth, screen, fighter_2, round_over)
      fighter_2.move(screen_widht, screen_heigth, screen, fighter_1, round_over)
    else:
      #temporizador de contagem
      draw_text(str(intro_count), count_font, white, screen_widht / 2, screen_heigth / 3)
      if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()
        
    #atualizando
    fighter_1.update()
    fighter_2.update()
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #verificando derrota
    if round_over == False:
      if fighter_1.alive == False:
        score[1] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
      elif fighter_2.alive == False:
        score[0] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
    else:
      #exibir vitoria
      screen.blit(victory_img, (360, 150))


      #acaba jogo
      if score[0] == 2 or score[1] == 2:
        if pygame.time.get_ticks() - round_over_time > round_over_cooldown:
          round_over = True
          round_over_time = pygame.time.get_ticks()
          screen.blit(victory_img, (360, 150))

          main_menu()

      if pygame.time.get_ticks() - round_over_time > round_over_cooldown:
        round_over = False
        intro_count = 3
        fighter_1 = Fighter(1, 200, 310, False, fighter1_data, figther1_sheet, fighter1_animation_steps, sword_fx)
        fighter_2 = Fighter(2, 700, 310, True, fighter_data, fighter2_sheet, fighter2_animation_steps, sword2_fx)
      
         
    #manipulando eventos
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.mixer.music.pause()
          main_menu()
  


    pygame.display.update()

#Menu do jogo
BG = pygame.image.load("assets/images/menu/FUNDO MENU.png")
BGcredito = pygame.image.load("assets/images/menu/FUNDO CREDITO.png")


def get_font(size):
    return pygame.font.Font("assets/fonts/Starjedi.ttf", size)


def play():
    run = True
    while run:
       
       

        screen.blit(jogo())



        pygame.display.update()
    
def options():
    while True:
        
        mouse_pos_cred = pygame.mouse.get_pos()

        screen.blit(BGcredito, (0, 0))
        

        cred_text = get_font(30).render("", True, "white")
        cred_rect = cred_text.get_rect(center=(500, 260))
        screen.blit(cred_text, cred_rect)

        cred_back = Button(image=pygame.image.load("assets/images/menu/voltar.png"), pos=(500, 460), 
                            text_input="", font=get_font(75), base_color="Black", hovering_color="Green")

        cred_back.changeColor(mouse_pos_cred)
        cred_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cred_back.checkForInput(mouse_pos_cred):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.mixer.music.load("assets/audio/musicmenu.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)
    while True:
        
        screen.blit(BG, (0, 0))
        

        mouse_pos_menu = pygame.mouse.get_pos()

        menu_text = get_font(100).render("", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load("assets/images/menu/jogar.png"), pos=(850, 200), 
                            text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="white")
        cred_button = Button(image=pygame.image.load("assets/images/menu/creditos.png"), pos=(850, 325), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
        sair_button = Button(image=pygame.image.load("assets/images/menu/sair.png"), pos=(850, 450), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="white")

        screen.blit(menu_text, menu_rect)
        
        

        for button in [play_button, cred_button, sair_button]:
            button.changeColor(mouse_pos_menu)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
              if event.key == pygame.K_RETURN:
                play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos_menu):
                    play()
                if cred_button.checkForInput(mouse_pos_menu):
                    options()
                if sair_button.checkForInput(mouse_pos_menu):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
input()
pygame.quit()