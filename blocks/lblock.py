import pygame

from blocks.square import Square

class LBlock(Square):
    width = 90
    height = 60

    width1 = width // 3 # 30 for 90
    width2 = width * 2/3 # 60 for 90
    height1 = height//2 # 30 for 60
    height2 = height * 3/2 # 90 for 30
    height3 = height # 60 for 60, this is for a const 60 value for later use
    
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
        self.horizontalRect = pygame.Rect(self.x + self.width1, self.y, self.width2, self.height1)

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
        nextRectHorizontal = pygame.Rect(self.horizontalRect.x, nextHorizontalY, self.width2, self.height1)

        for other in otherBlocks:
            if isinstance(other.rect, pygame.Rect):
                if other is self:
                    continue
                
                if nextRectVertical.colliderect(other.rect):
                    self.updateBodyVertical(other.rect)
                    return

                elif nextRectHorizontal.colliderect(other.rect):
                    self.updateBodyHorizontal(other.rect)
                    return
            elif isinstance(other.rect, tuple):
                if other is self:
                    continue

                for collider in other.rect:
                    if nextRectVertical.colliderect(collider):
                        self.updateBodyVertical(collider)
                        return

                    elif nextRectHorizontal.colliderect(collider):
                        self.updateBodyHorizontal(collider)
                        return
                        
        self.body.y = nextY
        self.updateSmallBlocks()

    def move(self, key, otherBlocks):
        if not self.isGrounded:
            if key in (pygame.K_a, pygame.K_LEFT) and self.body.x > 0:
                nextX = self.body.x - 30
                nextRectVertical = pygame.Rect(nextX, self.body.y, self.width1, self.height)
                nextRectHorizontal = pygame.Rect(nextX + self.height1, self.body.y, self.width2, self.height1)
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

            if key in (pygame.K_d, pygame.K_RIGHT) and self.body.x + self.width < self.g_width:
                nextX = self.body.x + 30
                nextRectVertical = pygame.Rect(nextX, self.body.y, self.width1, self.height)
                nextRectHorizontal = pygame.Rect(nextX + self.height1, self.body.y, self.width2, self.height1)
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
                self.setBodyHorizontal()
                self.verticalRect.x = x
                self.verticalRect.y = y
                self.horizontalRect.x = x + self.width1
                self.horizontalRect.y = y

                self.topLeft.setPosition(x, y)
                self.oneDown.setPosition(x, y + self.height1) 
                self.oneRight.setPosition(x + self.width1, y)
                self.twoRight.setPosition(x + self.width2, y)
            case 1:
                self.setBodyHorizontal()
                self.verticalRect.x = x + self.width2
                self.verticalRect.y = y
                self.horizontalRect.x = x
                self.horizontalRect.y = y + self.height1

                self.topLeft.setPosition(x, y + self.height1)
                self.oneRight.setPosition(x + self.width1, y + self.height1)
                self.oneDown.setPosition(x + self.width2, y + self.height1)
                self.twoRight.setPosition(x + self.width2, y)
            case 2:
                self.setBodyVertical()
                self.verticalRect.x = x + self.height1
                self.verticalRect.y = y + self.width1
                self.horizontalRect.x = x
                self.horizontalRect.y = y

                self.topLeft.setPosition(x + self.width1, y)
                self.oneDown.setPosition(x, y)
                self.oneRight.setPosition(x + self.width1, y + self.height1)
                self.twoRight.setPosition(x + self.width1, y + self.height3)
            case 3:
                self.setBodyVertical()
                self.verticalRect.x = x
                self.verticalRect.y = y
                self.horizontalRect.x = x
                self.horizontalRect.y = y + self.height3

                self.topLeft.setPosition(x, y)
                self.oneRight.setPosition(x, y + self.height1)
                self.twoRight.setPosition(x, y + self.height3)
                self.oneDown.setPosition(x + self.width1, y + self.height3)

    def rotate(self):
        if not self.rotation == 3:
            self.rotation += 1
        else:
            self.rotation = 0

    def setBodyVertical(self):
        x = self.body.x
        y = self.body.y

        self.width = 60
        self.height = 90

        self.body = pygame.Rect(x, y, self.width, self.height)

    def setBodyHorizontal(self):
        x = self.body.x
        y = self.body.y

        self.width = 90
        self.height = 60

        self.body = pygame.Rect(x, y, self.width, self.height)
        
    def updateBodyHorizontal(self, collider):
        match self.rotation:
            case 0:
                self.body.y = collider.y - self.height1
                self.updateSmallBlocks()
                self.groundBlock()
            case 1:
                self.body.y = collider.y - self.height
                self.updateSmallBlocks()
                self.groundBlock()
            case 2:
                self.body.y = collider.y - self.height1
                self.updateSmallBlocks()
                self.groundBlock()
            case 3:
                self.body.y = collider.y - self.height2
                self.updateSmallBlocks()
                self.groundBlock()

    def updateBodyVertical(self, collider):
        match self.rotation:
            case 0:
                self.body.y = collider.y - self.height
                self.updateSmallBlocks()
                self.groundBlock()
            case 1:
                self.body.y = collider.y - self.height
                self.updateSmallBlocks()
                self.groundBlock()
            case 2:
                self.body.y = collider.y - self.height2
                self.updateSmallBlocks()
                self.groundBlock()
            case 3:
                self.body.y = collider.y - self.height2
                self.updateSmallBlocks()
                self.groundBlock()

