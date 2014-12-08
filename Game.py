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

ball1 = Ball("ball.png", [3,9], [375, 150], "ball_hit.png")
ball2 = Ball("ball.png", [4,8], [450, 300], "ball_hit.png")
ball3 = Ball("ball.png", [5,7], [375, 450], "ball_hit.png")
ball4 = Ball("ball.png", [6,6], [225, 450], "ball_hit.png")
ball5 = Ball("ball.png", [7,5], [150, 300], "ball_hit.png")
ball6 = Ball("ball.png", [8,4], [225, 150], "ball_hit.png")
ball7 = Ball("ball.png", [9,3], [300, 300], "ball_hit.png")

gs = Score('green', 'black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    ball_BL.update(width, height)
    ball_GN.update(width, height)
    ball_OG.update(width, height)
    ball_PL.update(width, height)
    ball_RD.update(width, height)
    ballYW.update(width, height)
    
    ball_BL.collideBall(ball_GN)
    ball_BL.collideBall(ball_OG)
    ball_BL.collideBall(ball_PL)
    ball_BL.collideBall(ball_RD)
    ball_BL.collideBall(ball_YW)
    
    ball_GN.collideBall(ball_BL)
    ball_GN.collideBall(ball_OG)
    ball_GN.collideBall(ball_PL)
    ball_GN.collideBall(ball5)
    ball_GN.collideBall(ball6)
    
    ball_OG.collideBall(ball_BL)
    ball_OG.collideBall(ball_GN)
    ball_OG.collideBall(ball_PL)
    ball_OG.collideBall(ball5)
    ball_OG.collideBall(ball6)
    
    ball_PL.collideBall(ball_BL)
    ball_PL.collideBall(ball_GN)
    ball_PL.collideBall(ball_OG)
    ball_PL.collideBall(ball5)
    ball_PL.collideBall(ball6)
    
    ball5.collideBall(ball_BL)
    ball5.collideBall(ball_GN)
    ball5.collideBall(ball_OG)
    ball5.collideBall(ball_PL)
    ball5.collideBall(ball6)
    
    ball6.collideBall(ball_BL)
    ball6.collideBall(ball_GN)
    ball6.collideBall(ball_OG)
    ball6.collideBall(ball_PL)
    ball6.collideBall(ball5)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(gs.image, gs.rect)
    screen.blit(ball_BL.image, ball_BL.rect)
    screen.blit(ball_GN.image, ball_GN.rect)
    screen.blit(ball_OG.image, ball_OG.rect)
    screen.blit(ball_PL.image, ball_PL.rect)
    screen.blit(ball5.image, ball5.rect)
    screen.blit(ball6.image, ball6.rect)
    pygame.display.flip()
    clock.tick(60)
        
        
        
        
