import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, option):
		super().__init__()
		self.option = option
		self.make_animation = True
		self.sprites = []
		self.sprites.append(pygame.image.load('mario_2.png'))
		self.sprites.append(pygame.image.load('mario_4.png'))

		self.sprites2 = []
		self.sprites2.append(pygame.image.load('mario_2.png'))
		self.sprites2.append(pygame.image.load('mario_4.png'))

		self.sprites3 = []
		self.sprites3.append(pygame.image.load('mario_3.png'))
		self.sprites3.append(pygame.image.load('mario_4.png'))

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def update(self,speed):
		if self.option == 1:
			self.current_sprite += 0.05
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0

			self.image = self.sprites[int(self.current_sprite)]
		elif self.option == 2:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites2):
				self.current_sprite = 0

			self.image = self.sprites2[int(self.current_sprite)]
		elif self.option == 3:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites3):
				self.current_sprite = 0

			self.image = self.sprites3[int(self.current_sprite)]
# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(30,100,1)
player2 = Player(142,100,2)
player3 = Player(250,100,3)
moving_sprites.add(player)
moving_sprites.add(player2)
moving_sprites.add(player3)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Drawing
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.08)
	pygame.display.flip()
	clock.tick(60)