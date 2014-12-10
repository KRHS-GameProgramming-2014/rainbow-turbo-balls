import pygame, sys, random
from AIballs import Ball_BL, Ball_GN, Ball_OG, Ball_PL, Ball_RD, Ball_YW
#from Player import Player
from Score import Score

pygame.init()

clock = pygame.time.Clock()

width = 1100 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0 


screen = pygame.display.set_mode(size)

ball_BL = Ball("RSC/AI Balls/BL_AI_B.png", [3,9], [375, 150])
ball_GN = Ball("RSC/AI Balls/GN_AI_B.png", [4,8], [450, 300])
ball_OG = Ball("RSC/AI Balls/OG_AI_B.png", [5,7], [375, 450])
ball_PL = Ball("RSC/AI Balls/PL_AI_B.png", [6,6], [225, 450])
ball_RD = Ball("RSC/AI Balls/RD_AI_B.png", [7,5], [150, 300])
ball_YW = Ball("RSC/AI Balls/YW_AI_B.png", [8,4], [225, 150])


gs = Score('green', 'black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    ball_BL.update(width, height)
    ball_GN.update(width, height)
    ball_OG.update(width, height)
    ball_PL.update(width, height)
    ball_RD.update(width, height)
    ball_YW.update(width, height)
    
    ball_BL.collideBall(ball_GN)
    ball_BL.collideBall(ball_OG)
    ball_BL.collideBall(ball_PL)
    ball_BL.collideBall(ball_RD)
    ball_BL.collideBall(ball_YW)
    
    ball_GN.collideBall(ball_BL)
    ball_GN.collideBall(ball_OG)
    ball_GN.collideBall(ball_PL)
    ball_GN.collideBall(ball_RD)
    ball_GN.collideBall(ball_YW)
    
    ball_OG.collideBall(ball_BL)
    ball_OG.collideBall(ball_GN)
    ball_OG.collideBall(ball_PL)
    ball_OG.collideBall(ball_RD)
    ball_OG.collideBall(ball_YW)
    
    ball_PL.collideBall(ball_BL)
    ball_PL.collideBall(ball_GN)
    ball_PL.collideBall(ball_OG)
    ball_PL.collideBall(ball_RD)
    ball_PL.collideBall(ball_YW)
    
    ball5.collideBall(ball_BL)
    ball5.collideBall(ball_GN)
    ball5.collideBall(ball_OG)
    ball5.collideBall(ball_PL)
    ball5.collideBall(ball_YW)
    
    ballYW.collideBall(ball_BL)
    ballYW.collideBall(ball_GN)
    ballYW.collideBall(ball_OG)
    ballYW.collideBall(ball_PL)
    ballYW.collideBall(ball_RD)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(gs.image, gs.rect)
    screen.blit(ball_BL.image, ball_BL.rect)
    screen.blit(ball_GN.image, ball_GN.rect)
    screen.blit(ball_OG.image, ball_OG.rect)
    screen.blit(ball_PL.image, ball_PL.rect)
    screen.blit(ball_RD.image, ball_RD.rect)
    screen.blit(ball_YW.image, ball_YW.rect)
    pygame.display.flip()
    clock.tick(60)
        
        
        
        
