import pygame

from square import Square

class LBlock(Square):
    width = 90
    # height is same 60
    # speed is same

    width1 = width // 3 # 30 for 90
    width2 = width * 2/3 # 60 for 90
    
    def __init__(self, g_width, g_height, color):
        super().__init__(g_width, g_height, color)

        self.rotation = 0 # 0 for normal 4=0 to normal position

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

        # colliders to fit shape

        self.body = pygame.Rect(self.x, self.y, self.width, self.height)
        self.verticalRect = pygame.Rect(self.x, self.y, self.width1, self.height)
        self.horizontalRect = pygame.Rect(self.x + self.width1, self.y, self.width2, self.height//2)

        self.rect = (
                self.verticalRect,
                self.horizontalRect
            )
    
    def fall(self, otherBlocks):
        if self.isGrounded:
            return

        nextY = self.body.y + self.speed
        nextVerticalY = self.verticalRect.y + self.speed
        nextHorizontalY = self.horizontalRect.y + self.speed

        if nextY + self.height >= self.g_height:
            self.body.y = self.g_height - self.height
            self.updateSmallBlocks()
            self.groundBlock()
            return

        nextRectVertical = pygame.Rect(self.verticalRect.x, nextVerticalY, self.width1, self.height)
        nextRectHorizontal = pygame.Rect(self.horizontalRect.x, nextHorizontalY, self.width2, self.height//2)

        for other in otherBlocks:
            if isinstance(other.rect, pygame.Rect):
                if other is self:
                    continue
                
                if nextRectVertical.colliderect(other.rect):
                    self.body.y = other.rect.y - self.height 
                    self.updateSmallBlocks()
                    self.groundBlock()
                    return

                elif nextRectHorizontal.colliderect(other.rect):
                    self.body.y = other.rect.y - self.height//2 if self.rotation == 0 else other.rect.y - self.height
                    self.updateSmallBlocks()
                    self.groundBlock()
                    return
            elif isinstance(other.rect, tuple):
                if other is self:
                    continue

                for collider in other.rect:
                    if nextRectVertical.colliderect(collider):
                        self.body.y = collider.y - self.height
                        self.updateSmallBlocks()
                        self.groundBlock()
                        return

                    elif nextRectHorizontal.colliderect(collider):
                        self.body.y = collider.y - self.height//2 if self.rotation == 0 else collider.y - self.height
                        self.updateSmallBlocks()
                        self.groundBlock()
                        return
                        
        self.body.y = nextY
        self.updateSmallBlocks()

    def move(self, key, otherBlocks):
        if not self.isGrounded:
            if key == pygame.K_a and self.body.x > 0:
                nextX = self.body.x - 30
                nextRectVertical = pygame.Rect(nextX, self.body.y, self.width1, self.height)
                nextRectHorizontal = pygame.Rect(nextX + self.height//2, self.body.y, self.width2, self.height//2)
                for other in otherBlocks:
                    if other is self:
                         continue
                    if isinstance(other.rect, pygame.Rect):
                        if nextRectVertical.colliderect(other.rect):
                            return
                        elif nextRectHorizontal.colliderect(other.rect):
                            return
                    elif isinstance(other.rect, tuple):
                        for collider in other.rect:
                            if nextRectVertical.colliderect(collider):
                                return
                            elif nextRectHorizontal.colliderect(collider):
                                return
                self.body.x = nextX
                self.updateSmallBlocks()

            if key == pygame.K_d and self.body.x + self.width < self.g_width:
                nextX = self.body.x + 30
                nextRectVertical = pygame.Rect(nextX, self.body.y, self.width1, self.height)
                nextRectHorizontal = pygame.Rect(nextX + self.height//2, self.body.y, self.width2, self.height//2)
                for other in otherBlocks:
                    if other is self:
                         continue
                    if isinstance(other.rect, pygame.Rect):
                        if nextRectVertical.colliderect(other.rect):
                            return
                        elif nextRectHorizontal.colliderect(other.rect):
                            return
                    elif isinstance(other.rect, tuple):
                        for collider in other.rect:
                            if nextRectVertical.colliderect(collider):
                                return
                            elif nextRectHorizontal.colliderect(collider):
                                return
                self.body.x = nextX
                self.updateSmallBlocks()

            if key == pygame.K_r:
                self.rotate()
                self.updateSmallBlocks()

    def updateSmallBlocks(self):
        x = self.body.x
        y = self.body.y
        
        match self.rotation:
            case 0:
                self.verticalRect.x = x
                self.verticalRect.y = y
                self.horizontalRect.x = x + self.width1
                self.horizontalRect.y = y

                self.topLeft.setPosition(x, y)
                self.oneDown.setPosition(x, y + self.height//2)
                self.oneRight.setPosition(x + self.width1, y)
                self.twoRight.setPosition(x + self.width2, y)
            case 1:
                self.verticalRect.x = x + self.width2
                self.verticalRect.y = y
                self.horizontalRect.x = x
                self.horizontalRect.y = y + self.height//2

                self.topLeft.setPosition(x, y + self.height//2)
                self.oneRight.setPosition(x + self.width1, y + self.height//2)
                self.oneDown.setPosition(x + self.width2, y + self.height//2) 
                self.twoRight.setPosition(x + self.width2, y)

    def rotate(self):
        if not self.rotation == 1:
            self.rotation += 1
        else:
            self.rotation = 0

    def updateBody(self):
        self.body = pygame.Rect(self.)
