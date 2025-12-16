import pygame

from lblock import LBlock

class SnakeBlock(LBlock):
    # width = 90
    # height = 60

    def __init__(self, g_width, g_height, color):
        super().__init__(g_width, g_height, color)
        
        w = self.topLeft.width
        h = self.topLeft.height
        
        self.oneDown.setPosition(self.x + self.width1, self.y + self.height1)
        self.twoRight.setPosition(self.x + self.width2, self.y + self.height1)

        self.verticalRect = pygame.Rect(self.x + self.width1, self.y + self.height1, self.height1, self.width1)
        self.horizontalRect = pygame.Rect(self.x, self.y, self.height1, self.width1)

    def updateSmallBlocks(self):
        x = self.body.x
        y = self.body.y

        if self.rotation == 0:
            self.setBodyHorizontal()
            # only verticalRect needs setting
            self.verticalRect = pygame.Rect(x + self.width1, y + self.height1, self.height1, self.width1)
            self.horizontalRect.x = x
            self.horizontalRect.y = y




    def rotate(self):
        self.rotation = 1 if not self.rotation == 1 else 0

    # maybe redo: the collider update idk rn


        
