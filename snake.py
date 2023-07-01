import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# bckground image-->

# img = pygame.image.load("snake.jpeg")
# img = pygame.transform.scale(img , (screen_width , screen_height)).convert_alpha()

fps = 30
clock = pygame.time.Clock()

white = (255,255,255)
red =  (255,0,0)
green = (0,255,0)
black = (0,0,0)

screen_width = 1250
screen_height = 600

game_window = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Classic_Snake")
pygame.display.update()
 
font = pygame.font.SysFont(None,55)

def game_score(text,color,x,y):
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window,color , snake_list,snake_size):
    for x , y in snake_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(black)
        game_score("Welcome to Snakes",green,350,250)
        game_score("Press Space Bar to play",green ,330 , 300 )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # pygame.mixer.music.load("")
                    # pygame.mixer.music.play("")
                    game_loop()
            
        pygame.display.update()
        clock.tick(fps)

def game_loop():

    game_over = False
    exit_game = False
    
    score = 0

    snake_x = 350
    snake_y = 225
    snake_size = 8

    init_velocity = 5
    velocity_x = 0
    velocity_y = 0

    snake_list = []
    snake_length = 1

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt" , "w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        highscore = f.read()


    food_x = random.randint(300,screen_width-50)
    food_y = random.randint(300,screen_height-50)

    while not exit_game:
        if game_over:
            with open("highscore.txt" , "w") as f:
                f.write(str(highscore))

            game_window.fill(black)
            game_score("Your Score : "+ str(score)  ,red,150,300)
            game_score(".Oops..!! Game Over" , red , 200 , 350)
            game_score("Press 'Enter' to play again..." , red , 250,400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key ==  pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        velocity_x += 7
                        velocity_y = 0

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        velocity_y += 7
                        velocity_x = 0

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        velocity_x -= 7
                        velocity_y = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        velocity_y -= 7
                        velocity_x = 0

                    if event.key == pygame.K_l:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(300,screen_width-100)
                food_y = random.randint(300,screen_height-100)
                snake_length += 2
                if score > int(highscore):
                    highscore = score

                if score == 100:
                    velocity_x += 2
                    velocity_y += 2


            game_window.fill(white)
            # game_window.blit(img)
            game_score("score:" + str(score) + "  HighScore : " + str(highscore),red,5,5)
            pygame.draw.rect(game_window, red , [food_x , food_y ,  snake_size , snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                print('score:',score)
                print("The End")
                game_over = True

            plot_snake(game_window,black,snake_list , snake_size )

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
# game_loop()