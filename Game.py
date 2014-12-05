import pygame, sys, random
from AIballs import Ball
#from Player import Player

pygame.init()

clock = pygame.time.Clock()

width = 1100 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0 


screen = pygame.display.set_mode(size)

ball1 = Ball("RSC/AI Balls/BL_AI_B.png", [7,7], [375, 150])
ball2 = Ball("RSC/AI Balls/GN_AI_B.png", [6,6], [450, 300])
ball3 = Ball("RSC/AI Balls/OG_AI_B.png", [5,5], [375, 450])
ball4 = Ball("RSC/AI Balls/PL_AI_B.png", [1,1], [150, 300])
ball5 = Ball("RSC/AI Balls/RD_AI_B.png", [2,2], [225, 150])
ball6 = Ball("RSC/AI Balls/YW_AI_B.png", [3,3], [300, 300])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    ball1.update(width, height)
    ball2.update(width, height)
    ball3.update(width, height)
    ball4.update(width, height)
    ball5.update(width, height)
    ball6.update(width, height)
    
    ball1.collideBall(ball2)
    ball1.collideBall(ball3)
    ball1.collideBall(ball4)
    ball1.collideBall(ball5)
    ball1.collideBall(ball6)
    
    ball2.collideBall(ball1)
    ball2.collideBall(ball3)
    ball2.collideBall(ball4)
    ball2.collideBall(ball5)
    ball2.collideBall(ball6)
    
    ball3.collideBall(ball1)
    ball3.collideBall(ball2)
    ball3.collideBall(ball4)
    ball3.collideBall(ball5)
    ball3.collideBall(ball6)
    
    ball4.collideBall(ball1)
    ball4.collideBall(ball2)
    ball4.collideBall(ball3)
    ball4.collideBall(ball5)
    ball4.collideBall(ball6)
    
    ball5.collideBall(ball1)
    ball5.collideBall(ball2)
    ball5.collideBall(ball3)
    ball5.collideBall(ball4)
    ball5.collideBall(ball6)
    
    ball6.collideBall(ball1)
    ball6.collideBall(ball2)
    ball6.collideBall(ball3)
    ball6.collideBall(ball4)
    ball6.collideBall(ball5)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    screen.blit(ball3.image, ball3.rect)
    screen.blit(ball4.image, ball4.rect)
    screen.blit(ball5.image, ball5.rect)
    screen.blit(ball6.image, ball6.rect)
    pygame.display.flip()
    clock.tick(60)
        
        
        
        
