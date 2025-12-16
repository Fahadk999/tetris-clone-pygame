import pygame

from lblock import LBlock

class OtherLBlock(LBlock):

    def __init__(self, g_width, g_height, color):
        super().__init__(g_width, g_height, color)
        w = self.topLeft.width
        h = self.topLeft.height

        # --- Reset pos for oneDown ---
        self.botLeft.setPosition(self.x + w*2, self.y + w)
        # ------------------------------

        self.oneDown = self.botLeft

        self.smallBlocks = (
            self.topLeft,
            self.oneRight,
            self.twoRight,
            self.oneDown
        )

        # colliders to fit shape
        self.body = pygame.Rect(self.x, self.y, self.width, self.height)
        self.verticalRect = pygame.Rect(self.x, self.y, self.width1, self.height)
        self.horizontalRect = pygame.Rect(self.x + self.width1, self.y, self.width2, self.height1)

        self.rect = (
                self.verticalRect,
                self.horizontalRect
            )
    
    def updateSmallBlocks(self):
        # only edit oneDown for horizontal
        x = self.body.x
        y = self.body.y
        
        match self.rotation:
            case 0:
                self.setBodyHorizontal()
                self.verticalRect.x = x + self.width2
                self.verticalRect.y = y
                self.horizontalRect.x = x
                self.horizontalRect.y = y

                self.topLeft.setPosition(x, y)
                self.oneDown.setPosition(x + self.width2, y + self.height1) 
                self.oneRight.setPosition(x + self.width1, y)
                self.twoRight.setPosition(x + self.width2, y)
            case 1:
                self.setBodyHorizontal()
                self.verticalRect.x = x
                self.verticalRect.y = y
                self.horizontalRect.x = x + self.width1
                self.horizontalRect.y = y + self.height1

                self.topLeft.setPosition(x, y + self.height1)
                self.oneRight.setPosition(x + self.width1, y + self.height1)
                self.oneDown.setPosition(x + self.width2, y + self.height1)
                self.twoRight.setPosition(x, y)
            case 2:
                self.setBodyVertical()
                self.verticalRect.x = x
                self.verticalRect.y = y + self.width1
                self.horizontalRect.x = x
                self.horizontalRect.y = y

                self.topLeft.setPosition(x + self.width1, y)
                self.oneDown.setPosition(x, y)
                self.oneRight.setPosition(x, y + self.height1)
                self.twoRight.setPosition(x, y + self.height3)
            case 3:
                self.setBodyVertical()
                self.verticalRect.x = x + self.width1
                self.verticalRect.y = y
                self.horizontalRect.x = x
                self.horizontalRect.y = y + self.height3

                self.topLeft.setPosition(x + self.width1, y)
                self.oneRight.setPosition(x + self.width1, y + self.height1)
                self.twoRight.setPosition(x, y + self.height3)
                self.oneDown.setPosition(x + self.width1, y + self.height3)
