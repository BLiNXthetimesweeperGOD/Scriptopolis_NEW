import pygame
from LVLDAT import Level
from PlatformOBJ import Platform
#from backdrop import BGL
from PlatformImageOBJ import PlatformImage
from PlayerCharacter import Player
import random
import os
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255,100,100)
PURPLE = (255,0,255)
GRAY = (100,100,100)
class Level_01(Level):
    """ Definition for level 1. """
    def __init__(self, player):
        """ Create level 1. """
        #Platform types are in this list for level creation purposes:                                           (0)
        types = ["spawn",#Where the player starts                                              (0)
                 "",#The main floor type                                                       (1)
                 "normal",#Same as ""                                                          (2)
                 "up",#Acts as an elevator going up                                            (3)
                 "down",#Acts as an elevator going down                                        (4)
                 "bouncy",#Trampoline-like, sends you higher with each bounce up to 10 bounces (5)
                 "fall",#Falls out of the world                                                (6)
                 "flyup",#Flies away                                                           (7)
                 "pullup",#Pulls the player to it                                              (8)
                 "pulldown",#Pulls the player to it                                            (9)
                 "pullleft",#Pulls the player to it                                           (10)
                 "pullright",#Pulls the player to it                                          (11)
                 "vanish",#Vanishes on contact                                                (12)
                 "hazard",#Dangerous to touch                                                 (13)
                 "fast",#Speeds the player up                                                 (14)
                 "slow",#Slows the player down                                                (15)
                 "reset",#Sends the player back to the start of the level                     (16)
                 "goal",#Completes the level if another level exists after the current one    (17)
                 "push",#You can push these                                                   (18)
                 "timed",#Vanishes and reappears on a timer                                   (19)
                 "slideleft",#Moves the player to the left                                    (20)
                 "slideright",#Moves the player to the right                                  (21)
                 "message",#Sets the current text                                             (22)
                 "enablemessages",#Enables the text                                           (23)
                 "disablemessages",#Disables the text                                         (24)
                 "multimessage",#Makes multiple timed messages appear                         (25)
                 "flyingplatform",#Oh, hey! It's me!... At least it was.                      (26) (IDs 28 and 29 can be used to alter the state of this platform)
                 "lowerlimit",#Warps player back to spawn in the case that they fall.         (27)
                 "fpenable",#Enables the flying platform's movement.                          (28)
                 "fpdisable",#Disables the flying platform's movement.                        (29)
                 "suffer",#As the name implies, it's meant to make the player suffer.         (30)
                 ]
        # Call the parent constructor
        Level.__init__(self, player)
        self.level_limit = -2500
        #Level platform list (if the ID is a 1, it's the default block)
        level = [[1, 11, -1, -22, 1],
                 [1, 11, 4, -24, 1],
                 [1, 1, -5, 0, 8],#Pull block (up)
                 [10, 1, 5, -24, 1],
                 [1, 1, 0, -15, 5],#Bouncy block
                 [9, 1, -1, -11, 1],
                 [9, 1, -10, -4, 1],
                 [1, 8, -1, -11, 1],
                 [1, 1, 0, -1, 5],#Bouncy block
                 [1, 1, 1, -6, 3],#Up elevator block
                 [1, 5, 2, -5, 1],
                 [1, 1, 3, -8, 4],#Down elevator block
                 [1, 1, 4, -4, 5],#Bouncy block
                 [1, 1, 8, -8, 1],
                 [2, 1, -4, 0, 1],
                 [1, 5, 1, -5, 1],
                 [1, 5, 3, -5, 1],
                 [6, 3, 4, -3, 1],
                 [20, 1, 1, 0, 1],
                 [2, 1, -1, 0, 1],
                 [2, 1, -1, 0, 1],
                 [1, 1, -2, 25000, 22, "This is where you respawn if you manage to fall off the level."],
                 [1, 1, -2, 55, 27],#Lower limit for this map (the respawn zone)
                 [1, 2, 8, -5, 18],#Pushable block
                 [1, 1, 6, 25000, 22, "These blocks can be pushed! Lovely, right?"],
                 [1, 1, 16, -5, 26],#Flying block
                 [1, 1, 16, 25000, 22, "The floating block can indeed fly. There is left/right boundaries for it though."],
                 [1,1, 8+16, 25, 29],#Flying block disabled zone
                 [15,1, 9, 25, 28],#Flying block enabled zone
                 [1,1, 8, 25, 29],#Flying block disabled zone
                 [1,10,-25,-9,30],#Suffer!
                 [2, 3, 8, -8, 1],
                 [1, 1, -2, 0, 0],#Spawn block
                 ]
        # Go through the array above and add platforms
        for platform in level:
            #block = Platform(platform[0]*64, platform[1]*64)
            Btype = types[platform[4]]
            if Btype != "up" or Btype != "down":
                block = Platform(platform[0]*64, platform[1]*64)
                block.rect.x = platform[2]*64
                block.rect.y = platform[3]*64
                block.type = types[platform[4]]
            Y = platform[3]
            if Btype == "spawn":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles', "spawnTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "up":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles', "moveUpTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "down":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles', "moveDownTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "push":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles', "moveDownTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "bouncy":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles', "moveBounceTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "" or Btype == "normal":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles', "floorTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype.startswith("pull"):
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles', "pullTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "message":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles',"setMessageTile.PNG")).convert()
                        block.message = platform[5]
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "enablemessages":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles',"setEnableTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "disablemessages":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles',"setDisableTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "suffer":
                for i in range(platform[1]):
                    X = platform[2]
                    for i in range(platform[0]):
                        block = Platform(1*64, 1*64)
                        block.rect.x = X*64
                        block.rect.y = Y*64
                        block.type = types[platform[4]]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles',"sufferTile.PNG")).convert()
                        self.platform_list.add(block)
                        X+=1
                    Y+=1
            if Btype == "developer":
                block.image = pygame.image.load(os.path.join('images', "Dr RNG 3.PNG")).convert()
                block.type = types[platform[4]]
            if Btype == "flyingplatform":
                block = Platform(1*64, 1*64)
                block.rect.x = platform[2]*64
                block.rect.y = platform[3]*64
                block.type = types[platform[4]]
                block.image = pygame.image.load(os.path.join('blockimages', "FlyingPlatform.PNG")).convert()
            self.platform_list.add(block)
