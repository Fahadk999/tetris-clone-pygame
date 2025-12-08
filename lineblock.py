import pygame

from square import Square

# make rotations for lblock also

class LineBlock(Square):
    width = 30
    height = 120

    height1 = height//2 # 60 for 120
    height2 = height * 1/4 # 30 for 120
    height3 = height * 3/4 # 90 for 120

    def __init__(self, g_height, g_width, color):
        super().__init__(g_height, g_width, color)

        # origin block
        self.blockOne = self.topLeft

        self.blockTwo = self.botLeft

        self.topRight.setPosition(self.x, self.y + self.height1)
        self.botRight.setPosition(self.x, self.y + self.height3)
        self.blockThree = self.topRight
        self.blockFour = self.botRight

        self.smallBlocks = (
                self.blockOne,
                self.blockTwo,
                self.blockThree,
                self.blockFour
        )

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def updateSmallBlocks(self):
        x = self.rect.x
        y = self.rect.y

        self.blockOne.setPosition(x, y)
        self.blockTwo.setPosition(x, y + self.height2)
        self.blockThree.setPosition(x, y + self.height1)
        self.blockFour.setPosition(x, y + self.height3)


