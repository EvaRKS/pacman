print("pacman time :)")
"https://docs.google.com/document/d/15NM6PDM-4rxv42vfmq85V0iRdOQ-7rnTjBvFhplXGLs/edit"

with open("board") as f:
    lines = f.read().splitlines()

board = []

for line in lines:
    rozdelenej_line = line.split(", ")

    board.append(rozdelenej_line)

print(board)

import pygame

SIZE = (28, 31)
board = []

TILE = 0
VI_CONVERT = 0
SI_CONVERT = 0


def background(x):
    global TILE, VI_CONVERT, SI_CONVERT

    image = pygame.image.load("assets\Arcade - Pac-Man - General Sprites.png")
    SIRKA_IMG = image.get_width()
    VYSKA_IMG = image.get_height()

    VYSKA_DISP = 500
    SIRKA_DISP = (VYSKA_DISP * (SIRKA_IMG / 3) / (VYSKA_IMG))
    display = pygame.display.set_mode((SIRKA_DISP, VYSKA_DISP))

    VI_CONVERT = VYSKA_DISP
    SI_CONVERT = (VI_CONVERT * (SIRKA_IMG) / (VYSKA_IMG))

    image = pygame.transform.scale(image, (SI_CONVERT, VI_CONVERT))

    # if x == "full":
        # display.blit(image, (0, 0), (0, 0, SI_CONVERT, VI_CONVERT))
    # if x == "empty":
        # display.blit(image, (0, 0), (SI_CONVERT / 3, 0, SI_CONVERT, VI_CONVERT))

    TILE = ((SI_CONVERT/3) / SIZE[0], VI_CONVERT / SIZE[1])

    for j in range(0, SIZE[1]):
        for i in range(0, SIZE[0]):
            display.blit(image, (j*TILE[0], i*TILE[1]), (j* TILE[0], i*TILE[1], TILE[0], (i+SIZE[1])*TILE[1]))


def create_board(x, y, z):
    global board
    board = []

    i = 0
    while i < (x/3):
        rada = []

        j = z[1]
        while j < y:
            rada.append(0)
            j += z[1]

        board.append(rada)
        i += z[0]

    print(board)

background("empty")
create_board(SI_CONVERT, VI_CONVERT, TILE)
print(len(board))
print(len(board[2]))

while True:
    background("full")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()

