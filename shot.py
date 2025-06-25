from circleshape import CircleShape
import pygame

class Shot(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=1)
	
	def update(self, dt):
		self.position = self.position + self.velocity * dt
SHOT_RADIUS = 5

