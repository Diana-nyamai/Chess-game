import pygame as p
from chessimg import chessengine
p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
initialise a global dictionary of images:called once in main
'''


def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bp', 'wR', 'wK', 'wB', 'wQ', 'wN', 'wp']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("chessimg/img/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    '''
    THE MAIN DRIVER
    '''


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = chessengine.GameState()
    loadImages()  # only do this once
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
where the graphics will be placed
'''


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


'''
draw squares on the board
'''


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
draw pieces on the board 
'''


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
