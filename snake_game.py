import pygame
import random
import os
# from PIL import Image

pygame.mixer.init()
pygame.init()

screen_width = 1250
screen_height = 600

game_window = pygame.display.set_mode((screen_width,screen_height))
# bckground image-->

img = pygame.image.load("ws_Beautiful_green_field_1920x1200.jpg")
img = pygame.transform.scale(img , (screen_width , screen_height)).convert_alpha()

fps = 30
clock = pygame.time.Clock()

white = (255,255,255)
red =  (255,0,0)
green = (0,255,0)
black = (0,0,0)


pygame.display.set_caption("Classic_Snake")
pygame.display.update()
 
font = pygame.font.SysFont(None,55)

def print_text(text,color,x,y):
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window,color , snake_list,snake_size):
    for x , y in snake_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window = pygame.display.set_mode((screen_width,screen_height))
        f_img = pygame.image.load("maxresdefault.jpg")
        game_window.blit(f_img,(0,0))
        f_img = pygame.transform.scale(f_img , (screen_width , screen_height)).convert_alpha()
        
        # pygame.mixer.music.load("15-Seconds-2020-01-19_-_Shake_It_Up_-_FesliyanStudios.com_-_David_Renda.mp3")
        # pygame.mixer.music.play()
        print_text("Welcome to Snakes",green,350,250)
        print_text("Press Space Bar to play",green ,330 , 300 )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
            
        pygame.display.update()
        clock.tick(fps)

def winner(h_score , exit_game):
    color = (25,15 ,5)
    color1 = (140,210,120)
    color2 = (45,45,45)

    with open("highscore.txt" , "w") as f:
        f.write(str(h_score))

    # pygame.mixer.music.load("15-Seconds-2020-01-19_-_Shake_It_Up_-_FesliyanStudios.com_-_David_Renda.mp3")
    # pygame.mixer.music.play()

    game_window.fill(color)
    print_text("Congrats...!!" , color1 , 450 , 350 )
    print_text("NEW HIGH SCORE", color1 , 400 , 300 )
    print_text("Score:" + str(h_score) , color2 , 490 , 400 )
    print_text("Press Enter to Continue...!!" , color1 , 700 , 500 )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_RETURN:
                welcome()

    pygame.display.update()
    clock.tick(fps)

def the_end(h_score , exit_game):
    my_color = (255,200,150)
    game_window = pygame.display.set_mode((screen_width,screen_height))
    l_img = pygame.image.load("losted.jpg")
    game_window.blit(l_img,(0,0))
    print_text("Your Score : "+ str(h_score)  ,my_color,150,300)
    print_text(".Oops..!! Game Over" , my_color , 200 , 350)
    print_text("Press 'Enter' to play again..." , my_color , 250,400)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_RETURN:
                welcome()
    pygame.display.update()
    clock.tick(fps)

            
def game_loop():

    game_over = False
    exit_game = False
    
    score = 0
    border = 0
    border_x = 1150
    border_y = 700
    border_size = 1
    snake_x = 350
    snake_y = 225
    snake_size = 8

    init_velocity = 5
    velocity_x = 0
    velocity_y = 0

    snake_list = []
    snake_length = 1

# check whether highscore file exist -->

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt" , "w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        highscore = f.read()

    food_x = random.randint(300,screen_width-50)
    food_y = random.randint(300,screen_height-50)

    while not exit_game:
        if game_over:
            exit_game = False

            if int(score) >= int(highscore):
                winner(highscore , exit_game)
            else:
                the_end(score , exit_game)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
 
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        velocity_x += 7
                        velocity_y = 0


                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y += 7

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        velocity_x -= 7
                        velocity_y = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        velocity_x = 0
                        velocity_y -= 7

                    if event.key == pygame.K_SPACE:
                        snake_x = velocity_x
                        snake_y = velocity_y
                        velocity_x = 0
                        velocity_y = 0

                # my cheat code
                    if event.key == pygame.K_l:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                pygame.mixer.music.load('eat.mp3')
                pygame.mixer.music.play()
                score += 10
                food_x = random.randint(300,screen_width-100)
                food_y = random.randint(300,screen_height-100)
                snake_length += 2
                if score > int(highscore):
                    highscore = score

            game_window.fill(white)
            game_window.blit(img,(0,0))
            
            if border == 0:
                border = 1
                pygame.draw.rect(game_window,black,[border_x , border_y , border_size, border_size])
            print_text("score:" + str(score) + "  HighScore : " + str(highscore),red,5,5)
            pygame.draw.rect(game_window, red , [food_x , food_y ,  snake_size , snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('hit-out.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('hit-out.mp3')
                pygame.mixer.music.play()

            plot_snake(game_window,black,snake_list , snake_size )

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()