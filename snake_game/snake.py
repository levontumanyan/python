import pygame
import random

class Snake():
	min_length = 3

	def __init__(self, length = min_length, x = 0, y = 0, ) -> None:
		self.length = length
		self.speed = 1
		self.x = x
		self.y = y
		#possibly change the below to random choice.
		self.direction = "up"
		self.body = [[x, y] for _ in range(length)]

	def move(self):
        # Move the snake in the current direction
		if self.direction == "up":
			self.y -= 1
		elif self.direction == "down":
			self.y += 1
		elif self.direction == "left":
			self.x -= 1
		elif self.direction == "right":
			self.x += 1
		# Update the body
		for i in range(self.length - 1, 0, -1):
			self.body[i] = self.body[i - 1]
		self.body[0] = [self.x, self.y]

	def change_direction(self, new_direction):
		self.direction = new_direction

snake1 = Snake()

snakes = [Snake() for _ in range(100)]
#print(snakes)

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# # Update the snake's body
	# snake_body.insert(0, [snake_x, snake_y])
	# snake_body.pop()

	# # Draw the snake on the screen
	# for segment in snake_body:
	# 	pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(segment[0], segment[1], snake_size, snake_size))

	# Update the display
	pygame.display.flip()