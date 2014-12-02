import sys, pygame
pygame.init()

clock = pygame.time.Clock()

width = 900 
height = 850
size = width, height
speedx = 1
speedy = 1
speed = [speedx, speedy]
speedx2 = 2
speedy2 = 2
speed2 = [speedx2, speedy2]
speedx3 = 3
speedy3 = 3
speed3 = [speedx3, speedy3]
speedx4 = 5
speedy4 = 5
speed4 = [speedx4, speedy4]
speedx5 = 6
speedy5 = 6
speed5 = [speedx5, speedy5]
speedx5 = 7
speedy5 = 7
speed5 = [speedx6, speedy6]
bgColor = r,g,b = 0, 0, 0
#255 is limit

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Crt.png")
ballrect = ball.get_rect()
ball2 = pygame.image.load("Lbr.png")
ballrect2 = ball2.get_rect()
ball3 = pygame.image.load("Mat.png")
ballrect3 = ball3.get_rect()
ball4 = pygame.image.load("Spr.png")
ballrect4 = ball4.get_rect()
ball5 = pygame.image.load("Tgr.png")
ballrect5 = ball5.get_rect()
ballrect = ballrect.move(100, 500)
ballrect2 = ballrect2.move(200, 400)
ballrect3 = ballrect3.move(300, 300)
ballrect2 = ballrect4.move(400, 200)
ballrect2 = ballrect5.move(500, 100)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		
	ballrect2 = ballrect2.move(speed2)
	if ballrect2.left < 0 or ballrect2.right > width:
		speed2[0] = -speed2[0]
	if ballrect2.top < 0 or ballrect2.bottom > height:
		speed2[1] = -speed2[1]
		
	ballrect3 = ballrect3.move(speed3)
	if ballrect3.left < 0 or ballrect3.right > width:
		speed3[0] = -speed3[0]
	if ballrect3.top < 0 or ballrect3.bottom > height:
		speed3[1] = -speed3[1]
		
	ballrect4 = ballrect4.move(speed4)
	if ballrect4.left < 0 or ballrect4.right > width:
		speed4[0] = -speed4[0]
	if ballrect4.top < 0 or ballrect4.bottom > height:
		speed4[1] = -speed4[1]
		
	ballrect5 = ballrect5.move(speed5)
	if ballrect5.left < 0 or ballrect5.right > width:
		speed5[0] = -speed5[0]
	if ballrect5.top < 0 or ballrect5.bottom > height:
		speed5[1] = -speed5[1]
		
	if ballrect.right > ballrect2.left and ballrect.left < ballrect2.right:
		if ballrect.bottom > ballrect2.top and ballrect.top < ballrect2.bottom:
			speed[0] = -speed[0]
			speed[1] = -speed[1]
			speed2[0] = -speed2[0]
			speed2[1] = -speed2[1]
			
	if ballrect.right > ballrect3.left and ballrect.left < ballrect3.right:
		if ballrect.bottom > ballrect3.top and ballrect.top < ballrect3.bottom:
			speed[0] = -speed[0]
			speed[1] = -speed[1]
			speed3[0] = -speed3[0]
			speed3[1] = -speed3[1]
		
	if ballrect.right > ballrect4.left and ballrect.left < ballrect4.right:
		if ballrect.bottom > ballrect4.top and ballrect.top < ballrect4.bottom:
			speed[0] = -speed[0]
			speed[1] = -speed[1]
			speed4[0] = -speed4[0]
			speed4[1] = -speed4[1]
				
	if ballrect.right > ballrect5.left and ballrect.left < ballrect5.right:
		if ballrect.bottom > ballrect5.top and ballrect.top < ballrect5.bottom:
			speed[0] = -speed[0]
			speed[1] = -speed[1]
			speed5[0] = -speed5[0]
			speed5[1] = -speed5[1]
			
	if ballrect2.right > ballrect3.left and ballrect2.left < ballrect3.right:
		if ballrect2.bottom > ballrect3.top and ballrect2.top < ballrect3.bottom:
			speed2[0] = -speed2[0]
			speed2[1] = -speed2[1]
			speed3[0] = -speed3[0]
			speed3[1] = -speed3[1]
			
	if ballrect2.right > ballrect4.left and ballrect2.left < ballrect4.right:
		if ballrect2.bottom > ballrect4.top and ballrect2.top < ballrect4.bottom:
			speed2[0] = -speed2[0]
			speed2[1] = -speed2[1]
			speed4[0] = -speed4[0]
			speed4[1] = -speed4[1]
			
	if ballrect2.right > ballrect5.left and ballrect2.left < ballrect5.right:
		if ballrect2.bottom > ballrect5.top and ballrect2.top < ballrect5.bottom:
			speed2[0] = -speed2[0]
			speed2[1] = -speed2[1]
			speed5[0] = -speed5[0]
			speed5[1] = -speed5[1]
			
	if ballrect3.right > ballrect4.left and ballrect3.left < ballrect4.right:
		if ballrect3.bottom > ballrect4.top and ballrect3.top < ballrect4.bottom:
			speed3[0] = -speed3[0]
			speed3[1] = -speed3[1]
			speed4[0] = -speed4[0]
			speed4[1] = -speed4[1]
			
	if ballrect3.right > ballrect5.left and ballrect3.left < ballrect5.right:
		if ballrect3.bottom > ballrect5.top and ballrect3.top < ballrect5.bottom:
			speed3[0] = -speed3[0]
			speed3[1] = -speed3[1]
			speed5[0] = -speed5[0]
			speed5[1] = -speed5[1]
			
	if ballrect3.right > ballrect5.left and ballrect3.left < ballrect5.right:
		if ballrect3.bottom > ballrect5.top and ballrect3.top < ballrect5.bottom:
			speed4[0] = -speed4[0]
			speed4[1] = -speed4[1]
			speed5[0] = -speed5[0]
			speed5[1] = -speed5[1]
			
	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(ball, ballrect)
	screen.blit(ball2, ballrect2)
	screen.blit(ball3, ballrect3)
	screen.blit(ball4, ballrect4)
	screen.blit(ball5, ballrect5)
	pygame.display.flip()
	clock.tick(60)

