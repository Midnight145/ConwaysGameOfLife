import pygame

WHITE = (255, 255, 255)


class Cell(pygame.sprite.Sprite):
    def __init__(self, posx, posy, color, state=1):
        super().__init__()
        self.position = posx, posy
        self.state = state
        self.rect = pygame.Rect(posx, posy, 10, 10)
        self.rect.x = posx
        self.rect.y = posy
        self.width = 10
        self.height = 10
        self.color = color
        self.x = posx
        self.y = posy
        self.pos = (self.x, self.y)

    def isAlive(self, cells):
        pass

    def isDead(self, cells):
        pass

    def kill(self, board, cells):

        new_cells = removeCell(self.pos, board, cells)
        return new_cells

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


def newCell(pos, board, cells):
    for i in board.board_rects:
        if i.rect.collidepoint(pos):
            cell = Cell(i.rect.x, i.rect.y, WHITE)
            if any((i.rect.x, i.rect.y) == k.position for k in cells):
                return -1
            return cell


def removeCell(pos, board, cells):

    for i in board.board_rects:
        if i.rect.collidepoint(pos):
            currentCell = i
    for k in cells:
        if (currentCell.rect.x, currentCell.rect.y) == k.position:
            index = cells.index(k)
            del cells[index]
    return cells


def live(board, cells):
    return check(board, cells)


def check(board, cells):
    cells.sort(key=lambda x: (x.pos[1], x.pos[0]))
    to_remove = []
    to_create = []
    for i in board.board_rects:
        touching = i.amount_touching(cells)
        # Not cell THIS WORKS
        if i.rect.collidelist(cells) == -1:
            if touching == 3:
                # print("here")
                to_create.append((i.rect.x, i.rect.y))

    for i in cells:
        touching = i.amount_touching(cells)
        if i.rect.collidelist(cells) != -1:
            if touching >= 4 or touching <= 1:
                to_remove.append(i)

    for die in to_remove:
        cells = die.kill(board, cells)
    for live in to_create:
        new_cell = newCell(live, board, cells)
        cells.append(new_cell)

    return cells
