import pygame, sys, random
from GameBalls import Ball
from GameBalls import PBall
from Score import Score
from Button import Button

pygame.init()

clock = pygame.time.Clock()

width = 1100 
height = 700
size = width, height

screen = pygame.display.set_mode(size)

balls = []
    
bgColor = r,g,b = 0, 0, 0 
bgImage = pygame.image.load("RSC/Game/SCREEN.png").convert()
bgRect = bgImage.get_rect()

run = False

<<<<<<< HEAD
#balls = [Ball("RSC/AI Balls/BL_AI_B.png", [7,7], [375, 150]),
         #Ball("RSC/AI Balls/GN_AI_B.png", [6,6], [450, 300]),
         #Ball("RSC/AI Balls/OG_AI_B.png", [3,3], [375, 450]),
         #Ball("RSC/AI Balls/PL_AI_B.png", [1,1], [225, 450]),
         #Ball("RSC/AI Balls/RD_AI_B.png", [2,2], [150, 300]),
         #Ball("RSC/AI Balls/YW_AI_B.png", [5,5], [225, 150])]
#PB_Black = Ball("RSC/Player Balls/BK_P_B.png", [4,4], [300,400])
#PB_White = Ball("RSC/Player Balls/WT_P_B.png", [4,4], [375, 400])
=======
player = PBall
PB_Black = ([4,4], [300,400])
#PB_White = Ball(, [4,4], [375, 400])
>>>>>>> origin/master

#gs = Score('green', 'black')

run = False

startButton = Button([width/2, height-200], 
                     "RSC/Game/NEW_GAME_BUTTON.png")

while True:
<<<<<<< HEAD
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = True
                    
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        clock.tick(60)
        
        bgImage = pygame.image.load("RSC/Game/START_SCREEN_BACKROUND.png").convert()
        bgRect = bgImage.get_rect()
    while run:
        bgImage = pygame.image.load("RSC/Game/SCREEN.png").convert()
        bgRect = bgImage.get_rect()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
        
        if len(balls) < 20:
            spawn_number = random.randint(0,64)
            if spawn_number < 32:
                balls += [Ball("purple", [1,1], [random.randint (0,1100), random.randint (0,700)])]
            elif spawn_number < 48:
                balls += [Ball("red", [2,2], [random.randint (0,1100), random.randint (0,700)])]
            elif spawn_number < 56: 
                balls += [Ball("orange", [3,3], [random.randint (0,1100), random.randint (0,700)])]
            elif spawn_number < 60: 
                balls += [Ball("yellow", [5,5], [random.randint (0,1100), random.randint (0,700)])]
            elif spawn_number < 62: 
                balls += [Ball("green", [6,6], [random.randint (0,1100), random.randint (0,700)])]
            else:  
                balls += [Ball("blue", [7,7], [random.randint (0,1100), random.randint (0,700)])]

        for ball in balls:
            ball.update(width, height)
        
        #for bully in balls:
            #for victem in balls:
                #bully.collideBall(victem)


        
        #for ball in balls:
            #if not ball.living:
                #balls.remove(ball)
        
        
        bgColor = r,g,b
        #screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        #screen.blit(PB_Black.image, PB_Black.rect)
        #screen.blit(PB_White.image, PB_White.rect)
        
        pygame.display.flip()
        clock.tick(60)
=======
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop left")
    
    if len(balls) < 20:
        spawn_number = random.randint(0,64)
        if spawn_number < 32:
            balls += [Ball("purple", [1,1], [random.randint (0,1100), random.randint (0,700)])]
        elif spawn_number < 48:
            balls += [Ball("red", [2,2], [random.randint (0,1100), random.randint (0,700)])]
        elif spawn_number < 56: 
            balls += [Ball("orange", [3,3], [random.randint (0,1100), random.randint (0,700)])]
        elif spawn_number < 60: 
            balls += [Ball("yellow", [5,5], [random.randint (0,1100), random.randint (0,700)])]
        elif spawn_number < 62: 
            balls += [Ball("green", [6,6], [random.randint (0,1100), random.randint (0,700)])]
        else:  
            balls += [Ball("blue", [7,7], [random.randint (0,1100), random.randint (0,700)])]

    for ball in balls:
        ball.update(width, height)
    
    for bully in balls:
        for victem in balls:
            bully.collideBall(victem)


    
    #for ball in balls:
        #if not ball.living:
            #balls.remove(ball)
    
    
    bgColor = r,g,b
    #screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    #screen.blit(PB_Black.image, PB_Black.rect)
    #screen.blit(PB_White.image, PB_White.rect)
    
    pygame.display.flip()
    clock.tick(60)
>>>>>>> origin/master
        
        
        
        
