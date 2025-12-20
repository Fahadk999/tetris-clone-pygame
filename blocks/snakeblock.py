import pygame

from blocks.lblock import LBlock

class SnakeBlock(LBlock):
    # width = 90
    # height = 60

    def __init__(self, g_width, g_height, color):
        super().__init__(g_width, g_height, color)
        w = self.topLeft.width
        h = self.topLeft.height
        
        # topLeft and oneRight are the same of lblock
        self.oneDown.setPosition(self.x + self.width1, self.y + self.height1)
        self.twoRight.setPosition(self.x + self.width2, self.y + self.height1)

        self.body = pygame.Rect(self.x, self.y, self.width, self.height)
        self.verticalRect = pygame.Rect(self.x + self.width1, self.y + self.height1, self.width2, self.height1)
        self.horizontalRect = pygame.Rect(self.x, self.y, self.width2, self.height1)

        self.smallBlocks = (
            self.topLeft,
            self.oneRight,
            self.twoRight,
            self.oneDown
        )

        self.rect = (
                self.verticalRect,
                self.horizontalRect
            )

    def updateSmallBlocks(self):
        x = self.body.x
        y = self.body.y

        if self.rotation == 0:
            self.setBodyHorizontal()
            # only verticalRect needs setting
            self.verticalRect = pygame.Rect(x + self.width1, y + self.height1, self.width2, self.height1)
            self.horizontalRect = pygame.Rect(x, y, self.width2, self.height1)
            self.rect = (
                    self.verticalRect,
                    self.horizontalRect
                )

            self.topLeft.setPosition(x, y)
            self.oneRight.setPosition(x + self.width1, y)
            self.oneDown.setPosition(x + self.width1, y + self.height1)
            self.twoRight.setPosition(x + self.width2, y + self.height1)

        elif self.rotation == 1:
            self.setBodyVertical()
            self.verticalRect = pygame.Rect(x + self.width1, y + self.height1, self.width1, self.height3)
            self.horizontalRect = pygame.Rect(x, y, self.width1, self.height3)
            self.rect = (
                    self.verticalRect,
                    self.horizontalRect
                )

            self.topLeft.setPosition(x + self.width1, y)
            self.oneRight.setPosition(x + self.width1, y + self.height1)
            self.oneDown.setPosition(x, y + self.height1)
            self.twoRight.setPosition(x, y + self.height3)
            
    def rotate(self):
        self.rotation ^= 1
        self.updateSmallBlocks()

    # maybe redo: the collider update idk rn

    def updateBodyHorizontal(self, collider):
        if self.rotation == 0:
            self.body.y = collider.y - self.height1
            self.updateSmallBlocks()
            self.groundBlock()
        elif self.rotation == 1:
            self.body.y = collider.y - self.height3
            self.updateSmallBlocks()
            self.groundBlock()

    def updateBodyVertical(self, collider):
        if self.rotation == 0:
            self.body.y = collider.y - self.height3
            self.updateSmallBlocks()
            self.groundBlock()
        elif self.rotation == 1:
            self.body.y = collider.y - self.height
            self.updateSmallBlocks()
            self.groundBlock()
