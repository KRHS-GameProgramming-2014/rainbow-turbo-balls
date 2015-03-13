import pygame, math

class Ball():
    def __init__(self, color, speed = [0,0], pos = [0,0]):
        if color == "purple":
            self.image = pygame.image.load("RSC/AI Balls/PL_AI_B.png")
            self.color = color
            self.value = 1
        elif color == "red":
            self.image = pygame.image.load("RSC/AI Balls/RD_AI_B.png")
            self.color = color
            self.value = 2
        elif color == "orange":
            self.image = pygame.image.load("RSC/AI Balls/OG_AI_B.png")
            self.color = color
            self.value = 3
        elif color == "yellow":
            self.image = pygame.image.load("RSC/AI Balls/YW_AI_B.png")
            self.color = color
            self.value = 5
        elif color == "green":
            self.image = pygame.image.load("RSC/AI Balls/GN_AI_B.png")
            self.color = color
            self.value = 6
        elif color == "blue":
            self.image = pygame.image.load("RSC/AI Balls/BL_AI_B.png")
            self.color = color
            self.value = 7
        elif color == "black":
            self.image = pygame.image.load("RSC/Player AI Balls/BK_AI_B.png")
            self.color = color
            self.value = 4
        elif color == "white":
            self.image = pygame.image.load("RSC/AI Balls/WT_AI_B.png")
            self.color = color
            self.value = 4
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        #self.maxSpeed = 4
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.living = True

    def place(self, pos):
        self.rect.center = pos

    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)

    def move(self):
        self.rect = self.rect.move(self.speed)

    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                

    def collideBall(self, other):
        if self != other:
            #print "trying to hit Ball"
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
    
    def collideAIBall(self, other):
        if self != other:
            #print "trying to hit Ball"
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.living = False
                        return [PlayerAI(other.color, self.rect.center)]
        return []

    def collidePBall(self, other):
        if self != other:
            #print "trying to hit Ball"
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.living = False
                        return [PlayerAI(other.color, self.rect.center)] 
        return []
    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))


class PBall():
    def __init__(self, color, pos = [0,0]):
        self.color = color
        if self.color == "white":
            self.image = pygame.image.load("RSC/Player Balls/WT_P_B.png")
        else:
            self.image = pygame.image.load("RSC/Player Balls/BK_P_B.png")
       
        self.rect = self.image.get_rect()
        self.place(pos)
        self.speedx = 0
        self.speedy = 0
        self.maxSpeed = 4
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
            
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)      
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
                #print "hit xWall"
    
    def place(self, pos):
        self.rect.center = pos

    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)

    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0

    def collideBall(self, other):
        if self != other:
            #print "trying to hit Ball"
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
                            #print "hit Ball"
                        #if self.change:
                            #self.image = self.altImage
                            #self.changed = True
    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
class PlayerAI(Ball):
    def __init__(self, color, pos):
        Ball.__init__(self, color.lower(), [4,4], pos)
        
    def collideAIBall(self, other):
        if self != other:
            #print "trying to hit Ball"
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.living = False
                        return [PlayerAI(other.color, self.rect.center)]
        return []
