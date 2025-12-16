import pygame
from random import randint

from colors import Color
from surface import Surface
from square import Square
from lblock import LBlock
from lineblock import LineBlock
from otherlblock import OtherLBlock

class Game:
    SPAWN_BLOCK_EVENT = pygame.event.custom_type()

    def __init__(self, s_width, s_height):
        self.s_width = s_width
        self.s_height = s_height
        self.gameSurface = Surface(600, 800, 0, 0, (196, 165, 135))
        self.g_width = self.gameSurface.width
        self.g_height = self.gameSurface.height
        self.blocks = []

    def draw(self, screen):
        self.gameSurface.draw(screen)
        for block in self.blocks:
            block.draw(screen)

    def update(self):
        for block in self.blocks:
            block.fall(self.blocks)
        self.checkEvent()

    def spawnBlock(self):
        square = Square(self.g_width, self.g_height, Color.BLUE)
        lblock = LBlock(self.g_width, self.g_height, Color.RED)
        lineBlock = LineBlock(self.g_width, self.g_height, Color.PURPLE)
        otherLBlock = OtherLBlock(self.g_width, self.g_height, "green")
        
        spawnblocks = [
                otherLBlock
            ]

        newShape = spawnblocks[randint(0, len(spawnblocks) - 1)]
        self.blocks.append(newShape)

    def handleEvent(self, event):
        if event.type == self.SPAWN_BLOCK_EVENT:
            self.spawnBlock()
        elif event.type == pygame.KEYDOWN:
            for block in self.blocks:
                block.move(event.key, self.blocks)

    def checkEvent(self):
        if not self.blocks or self.blocks[len(self.blocks)-1].isGrounded:
            pygame.event.post(pygame.event.Event(self.SPAWN_BLOCK_EVENT))
