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
