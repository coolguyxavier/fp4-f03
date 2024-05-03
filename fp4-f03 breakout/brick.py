# - FP4-F03 Pygame Option 3-Breakout - #
# - Xzavier Moosomin - #
# - 05/03/2024 - #

# - Imports - #

import pygame

# - Constants -#

black = (0,0,0)

# - Classes - #

class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and make it transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # create brick
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()