
class Score():
	def __init__(self, color, owner, width=1100, height=700):
		self.score = 0
		self.maxScore = 999
		self.fontSize = 15
		self.font = pygame.font.Font(None, self.fontSize)
		if color == 'green':
			self.baseImage = pygame.image.load('RSC/Scores/Green.png')
			self.rect = self.baseImage.get_rect()
			self.value = 6
			self.textColor = [0,255,0]
			if owner == 'black':
				self.place([400, 25])
			else:
				self.place([width-400, Hight-25])
		self.text = str(self.score)
		self.textImage = self.font.render(self.text, 1, self.textColor)
		self.textRect = self.textImage.get_rect(center = self.rect.center)
		self.image = self.baseImage.blit(self.textImage, self.textRect)
		self.change = False
		
	def place(self, pos):
		self.rect.center = pos
			
	def update(self):
		if self.change:
			self.textImage = self.font.render(self.text, 1, self.textColor)
			self.textRect = self.textImage.get_rect(center = self.rect.center)
			self.image = self.baseImage.blit(self.textImage, self.textRect)
			self.change = False
	
	def setScore(self, score):
		self.score = score
		self.change = True
		
	def increaseScore(self):
		self.score += self.value
		if self.score > self.maxScore:
			self.score = self.maxScore
		self.change = True
		
	def resetScore(self):
		self.score = 0
		self.change = True

#timer = Score([75, 25], [64,64,64] "Score: ", 20)
#timerWait = 0
#timerWaitMax = 6

scoreBK_WT = Score([25, 25], 20)
scoreBK_PL = Score([100, 25], [128,0,255], 20)
scoreBK_RD = Score([175, 25], [255,0,0], 20)
scoreBK_OG = Score([250, 25], [255,128,0], 20)
scoreBK_YW = Score([325, 25], [255,255,0], 20)
scoreBK_GN = Score([400, 25], [0,255,0], 20)
scoreBK_BL = Score([475, 25], [0,192,255], 20)


scoreWT_BK = Score([width-25, Hight-25], 20)
scoreWT_PL = Score([width-100, Hight-25], [128,0,255], 20)
scoreWT_RD = Score([width-175, Hight-25], [255,0,0], 20)
scoreWT_OG = Score([width-250, Hight-25], [255,128,0], 20)
scoreWT_YW = Score([width-325, Hight-25], [255,255,0], 20)
scoreWT_GN = Score([width-400, Hight-25], [0,255,0], 20)
scoreWT_BL = Score([width-475, Hight-25], [0,192,255], 20)

nbrBK_WT = Score([75, 25], 20)
nbrBK_PL = Score([150, 25], [128,0,255], 20)
nbrBK_RD = Score([225, 25], [255,0,0], 20)
nbrBK_OG = Score([300, 25], [255,128,0], 20)
nbrBK_YW = Score([375, 25], [255,255,0], 20)
nbrBK_GN = Score([450, 25], [0,255,0], 20)
nbrBK_BL = Score([525, 25], [0,192,255], 20)

#MAX 99

nbrWT_BK = Score([[width-75, Hight-25], 20)
nbrWT_PL = Score([width-150, Hight-25], [128,0,255], 20)
nbrWT_RD = Score([width-225, Hight-25], [255,0,0], 20)
nbrWT_OG = Score([width-300, Hight-25], [255,128,0], 20)
nbrWT_YW = Score([width-375, Hight-25], [255,255,0], 20)
nbrWT_GN = Score([width-450, Hight-25], [0,255,0], 20)
nbrWT_BL = Score([width-525, Hight-25], [0,192,255], 20)
