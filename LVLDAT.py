import pygame
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Level():
 
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.imageplatform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.end_list = pygame.sprite.Group()
        self.pushblock = pygame.sprite.Group()
        self.player = player
 
        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.world_height = 0
    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.imageplatform_list.update()
        self.end_list.update()
        self.enemy_list.update()
        #self.backdrop_list.update()
        self.pushblock.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
        A = (0, 2, 4)
        # Draw the background
        
        screen.fill(BLACK)
         
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.imageplatform_list.draw(screen)
        self.end_list.draw(screen)
        #self.backdrop_list.draw(screen)
        self.enemy_list.draw(screen)
    #    self.pushblock.draw(screen)
    def shift_world_x(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
        
        for platformimage in self.imageplatform_list:
            platformimage.rect.x += shift_x
        for endimg in self.end_list:
            endimg.rect.x += shift_x
        #for backdrop in self.backdrop_list:
        #    backdrop.rect.x += shift_x*2
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        for box in self.pushblock:
            box.rect.x+=5
    def shift_world_y(self, shift_y):
        """ When the user moves up/down and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_height += shift_y
        # Go through all the sprite lists and change height
        for platform in self.platform_list:
            platform.rect.y += shift_y
        for platformimage in self.imageplatform_list:
            platformimage.rect.y += shift_y
        for endimg in self.end_list:
            endimg.rect.y += shift_y
        for enemy in self.enemy_list:
            enemy.rect.y += shift_y
# Create platforms for the level
from Levels.LevelList import *
from Levels.Objects.ObjectList import *
