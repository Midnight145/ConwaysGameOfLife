import pygame

from modules import Board, Cell

pygame.init()
board = Board.Board(100, 100)
screen = board.create_board()

gameEnd = False
board_rects = []


def init():

    pygame.display.set_caption('Conway\'s Game of Life')

    screen.fill((0, 0, 0))
    pygame.display.update()
    current_coords = [0, 0]
    color = (80, 80, 80)

    while current_coords[1] <= board.dimensions[1] * 10:
        if current_coords[1] % 20 == 0:
            current_coords[0] += 10
        while current_coords[0] <= board.dimensions[0] * 10:
            board_rects.append(Board.BoardRect(current_coords[0], current_coords[1], color))
            current_coords[0] += 20
        current_coords[0] = 0
        current_coords[1] += 10

    current_coords = [-10, 0]
    color = (0, 0, 0)
    while current_coords[1] <= board.dimensions[1] * 10:
        if current_coords[1] % 20 == 0:
            current_coords[0] += 10
        while current_coords[0] <= board.dimensions[0] * 10:
            board_rects.append(Board.BoardRect(current_coords[0], current_coords[1], color))
            current_coords[0] += 20
        current_coords[0] = -10
        current_coords[1] += 10


board.board_rects = board_rects

init()
cells = []
flag = False
while not gameEnd:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag = not flag
        if event.type == pygame.MOUSEBUTTONDOWN:
            currentCell = Cell.newCell(pygame.mouse.get_pos(), board, cells)
            if currentCell == -1:
                cells = Cell.removeCell(pygame.mouse.get_pos(), board, cells)

            else:
                cells.append(currentCell)
    if flag:
        Cell.live(board, cells)
    for i in board_rects:
        pygame.draw.rect(screen, i.color, i.rect)
    for i in cells:
        pygame.draw.rect(screen, (255, 255, 255), i.rect)
    pygame.display.update()
