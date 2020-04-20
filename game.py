import pygame
import helicopter
import enemy_heli
import boat
import sprites
import random

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.display.set_icon(sprites.icon)
display_width = 800
display_height = 600
game.display = pygame.display.set_mode((display_width, display_height))


font = "8-bit-Madness.ttf"
def message_to_screen(message, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, 0, color)
    return my_message


white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


for convert_sprites in sprites.all_sprites:
    convert_sprites.convert_alpha()

clock = pygame.time.Clock()
FPS = 30

player = helicopter.Helicopter = open(100, display_height/2 - 40)
moving = True
godmove = False

score = 0
highscore_file = open('highscore.dat', "r")
highscore_int = int(highscore_file.read())

cloud_x = 800
cloud_y = random.randint(0, 400)

enemy_heli = enemy_heli.EnemyHeli(-100, display_height/2 - 40)
enemy_heli_alive = False

boat = boat.Boat(-110, 430)
boat_alive = False

spaceship_x 800
spaceship_y = random.randint(0, 400)
spaceship_alive = False
spaceship_hit_player = False
warning_once = True
warning = False
warning_counter = 0
warning_message = message_to_screen("!", font, 200, red)

ballon_x = 800
ballon_y = random.randint(0, 400)

bullets = []

bombs = []

shoot = pygame.mixer.sound('sounds/shoot.wav')
pop = pygame.mixer.sound('sounds/pop.wav')
bomb = pygame.mixer.sound('sounds/bomb.wav')
explosion = pygame.mixer.sound('sounds/explosion.wav')
explosion2 = pygame.mixer.sound('sounds/explosion2.wav')
select = pygame.mixer.sound('sounds/select.wav')
select2 = pygame.mixer.sound('sounds/select2.wav')
whoosh = pygame.mixer.sound('sounds/whoosh.wav')


def main_menu():
    global cloud_x
    global cloud_y

    menu = True

    selected = "play"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    pygame.mixer.Sound.play(select)
                    selected = "play"

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pygame.mixer.Sound.play(select)
                    selected = "quit"
                
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(select2)
                    if selected == "play":
                        menu = "False"
                    if selected == "quit":
                        pygame.quit()
                        quit()
    game_display.blit(sprites.background, (0, 0))
    game_display.blit(sprites.cloud, (cloud_x, cloud_y))
    if cloud_x <= 800 - 1100:
        cloud_x = 800
        cloud_y = random.randint(0, 400)
    else:
        if not player.wreck_start:
            cloud_x -= 5
        if godmode:
            title = message_to_screen("HELICOPTERO (GODMODE)", font, 80, yellow)
        else:
            title = message_to_screen("HELICOPTERO", font, 100, black)
        controls_1 = message_to_screen("USE WASD PARA MOVER, SPACE PARA ATIRAR", font, 30, black)
        controls_2 = message_to_screen("USE SHIFT PARA JOGAR BOMBA, P PAUSAR", font, 30, black)
        
        if selected == "JOGAR":
            play = message_to_screen("JOGAR", font, 75, white)
        else:
            play = message_to_screen("JOGAR", font, 75, black)

        if selected == "SAIR":
            game_quit = message_to_screen("SAIR", font, 75, white)
        else:
            game_quit = message_to_screen("SAIR", font, 75, black)

            title_rect = title.get_rect()
            controls_1_rect = controls_1.get_rect()
            
            controls_2_rect = controls_2.get_rect()
            play_rect = play.get_rect()
            quit_rect = game_quit.get_rect()

            game_display.blit(title, (display_width/2 - (title_rect[2]/2), 40))

            game_display.blit(controls_1, (display_width/2 - (controls_1_rect[2]/2), 120))
            game_display.blit(controls_2, (display_width/2 - (controls_2_rect[2]/2), 140))
            game_display.blit(play, (display_width/2 - (play_rect[2]/2), 200))
            game_display.blit(game_quit, (display_width/2 - (game_quit[2]/2), 260))
            
            # Desenhando o oceano
            pygame.draw.rect(game_display, blue, (0, 500, 800, 100))

            # Atualizando a tela
            pygame.display.update()
            pygame.display.set_caption("VELOCIDADE DO HELICOPTERO" + str(int(clock.get_fps())) + "por segundo")
            clock.tick(FPS)

def pause():
    global highscore_file
    global highscore_int

    paused = True

    player.moving_up = False
    player.moving_left = False
    player.moving_down = False
    player.moving_right = False

    paused_text = message_to_screen("JOGO PARADO!", font, 100, black)
    paused_text_rect = paused_text.get_rect()
    game_display.blit(paused_text, (display_width / 2 - (paused_text_rect[2] / 2), 40))

    pygame.display.update()
    clock.tick(15)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if score > highscore_int:
                    if highscore_file = open('highscore.dat', "w")
                    highscore_file.write(str(score))
                    highscore_file.close()
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pygame.mixer.Sound.play(select)
                        paused = False
def game_loop():
    global spaceship_x
    global spaceship_y
    global spaceship_alive
    global spaceship_hit_player
    global warning
    global warning_counter
    global warning_once
    
    global bullets
    global moving
    
    global highscore_file
    global highscore_int
    global score
    
    global cloud_x
    global cloud_y

    global enemy_heli_alive
    global boat_alive

    game_exit = False
    game_over = False

    game_over_selected = "JOGAR NOVAMENTE"

    while not game_exit:
        while game_over:
            for event