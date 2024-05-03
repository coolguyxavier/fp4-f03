# - FP4-F03 Option 3, Breakout - #
# - Xzavier Moosomin - #
# - 05/02/2024 - #

# - Imports - #

import pygame

# - Constants - #
black = (0,0,0)

# - Classes - #

class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # checks so that the paddle isnt off screen
        if self.rect.x < 0:
            self.rect.x = 0
        
    def moveRight(self, pixels):
        self.rect.x += pixels
        # checks so isnt off screen
        if self.rect.x > 700:
            self.rect.x = 700
        