import pygame, sys, random
from GameBalls import Ball
from GameBalls import PBall
from Score import Score

pygame.init()

clock = pygame.time.Clock()

width = 1100 
height = 700
size = width, height

screen = pygame.display.set_mode(size)

balls = []
balls += [Ball("RSC/Player Balls/BK_P_B.png", [4,5], [100, 125])]

bgColor = r,g,b = 0, 0, 0 
bgImage = pygame.image.load("RSC/Game/SCREEN.png").convert()
bgRect = bgImage.get_rect()

balls = [Ball("RSC/AI Balls/BL_AI_B.png", [7,7], [375, 150]),
         Ball("RSC/AI Balls/GN_AI_B.png", [6,6], [450, 300]),
         Ball("RSC/AI Balls/OG_AI_B.png", [3,3], [375, 450]),
         Ball("RSC/AI Balls/PL_AI_B.png", [1,1], [225, 450]),
         Ball("RSC/AI Balls/RD_AI_B.png", [2,2], [150, 300]),
         Ball("RSC/AI Balls/YW_AI_B.png", [5,5], [225, 150])]
player = Ball("RSC/Player Balls/BK_P_B.png", [4,4], [300,400])
PB_White = Ball("RSC/Player Balls/WT_P_B.png", [4,4], [375, 400])

#gs = Score('green', 'black')

while True:
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
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
    screen.blit(PB_Black.image, PB_Black.rect)
    screen.blit(PB_White.image, PB_White.rect)
    
    pygame.display.flip()
    clock.tick(60)
        
        
        
        
