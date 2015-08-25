import pygame

class CMovingHead:
	def __init__(self):
		self.bg_color = 255, 255, 255
		self.head_color = 255, 0, 0
		self.eye_color = 0, 0, 255
		self.mouth_color = 0, 255, 0
		self.head_pos = 

	def add_head(self, head_color, pos):
		pygame.draw.rect(self.screen, head_color, pos, 0)

	def add_eye(self, eye_color, point):
		pygame.draw.circle(self.screen, eye_color, point, radius, 0)

	def add_mouth(self):
		pygame.draw.arc(self.screen, color, position, start_angle, end_angle, width)