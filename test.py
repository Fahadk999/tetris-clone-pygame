import pygame

from block import Block 

class BlockTemplate:
    width = 90
    height = 90
    speed = 3

    def __init__(self, g_width, g_height):
        self.g_width = g_width
        self.g_height = g_height
        self.landed = False

        self.x = g_width//2
        self.y = 0
        
        self.originBlock = Block(self.g_width, self.g_height, "red", x=self.x+30, y=self.y+30) 
        self.oneDown = Block(self.g_width, self.g_height, "blue", x=self.x+30, y=self.y+60) 

        self.smallBlocks = [
                self.originBlock,
                self.oneDown
                ]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def fall(self):
        if self.landed:
            return
        
        for b in self.smallBlocks:
            if b.rect.y + b.height >= self.g_height:
                self.originBlock.y = self.g_height - b.height 
                self.updateSmallBlocks()
                self.landed = True
                return

        self.originBlock.y += self.speed
        self.updateSmallBlocks()

    def updateSmallBlocks(self):
        x = self.originBlock.x
        y = self.originBlock.y

        self.oneDown.setPosition(x, y+30)

    def draw(self, screen):
        for b in self.smallBlocks:
            b.draw(screen)

