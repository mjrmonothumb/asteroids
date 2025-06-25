import pygame
from constants import *
from pygame.locals import *
from player import *
from asteroid import *
from shot import *
from asteroidfield import *
import sys


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)
asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable, )
shots = pygame.sprite.Group()
Shot.containers = (shots, updatable, drawable)

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	AsteroidField()
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.fill("black")
		updatable.update(dt)
		for asteroid in asteroids:
			if player.collisions(asteroid):
				print("Game over!")
				sys.exit("Game Over!")
		for asteroid in asteroids:
			for shoot in shots:
				if shoot.collisions(asteroid):
					shoot.kill()
					asteroid.split()


		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__== "__main__":
	main()


