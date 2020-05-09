import pygame


class Board:
    def __init__(self, dimx, dimy):
        self.dimensions = dimx, dimy
        self.board_rects = None

    def create_board(self):

        currentCoords = [0, 0]
        color = (0, 0, 0)
        temp = pygame.display.set_mode((self.dimensions[0] * 10, self.dimensions[1] * 10))

        return temp


class BoardRect(pygame.sprite.Sprite):
    def __init__(self, posx, posy, color):
        super().__init__()
        self.rect = pygame.Rect(posx, posy, 10, 10)
        self.position = posx, posy
        self.color = color

    def amount_touching(self, cells):
        tempx = self.rect.centerx
        tempy = self.rect.centery
        touching = 0
        # TODO: CHECK ALL AROUND THE CELL BOUNDARIES

        # Down
        self.rect.centery += 10
        if any(self.rect.collidepoint(x.rect.x, x.rect.y) for x in cells if x != self):
            touching += 1
        self.rect.centery = tempy

        # Up
        self.rect.centery -= 10
        if any(self.rect.collidepoint(x.rect.x, x.rect.y) for x in cells if x != self):
            touching += 1
        self.rect.centery = tempy

        # Right
        self.rect.centerx += 10
        if any(self.rect.collidepoint(x.rect.x, x.rect.y) for x in cells if x != self):
            touching += 1
        self.rect.centerx = tempx

        # Left
        self.rect.centerx -= 10
        if any(self.rect.collidepoint(x.rect.x, x.rect.y) for x in cells if x != self):
            touching += 1
        self.rect.centerx = tempx

        # Up-Right
        self.rect.centerx += 10
        self.rect.centery -= 10
        if any(self.rect.collidepoint(x.rect.x, x.rect.y) for x in cells if x != self):
            touching += 1
        self.rect.centerx = tempx
        self.rect.centery = tempy

        # Up-Left
        self.rect.centerx -= 10
        self.rect.centery -= 10
        if any(self.rect.collidepoint(x.rect.x, x.rect.y) for x in cells if x != self):
            touching += 1
        self.rect.centerx = tempx
        self.rect.centery = tempy

        # Down-Right
        self.rect.centerx += 10
        self.rect.centery += 10
        if any(self.rect.collidepoint(x.rect.x, x.rect.y) for x in cells if x != self):
            touching += 1
        self.rect.centerx = tempx
        self.rect.centery = tempy

        # Down-Left
        self.rect.centerx -= 10
        self.rect.centery += 10
        if any(self.rect.collidepoint(x.rect.x, x.rect.y) for x in cells if x != self):
            touching += 1
        self.rect.centerx = tempx
        self.rect.centery = tempy
        return touching
