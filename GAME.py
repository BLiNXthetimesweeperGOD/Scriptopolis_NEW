Music = ["Silence","Silence","loop0","loop2"]
from LoadDepends import *

# Global constants
level_count = 3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 600

def main():
    """ Main Program """
    pygame.init()
    
    font = pygame.font.SysFont("arial", 15)
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode((size), pygame.RESIZABLE)
    #Start off by getting everything set up
    player = Player() #Create the player
    level_list = [] #Create the level lists
    level_list.append(Level_01(player))
    #level_list.append(Level_04(player))
    #level_list.append(Level_05(player))
    #level_list.append(Level_03(player))
    
    pygame.display.set_caption("Scriptopolis Game")
 
    
    current_level_no = 0
    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    playrect = 0
    playrect2 = 0
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    drawgmovertxt = False
    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    for block in player.level.platform_list:
        if block.type == "spawn":
            blocksides = [block.rect.left, block.rect.right]
            startpos = st.median(blocksides)
            player.rect.bottom = block.rect.top
            player.rect.x = startpos
    
    pygame.mixer_music.load("music\\%s.wav" % (Music[current_level_no]))
    pygame.mixer_music.play(loops=0, start=0.0, fade_ms=1999)
    size = []
    # -------- Main Program Loop -----------
    while not done:
        #Player inputs
        size = pygame.display.get_window_size()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    player.text = "ON"
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    if player.freeFly != 1:
                        player.jump()
                    else:
                        player.go_up()
                if event.key == pygame.K_DOWN:
                    if player.freeFly != 1:
                        "Do nothing I guess... Maybe I should add a crouch animation."
                    else:
                        player.go_down()
                #Debug keys
                if event.key == pygame.K_KP0:
                    if player.debug == 0:
                        player.debug = 1
                    else:
                        player.debug = 0
                #Disable particles
                if event.key == pygame.K_KP1:
                    if player.noParticles == 0:
                        player.noParticles = 1
                    else:
                        player.noParticles = 0
                #Disable walls
                if event.key == pygame.K_KP2:
                    if player.noClip == 0:
                        player.noClip = 1
                    else:
                        player.noClip = 0
                #Disable special block physics
                if event.key == pygame.K_KP3:
                    if player.noPhysicsBlocks == 0:
                        player.noPhysicsBlocks = 1
                    else:
                        player.noPhysicsBlocks = 0
                #Disable textures/sprites/images and set everything to a flat color
                if event.key == pygame.K_KP4:
                    if player.noSprites == 0:
                        player.noSprites = 1
                        player.justSet = 1
                    else:
                        player.noSprites = 0
                        player.justSet = 1
                #Warp to spawn (good to escape softlocks)
                if event.key == pygame.K_KP5:
                    player.toSpawn = 1
                #Randomly warp the player to a different location on the map
                if event.key == pygame.K_KP6:
                    if player.randomlyWarp == 0:
                        player.randomlyWarp = 1
                if event.key == pygame.K_KP7:
                    print(size)
                #Cycle through the maps.
                #Each press adds 1 to the current stage ID and if it's more than the stage count, it goes back to the first map.
                if event.key == pygame.K_END:
                    if current_level_no <= len(level_list)-2:
                        pygame.mixer_music.fadeout(300)
                        current_level_no += 1
                        current_level = level_list[current_level_no]
                        player.level = current_level
                        player.toSpawn = 1
                        player.text = 0
                        player.justSet = 1
                    else:
                        pygame.mixer_music.fadeout(2000)
                        current_level_no = 0
                        current_level = level_list[current_level_no]
                        player.level = current_level
                        player.toSpawn = 1
                        player.text = 0
                        player.justSet = 1
                #Infinite jumps
                if event.key == pygame.K_KP8:
                    if player.noJumpCap == 0:
                        player.noJumpCap = 1
                    else:
                        player.noJumpCap = 0
                #Free fly mode
                if event.key == pygame.K_KP9:
                    if player.freeFly == 0:
                        player.freeFly = 1
                    else:
                        player.freeFly = 0
                #Free fly mode speed control
                if event.key == pygame.K_KP_PLUS:
                    player.speedMultiplier+=1
                if event.key == pygame.K_KP_MINUS:
                    player.speedMultiplier-=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0 and player.freeFly == 1:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0 and player.freeFly == 1:
                    player.stop()
        if pygame.mixer_music.get_pos() == -1:
            pygame.mixer_music.fadeout(3000)
            pygame.mixer_music.load("music\\%s.wav" % (Music[current_level_no]))
            pygame.mixer_music.play(loops=0, start=0.0, fade_ms=0)
        # Update the player.
        active_sprite_list.update()
        # Update items in the level
        current_level.update()
        scaleCorrector = int(size[0]/4)
        scaleCorrector2 = int(size[1]/4)
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= int(scaleCorrector*3):
            diff = int(scaleCorrector*3)-player.rect.right
            player.rect.right = int(scaleCorrector*3)
            #if diff > player.speedCap and player.change_x == player.speedCap:
            current_level.shift_world_x(diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= scaleCorrector:
            diff = scaleCorrector - player.rect.left
            player.rect.left = scaleCorrector
            current_level.shift_world_x(diff)

        # If the player gets near the top of the screen, shift the world down (-y)
        if player.rect.top <= scaleCorrector2:
            diff = player.rect.top - scaleCorrector2
            player.rect.top = scaleCorrector2
            current_level.shift_world_y(-diff)
 
        # If the player gets near the bottom of the screen, shift the world up (+y)
        if player.rect.bottom >= int(scaleCorrector2*3):
            diff = int(scaleCorrector2*3) - player.rect.bottom
            player.rect.bottom = int(scaleCorrector2*3)
            current_level.shift_world_y(diff)
        if player.text == "ON":
            PMES = font.render("%s" % (player.message), 1, (100,255,0))
        if player.debug == 1:
            #All of the debug text rendered during the game
            JUMP = font.render("JUMPS   %d" % (player.jumps), 1, (255,255,255))
            SNAP = font.render("FALL_SPEED_CHECK    %d" % (player.snappedtofloor), 1, (255,255,255))
            DIRT = font.render("FACING  %d" % (player.Direction), 1, (255,255,255))
            BOUN = font.render("BOUNCE_COUNT  %d" % (player.bounces), 1, (255,255,255))
            Xspd = font.render("X_SPEED %d" % (player.change_x), 1, (255,255,255))
            Yspd = font.render("Y_SPEED %d" % (player.change_y), 1, (255,255,255))
            CLIP = font.render("NO_COLLISION  %d" % (player.noClip), 1, (150,95,255))
            FLYM = font.render("FLY_MODE %d" % (player.freeFly), 1, (150,95,255))
            IJMP = font.render("INFINITE_JUMP %d" % (player.noJumpCap), 1, (150,95,255))
            IMGS = font.render("NO_SPRITES   %d %d" % (player.noSprites, player.noParticles), 1, (150,95,255))
            NPRP = font.render("NO_BLOCK_PROPERTIES %d" % (player.noPhysicsBlocks), 1, (150,95,255))
            FPEN = font.render("FLYING_PLATFORM_ACTIVE %d" % (player.fpEnabled), 1, (150,95,255))
            FRAM = font.render("STATE   %d %d %d %d %s %s" % (player.frame, player.bounces, player.Direction, player.pushing, player.state, player.image), 1, (150,95,255))
            if player.type != "":
                TYPE = font.render("SBTYPE   %s" % (player.type), 1, (150,95,20))#Displays what block type you're standing on
            if player.type == "":
                TYPE = font.render("SBTYPE   default", 1, (150,95,20))#Displays what block type you're standing on
            LEVL = font.render("STAGE   %d" % (current_level_no), 1, (100 ,255,100))
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit and current_level_no != level_count:
            player.rect.x = 120
            pygame.mixer_music.fadeout(300)
            print(current_level_no)
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        current_height = player.rect.y + current_level.world_height
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        POSX = font.render("POS_X %d" % (current_position), 1, (255,255,100))
        POSY = font.render("POS_Y %d" % (current_height), 1, (255,255,100))
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        draws = 0
        draws = player.rect.top
        if player.change_y >= 100:
            player.timer+=1
        # Particle effect generator. Needs to be cleaned up eventually, as the code is basically unreadable in some places.
        if player.noParticles != 1:
            #if size[0] > 600 and size[1] > 400:
            for g in range(player.rect.top,player.rect.bottom):
                draws+=1
                if player.Direction == 0:
                    direction = -1
                if player.Direction == 1:
                    direction = 1
                try:
                    if random.randint(0, 2) == 2:
                        for i in range(player.rect.left, player.rect.right):
                            A = screen.get_at((i, draws))
                            
                            A[0] = random.randint(1, 255)
                            A[1] = random.randint(1, 255)
                            A[3] = random.randint(1, 255)
                            if player.bounces != 0:
                                A[0] = random.randint(1, 100)
                                A[1] = random.randint(1, 250)
                                A[3] = random.randint(1, 255)
                            if player.goingUp != 0:
                                A[0] = random.randint(1, 100)
                                A[1] = random.randint(1, 200)
                                A[3] = random.randint(1, 255)
                            if player.goingDown != 0:
                                A[0] = random.randint(1, 255)
                                A[1] = random.randint(1, 200)
                                A[3] = random.randint(1, 100)
                                
                            if A[0] != 0 and A[1] != 0 and A[2] != 0 and random.randint(0, 1) == 1:
                                screen.set_at((i-int(player.change_x), int(draws+player.change_y/3*-1)), A)#A is the color, i is the location, player x/y speed alters where the pixel gets drawn to
                                screen.set_at((i-int(player.change_x/1.5), int(draws+player.change_y/2*-1)), A)
                                screen.set_at((i-int(player.change_x/2), int(draws+player.change_y/1*-1)), A)
                except:
                    "OUT OF BOUNDS PIXEL, OH NO! WE'RE GOING TO DIE! Oh, wait. False alarm. I somehow stopped it from killing us."
        # Limit to 60 frames per second
        clock.tick(60)
        if player.text == "ON":
            screen.blit(PMES, (100, 50))
        if player.debug == 1: #Needs to be cleaned up eventually. I got a bit lazy with the numbers.
            screen.blit(TYPE, (50, 65))
            screen.blit(Xspd, (50, 80))
            screen.blit(Yspd, (50, 95))
            screen.blit(JUMP, (50, 110))
            screen.blit(BOUN, (50, 125))
            screen.blit(FRAM, (50, 125+15))
            screen.blit(DIRT, (50, 140+15))
            screen.blit(LEVL, (50, 155+15))
            screen.blit(SNAP, (50, 170+15))
            screen.blit(CLIP, (50, 170+15+15))
            screen.blit(IJMP, (50, 170+15+15+15))
            screen.blit(IMGS, (50, 170+15+15+15+15))
            screen.blit(FLYM, (50, 170+15+15+15+15+15))
            screen.blit(NPRP, (50, 170+15+15+15+15+15+15))
            screen.blit(FPEN, (50, 170+15+15+15+15+15+15+15))
            
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        player.pushing = 0
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
if __name__ == "__main__":
    main()

