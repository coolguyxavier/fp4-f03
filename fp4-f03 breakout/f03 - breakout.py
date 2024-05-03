# - FP4-F03 Full Pygame Option #3, Breakout - #
# - Xzavier Moosomin - #
# - 05/02/2024 - #

# - Developer Notes - #
# i might just copy over some previous code from FP4-F02 since its already made
# for the paddle
# since the rectangle and the paddle are similar
# just need to have it set to a certain y value

# - Imports - #

import pygame

from paddle import Paddle
from ball import Ball
from brick import Brick

# - Pygame Initialization - #
pygame.init()

# - Constants - #

white = (255, 255, 255)
darkblue = (36, 90, 190)
lightblue = (0, 176, 240)
red = (255, 0, 0)
orange = (255, 100, 0)
yellow = (255, 255, 0)

# - Variables - #

score = 0
lives = 3

carryOn = True

# ============ Game Settings ============= #

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout!")

clock = pygame.time.Clock()

# - Sprite List -#

all_sprites_list = pygame.sprite.Group()

# - Create Sprites - #

paddle = Paddle(lightblue, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(red, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
    
for i in range(7):
    brick = Brick(orange, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
    
for i in range(7):
    brick = Brick(yellow, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
    
# add sprites to group
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# =============== Main Code ================= #

while carryOn:
    # ---- Main Event Loop ---- #
    for event in pygame.event.get(): # user does an action
        if event.type == pygame.QUIT: # user clicks quit
            carryOn = False # stops program
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x: # pressing the x key will exit game
                carryOn = False
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
            
    # ---- Game Logic ---- #
    all_sprites_list.update()
    
    # if ballcolor touches a wall, it bounces off it
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, white)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            
            carryOn = False # stops game
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
        
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()
        
    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, white)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            #Stop the Game
            carryOn=False
    
    # ---- Drawing Code ---- #
    screen.fill(darkblue)
    pygame.draw.line(screen, white, [0, 38], [800, 38], 2)
    
    # displays score and lives at top of screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (650, 10))
    
    all_sprites_list.draw(screen) # draws all sprites
    
    pygame.display.flip()
    
    
    clock.tick(60) # caps fps to 60 (not optimal)
    
pygame.quit() # exits program