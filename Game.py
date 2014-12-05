import pygame, sys, random
#from AIballs import AIballs
#from PlayerBall import PlayerBall
from Score import Score

pygame.init()

clock = pygame.time.Clock()

width = 1100 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

gs = Score('green', 'black')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()


	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(gs.image, gs.rect)
	pygame.display.flip()
	clock.tick(60)
