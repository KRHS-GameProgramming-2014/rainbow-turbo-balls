import pygame, math

class Ball():
    def __init__(self, image, speed = [0,0], pos = [0,0], altImage = None):
        if altImage:
            self.normImage = pygame.image.load(image)
            self.altImage = pygame.image.load(altImage)
            self.image = self.normImage
            self.change = True
            self.timerMax = 1*60
            self.timer = 0
            self.changed = False
        else:
            self.image = pygame.image.load(image)
            self.change = False
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self, width, height):
        if self.change:
            if self.changed:
                if self.timer < self.timerMax:
                    self.timer += 1
                else:
                    self.timer = 0
                    self.image = self.normImage
                    self.changed = False

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
                #print "hit xWall"

    def collideBall(self, other):
        if self != other:
        #print "trying to hit Ball"
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    #if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
                            #print "hit Ball"
                        if self.change:
                            self.image = self.altImage
                            self.changed = True

    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))


class PBall():
    def __init__(self, pos):
        Ball.__init__(self, "images/Player/pballbu.png", [0,0], pos)
        self.upImages = [pygame.image.load("images/Player/pballru.png"),
                         pygame.image.load("images/Player/pballgu.png"),
                         pygame.image.load("images/Player/pballbu.png")]
        self.downImages = [pygame.image.load("images/Player/pballrd.png"),
                           pygame.image.load("images/Player/pballgd.png"),
                           pygame.image.load("images/Player/pballbd.png")]
        self.leftImages = [pygame.image.load("images/Player/pballrl.png"),
                           pygame.image.load("images/Player/pballgl.png"),
                           pygame.image.load("images/Player/pballbl.png")]
        self.rightImages = [pygame.image.load("images/Player/pballrr.png"),
                            pygame.image.load("images/Player/pballgr.png"),
                            pygame.image.load("images/Player/pballbr.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 10
            
    def update(self, width, height):
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
        
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
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
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





   
    #def __init__(self, image, speed = [0,0], pos = [0,0], altImage = None):
        #if altImage:
            #self.normImage = pygame.image.load(image)
            #self.altImage = pygame.image.load(altImage)
            #self.image = self.normImage
            #self.change = True
            #self.timerMax = 1*60
            #self.timer = 0
            #self.changed = False
        #else:
            #self.image = pygame.image.load(image)
            #self.change = False
        #self.rect = self.image.get_rect()
        #self.speedx = speed[0]
        #self.speedy = speed[1]
        #self.speed = [self.speedx, self.speedy]
        #self.place(pos)
        #self.didBounceX = False
        #self.didBounceY = False

    #def update(self, width, height):
        #if self.change:
            #if self.changed:
                #if self.timer < self.timerMax:
                    #self.timer += 1
                #else:
                    #self.timer = 0
                    #self.image = self.normImage
                    #self.changed = False

        #self.didBounceX = False
        #self.didBounceY = False
        #self.speed = [self.speedx, self.speedy]
        #self.move()
        #self.collideWall(width, height)

    #def move(self):
        #self.rect = self.rect.move(self.speed)

    #def collideWall(self, width, height):
        #if not self.didBounceX:
            ##print "trying to hit Wall"
            #if self.rect.left < 0 or self.rect.right > width:
                #self.speedx = -self.speedx
                #self.didBounceX = True
                ##print "hit xWall"
        #if not self.didBounceY:
            #if self.rect.top < 0 or self.rect.bottom > height:
                #self.speedy = -self.speedy
                #self.didBounceY = True
                ##print "hit xWall"

    #def collideBall(self, other):
        ##print "trying to hit Ball"
        #if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            #if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                ##if (self.radius + other.radius) > self.distance(other.rect.center):
                    #if not self.didBounceX:
                        #self.speedx = -self.speedx
                        #self.didBouncex = True
                    #if not self.didBounceY:
                        #self.speedy = -self.speedy
                        #self.didBounceY = True
                        ##print "hit Ball"
                    #if self.change:
                        #self.image = self.altImage
                        #self.changed = True
        
        #if self.changed:    
            #if self.facing == "up":
                #self.images = self.upImages
            #elif self.facing == "down":
                #self.images = self.downImages
            #elif self.facing == "right":
                #self.images = self.rightImages
            #elif self.facing == "left":
                #self.images = self.leftImages
            
            #self.image = self.images[self.frame]
    
    #def go(self, direction):
        #if direction == "up":
            #self.facing = "up"
            #self.changed = True
            #self.speedy = -self.maxSpeed
        #elif direction == "stop up":
            #self.speedy = 0
        #elif direction == "down":
            #self.facing = "down"
            #self.changed = True
            #self.speedy = self.maxSpeed
        #elif direction == "stop down":
            #self.speedy = 0
            
        #if direction == "right":
            #self.facing = "right"
            #self.changed = True
            #self.speedx = self.maxSpeed
        #elif direction == "stop right":
            #self.speedx = 0
        #elif direction == "left":
            #self.facing = "left"
            #self.changed = True
            #self.speedx = -self.maxSpeed
        #elif direction == "stop left":
            #self.speedx = 0





    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
