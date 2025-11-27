import pygame

from square import Square

class LBlock(Square):
    width = 90
    # height is same
    # speed is same

    width1 = self.width // 3 # 30 for 90
    width2 = self.width * 2/3 # 60 for 90
    
    def __init__(self, g_width, g_height, color):
        super().__init__(g_width, g_height, color)

        # topLeft block is same
        w = self.topLeft.width
        h = self.topLeft.height

        # --- Reset pos for twoRight ---
        self.botRight.setPosition(self.x + w*2, self.y)
        # ------------------------------

        self.oneRight = self.topRight
        self.oneDown = self.botLeft
        self.twoRight = self.botRight

        self.smallBlocks = (
            self.topLeft,
            self.oneRight,
            self.twoRight,
            self.oneDown
        )

        # change collider to fit shape
        self.verticalRect = pygame.Rect(self.x, self.y, self.width1, self.height)
        self.horizontalRect = pygame.Rect(self.x + self.width1, self.y, self.width2, self.height//2)

        self.rect[] = (
                self.verticalRect,
                self.horizontalRect
            )

    def fall(self, otherBlocks):
        if self.isGrounded:
            return

        nextVerticlY = self.verticalRect.y + self.speed
        nextHorizontalY = self.horizontalRect.y + self.speed

        if nextVerticlY + self.height >= self.g_height:
            for rect in self.rect:
                rect.y = self.g_height - self.height
            self.updateSmallBlocks()
            self.groundBlock()
            return

        nextRectVertical = pygame.Rect(self.rect.x, nextVerticlY, self.width1, self.height)
        nextRectHorizontal = pygame.Rect(self.rect.x, nextHorizontalY, self.width2, self.height//2)

        for other in otherBlocks:
            if other is self:
                continue
            
            if nextRectVertical.colliderect(other.rect):
                self.rect.y = other.rect.y - self.height
                self.updateColliders()
                self.updateSmallBlocks()
                self.groundBlock()
                return

            elif nextRectHorizontal.colliderect(other.rect):
                self.rect.y = other.rect.y - self.height//2
                self.updateColliders()
                self.updateSmallBlocks()
                self.groundBlock()
                return

    def updateSmallBlocks(self):
        x = self.rect[0].x
        y = self.rect[0].y

        self.topLeft.setPosition(x, y)
        self.oneDown.setPosition(x, y + self.height//2)
        self.oneRight.setPosition(x + self.width1, y)
        self.twoRight.setPosition(x + self.width2, y)
    
#    def updateColliders(self):
#        x = self.rect.x
#        y = self.rect.y
#
#        self.verticalRect.y = y
#        self.verticalRect.x = x
#        self.horizontalRect.y = y
#        self.horizontalRect.x = x + self.width1
