import pygame

from block import Block

class Square:
    width = 60
    height = 60
    speed = 3

    def __init__(self, g_width, g_height, color):
        self.g_width = g_width
        self.g_height = g_height

        # The "origin block" of the square
        self.topLeft = Block(g_width, g_height, color)

        # Compute relative blocks
        b = self.topLeft
        w = b.width
        h = b.height
        self.x = self.topLeft.rect.x
        self.y = self.topLeft.rect.y
        
        self.topRight = Block(g_width, g_height, color, self.x + w, self.y)
        self.botLeft = Block(g_width, g_height, color, self.x, self.y + h)
        self.botRight = Block(g_width, g_height, color, self.x + w, self.y + h)

        self.smallBlocks = (
            b,
            self.topRight,
            self.botLeft,
            self.botRight
        )

        self.rect = pygame.Rect(self.x, self.y, w*2, h*2)

        self.isGrounded = False

    def draw(self, screen):
        for block in self.smallBlocks:
            block.draw(screen)

    def fall(self, otherBlocks):
        if self.isGrounded:
            return
        
        # bottom blocks check fall
        nextY = self.rect.y + self.speed
        # make a long rect to check bottom two blocks colliders
        if nextY + self.height >= self.g_height:
            self.rect.y = self.g_height - self.height
            self.updateSmallBlocks()
            self.groundBlock()
            return

        nextRect = pygame.Rect(self.rect.x, nextY, self.width, self.height)

        for other in otherBlocks:
            if isinstance(other.rect, pygame.Rect):
                if other is self:
                    continue

                if nextRect.colliderect(other.rect):
                    self.rect.y = other.rect.y - self.height
                    self.updateSmallBlocks()
                    self.groundBlock()
                    return
            elif isinstance(other.rect, tuple):
                if other is self:
                    continue

                for collider in other.rect:
                    if nextRect.colliderect(collider):
                        self.rect.y = collider.y - self.height
                        self.updateSmallBlocks()
                        self.groundBlock()
                        return
        
        self.rect.y = nextY
        self.updateSmallBlocks()

    def move(self, key, otherBlocks):
        if not self.isGrounded:
            if key == pygame.K_a and self.rect.x > 0:
                nextX = self.rect.x - 30
                nextRect = pygame.Rect(nextX, self.rect.y, self.rect.width, self.rect.height)
                for other in otherBlocks:
                    if other is self:
                        continue
                    if isinstance(other.rect, pygame.Rect):
                        if nextRect.colliderect(other.rect):
                            return
                    elif isinstance(other.rect, tuple):
                        for collider in other.rect:
                            if nextRect.colliderect(collider):
                                return
                self.rect.x = nextX
                self.updateSmallBlocks()

            if key == pygame.K_d and self.rect.x + self.width < self.g_width:
                nextX = self.rect.x + 30
                nextRect = pygame.Rect(nextX, self.rect.y, self.rect.width, self.rect.height)
                for other in otherBlocks:
                    if other is self:
                        continue
                    if isinstance(other.rect, pygame.Rect):
                        if nextRect.colliderect(other.rect):
                            return
                    elif isinstance(other.rect, tuple):
                        for collider in other.rect:
                            if nextRect.colliderect(collider):
                                return

                self.rect.x = nextX
                self.updateSmallBlocks()

    def updateSmallBlocks(self):
        x = self.rect.x
        y = self.rect.y 

        self.topLeft.setPosition(x, y)
        self.topRight.setPosition(x + self.width//2, y)
        self.botLeft.setPosition(x, y + self.height//2)
        self.botRight.setPosition(x + self.width//2, y + self.height//2)
        
    def groundBlock(self):
        self.isGrounded = True

        for b in self.smallBlocks:
            b.isGrounded = True
