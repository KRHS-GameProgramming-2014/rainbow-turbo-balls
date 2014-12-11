import pygame, sys, random
from AIballs import Ball
#from Player import Player
from Score import Score

pygame.init()

clock = pygame.time.Clock()

width = 1100 
height = 700
size = width, height

screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0 
bgImage = pygame.image.load("RSC/Game/SCREEN.png").convert()
bgRect = bgImage.get_rect()

ball_BL = Ball("RSC/AI Balls/BL_AI_B.png", [7,7], [375, 150])
ball_GN = Ball("RSC/AI Balls/GN_AI_B.png", [6,6], [450, 300])
ball_OG = Ball("RSC/AI Balls/OG_AI_B.png", [3,3], [375, 450])
ball_PL = Ball("RSC/AI Balls/PL_AI_B.png", [1,1], [225, 450])
ball_RD = Ball("RSC/AI Balls/RD_AI_B.png", [2,2], [150, 300])
ball_YW = Ball("RSC/AI Balls/YW_AI_B.png", [5,5], [225, 150])


#gs = Score('green', 'black')

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
    
    ball_RD.collideBall(ball_BL)
    ball_RD.collideBall(ball_GN)
    ball_RD.collideBall(ball_OG)
    ball_RD.collideBall(ball_PL)
    ball_RD.collideBall(ball_YW)
    
    ball_YW.collideBall(ball_BL)
    ball_YW.collideBall(ball_GN)
    ball_YW.collideBall(ball_OG)
    ball_YW.collideBall(ball_PL)
    ball_YW.collideBall(ball_RD)
    
    bgColor = r,g,b
    #screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    screen.blit(ball_BL.image, ball_BL.rect)
    screen.blit(ball_GN.image, ball_GN.rect)
    screen.blit(ball_OG.image, ball_OG.rect)
    screen.blit(ball_PL.image, ball_PL.rect)
    screen.blit(ball_RD.image, ball_RD.rect)
    screen.blit(ball_YW.image, ball_YW.rect)
    pygame.display.flip()
    clock.tick(60)
        
        
        
        
