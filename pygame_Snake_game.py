

# # snake game



import pygame
import random
import os




pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green=(0,100,0)
dark=(173,255,47)
org=(102,51,0)

change_to="RIGHT"
direction="RIGHT"

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#image
bgimg=pygame.image.load("snakeimg.png")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_width)).convert_alpha()



# Game Title
pygame.display.set_caption("Snake game")
gameWindow.fill(green)
pygame.display.update()

# Game specific variables

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome_screen():
    exit=False
    
    while not exit:
        gameWindow.fill((23,206,219))
        gameWindow.blit(bgimg,(0,0))
        text_screen("Press Space to play",org,201,20)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                exit=True
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    
                    game_loop()
                    
                

        pygame.display.update()    
        clock.tick(60)
# Game Loop
def game_loop():
    global change_to,direction
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(30, screen_width/2)
    food_y = random.randint(30, screen_height/2)
    score = 0
    init_velocity = 3
    snake_size = 20
    fps = 60
    if (not os.path.exists("snake_score.txt")):
        with open("snake_score.txt","w") as f:
            f.write("0")
        
    with open("snake_score.txt","r") as f:
        hiscore=int(f.read())
    while not exit_game:
        if game_over:
            with open("snake_score.txt","w") as f:
                f.write(str(hiscore))
                
                
                
            gameWindow.fill(white)
            text_screen("Game Over! press enter to continue",red,100,screen_height/2)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        
                        welcome_screen()
                        
        
            
            
            
            
            
            
        else: 


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        change_to="RIGHT"
                        
                        

                    if event.key == pygame.K_LEFT:
                        change_to="LEFT"
                        
                        

                    if event.key == pygame.K_UP:
                        change_to="UP"
                        

                    if event.key == pygame.K_DOWN:
                        change_to="DOWN"
                        
                        

                        
                        
                        
                        
                        
            if change_to=="UP" and direction!="DOWN":
                direction="UP"
                
                
            elif change_to=="DOWN" and direction!="UP":
                
                direction="DOWN"
            elif change_to=="RIGHT" and direction!="LEFT":
                direction="RIGHT"
                
            elif change_to=="LEFT" and direction!="RIGHT":
                direction="LEFT"
                
                
                
                
                
            if direction=="UP":
                
                velocity_y = - init_velocity
                velocity_x = 0
            elif direction=="DOWN":
                velocity_y = init_velocity
                velocity_x = 0
                
            elif direction=="RIGHT":
                velocity_x = init_velocity
                velocity_y = 0
            elif direction=="LEFT":
                velocity_x = - init_velocity
                velocity_y = 0
                
                
                
                
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<9 and abs(snake_y - food_y)<9:
                score +=10
                food_x = random.randint(100, screen_width / 2)
                food_y = random.randint(100, screen_height / 2)
                snk_length +=1.5
                init_velocity+=0.1
                color=black
                if score>hiscore:
                    hiscore=score
            gameWindow.fill(green)
            text_screen("Score: " + str(score) +"Hiscore: "+str(hiscore), white, 5, 5)
            pygame.draw.circle(gameWindow, red, [food_x, food_y], 10, 0)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over=True
            
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            plot_snake(gameWindow, dark, snk_list, snake_size)
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome_screen()


# In[ ]:




