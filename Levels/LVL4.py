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
class Level_04(Level):
    """ Definition for level 1. """
    def __init__(self, player):
        """ Create level 1. """
        #Platform types are in this list for level creation purposes:
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
                 "pushable",#You can push these                                               (18)
                 "timed",#Vanishes and reappears on a timer                                   (19)
                 "slideleft",#Moves the player to the left                                    (20)
                 "slideright",#Moves the player to the right                                  (21)
                 "message",#Sets the current text                                             (22)
                 "enablemessages",#Enables the text                                           (23)
                 "disablemessages",#Disables the text                                         (24)
                 "multimessage",#Makes multiple timed messages appear                         (25)
                 "developer",#Oh, hey! It's me!                                               (26)
                 "lowerlimit",#Warps player back to spawn in the case that they fall.         (27)
                 
                 ]
        # Call the parent constructor
        Level.__init__(self, player)
        player.text = "OFF"
        self.level_limit = -10500
        #Level platform list
        level = [
                 [5, 1, 0, 0, 0],#Spawn object
                 [1,1,5,0,23], 
                 [10, 1, 6, 0, 22, "Hey, can you hear me?"],
                 [9, 1, 16, 0, 22, "Hello?"],
                 [9, 1, 25, 0, 22, "Please listen!"],
                 [9, 1, 34, 0, 22, "I need your help."],
                 [8, 1, 42, 0, 22, "Our program is in danger."],
                 [30, 1, 50, 0, 22, "You need to go get our only developer back!"],
                 [20, 1, 80, 0, 22, "He's been ignoring us for far too long."],
                 [15, 1, 100, 0, 22, "You should be able to find him in the next room."],
                 [1, 1, 115, 0, 24],
                 [9,1,116,0,1],
                 [10, 1, 125, 0, 1],
                 [10, 1, 135, 0, 2],
                 [10, 1, 145, 0, 3],
                 [10, 1, 155, 0, 4],
                 [1,1,999,25,27],#Lower limit object
                 ]
        areas = [
            [10, 10, 1, 1]
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
                        block.message = platform[5]
                        block.image = pygame.image.load(os.path.join('blockimages/Tiles',"setMessageTile.PNG")).convert()
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
            if Btype == "developer":
                block.image = pygame.image.load(os.path.join('images', "Dr RNG 3.PNG")).convert()
            self.platform_list.add(block)
