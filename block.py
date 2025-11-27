import pygame

from time import sleep

class Block:
    width = 30
    height = 30
    speed = 3

    def __init__(self, g_width, g_height, color, x=0, y=0):
        self.g_width = g_width
        self.g_height = g_height
        self.x = self.g_width//2 if x == 0 else x
        self.y = 0 if y == 0 else y 
        self.color = color
        self.isGrounded = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def setPosition(self, x = 0, y = 0):
        self.rect.x = self.g_width//2 if x == 0 else x
        self.rect.y = 0 if y == 0 else y
