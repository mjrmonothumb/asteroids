from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		
	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

	def update(self, dt):
		self.position = self.position + self.velocity * dt

	def split(self):
		self.kill()
		if self.radius < ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		velocity = self.velocity.copy()
		velocity.rotate(random_angle)
		velocity_2 = self.velocity.copy()
		velocity_2.rotate(-random_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid_1.velocity = velocity * 1.2
		asteroid_2.velocity = velocity_2 * 1.2
		
		
