import pygame, sys, random
from GameBalls import Ball
from GameBalls import PBall
from Score import Score
from Button import Button
from hud import Text
from hud import Score

#test 1
pygame.init()

clock = pygame.time.Clock()

width = 1100 
height = 700
size = width, height

screen = pygame.display.set_mode(size)

balls = []
aiBalls = []
    
bgColor = r,g,b = 0, 0, 0 
bgImage = pygame.image.load("RSC/Game/SCREEN.png").convert()
bgRect = bgImage.get_rect()

run = False


PB_Black = PBall("Black", [300,400])
PB_White = PBall("white", [375, 400])


#gs = Score('green', 'black')

run = False

startButton = Button([width/2, height-200], 
                     "RSC/Game/NEW_GAME_BUTTON.png")
bgImage = pygame.image.load("RSC/Game/START_SCREEN_BACKROUND.png").convert()
bgRect = bgImage.get_rect()
while True:
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
        
    bgImage = pygame.image.load("RSC/Game/SCREEN.png").convert()
    bgRect = bgImage.get_rect()   
    while run:
        #-----Events-----
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    PB_Black.go("up")
                if event.key == pygame.K_d:
                    PB_Black.go("right")
                if event.key == pygame.K_s:
                    PB_Black.go("down")
                if event.key == pygame.K_a:
                    PB_Black.go("left")
                if event.key == pygame.K_UP:
                    PB_White.go("up")
                if event.key == pygame.K_RIGHT:
                    PB_White.go("right")
                if event.key == pygame.K_DOWN:
                    PB_White.go("down")
                if event.key == pygame.K_LEFT:    
                    PB_White.go("left")
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    PB_Black.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    PB_Black.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    PB_Black.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    PB_Black.go("stop left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    PB_White.go("stop up")
                if event.key == pygame.K_RIGHT:
                    PB_White.go("stop right")
                if event.key == pygame.K_DOWN:
                    PB_White.go("stop down")
                if event.key == pygame.K_LEFT:
                    PB_White.go("stop left")                   
        
        #-----Spawn-----
        if (len(balls) + len(aiBalls)) < 20:
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

        #-----Update----
        PB_Black.update(width, height)
        PB_White.update(width, height)
        
        for ball in balls:
            ball.update(width, height)
        for ball in aiBalls:
            ball.update(width, height)
        
        #-----Collide----
        for bully in balls:
            PB_Black.collideBall(bully)
            aiBalls += bully.collidePBall(PB_Black)
            if not bully.living:
                balls.remove(bully)
                break
            PB_White.collideBall(bully)
            aiBalls += bully.collidePBall(PB_White)
            if not bully.living:
                balls.remove(bully)
                break
            for victem in balls:
                bully.collideBall(victem)
               
        for bully in aiBalls:
            for victem in balls:
                aiBalls += victem.collideAIBall(bully)
                #bully.collideBall(victem)
                if not victem.living:
                    balls.remove(victem)
                    break
            for victem in aiBalls:
                bully.collideAIBall(victem)
                
                victem.collideAIBall(bully)
                if not bully.living:
                    aiBalls.remove(bully)
                    break
                if not victem.living:
                    aiBalls.remove(victem)
                    break
            if bully.color == "white":
                bully.collideAIBall(PB_Black)
            if bully.color == "black":
                bully.collideAIBall(PB_White)
        """
        for ball in balls:
            if not ball.living:
                balls.remove(ball)
                break
        for ball in aiBalls:
            if not ball.living:
                balls.remove(ball)
                break
        """
         
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        for ball in aiBalls:
            screen.blit(ball.image, ball.rect)
        screen.blit(PB_Black.image, PB_Black.rect)
        screen.blit(PB_White.image, PB_White.rect)
        
        pygame.display.flip()
        clock.tick(60)
            
            
            
            
