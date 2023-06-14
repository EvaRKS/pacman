import pygame
import random

print("pacman time :)")
"https://docs.google.com/document/d/15NM6PDM-4rxv42vfmq85V0iRdOQ-7rnTjBvFhplXGLs/edit"

"ZMENA"

with open("board") as f:
    lines = f.read().splitlines()

board = []
entry = 3
souradnice_pacman_board = (14, 11)
souradnice_ghost_board_seznam = [(11,14), (12,14), (15,14), (16,14)]

for line in lines:
    rozdelenej_line = line.split(", ")
    for i in range(0, len(rozdelenej_line)):
        rozdelenej_line[i] = int(rozdelenej_line[i])
        # rozdelenej_line[cislo] = int(rozdelenej_line[cislo])
    board.append(rozdelenej_line)

SIZE = (28, 31)

TILE = 0
VI_CONVERT = 0
SI_CONVERT = 0

image = pygame.image.load("./assets/sprites.png")
SIRKA_IMG = image.get_width()
VYSKA_IMG = image.get_height()

VYSKA_DISP = int(entry) * 248
SIRKA_DISP = (VYSKA_DISP * (SIRKA_IMG / 3) / (VYSKA_IMG))
display = pygame.display.set_mode((SIRKA_DISP, VYSKA_DISP))

K = VYSKA_DISP/VYSKA_IMG

def background():
    display.fill("black")

    global TILE, VI_CONVERT, SI_CONVERT, image

    VI_CONVERT = VYSKA_DISP
    SI_CONVERT = (VI_CONVERT * (SIRKA_IMG) / (VYSKA_IMG))

    image = pygame.transform.scale(image, (SI_CONVERT, VI_CONVERT))

    # if x == "full":
        # display.blit(image, (0, 0), (0, 0, SI_CONVERT, VI_CONVERT))
    # if x == "empty":
        # display.blit(image, (0, 0), (SI_CONVERT / 3, 0, SI_CONVERT, VI_CONVERT))

    # TILE = ((SI_CONVERT/3) / SIZE[0], VI_CONVERT / SIZE[1])

    TILE = (8*K, 8*K)

    display.blit(image, (0, 0), (SI_CONVERT/3, 0, SI_CONVERT/3, VI_CONVERT))

    for y in range(0, SIZE[1]):
        for x in range(0, SIZE[0]):
            if board[y][x] == 1:
                display.blit(image, (x * TILE[0], y * TILE[1]), (TILE[0], TILE[1], TILE[0], TILE[1]))
            if board[y][x] == 3:
                display.blit(image, (x * TILE[0], y * TILE[1]), (TILE[0], 3*(TILE[1]), TILE[0], TILE[1]))
            else:
               pass




def draw_pacman():
    global souradnice_pacman_board
    print(souradnice_pacman_board)

    # velikost_jednoho_ctverecku = VI_CONVERT/SIZE[0]
    velikost_jednoho_ctverecku = TILE[0]
    stred_jednoho_ctverecku = velikost_jednoho_ctverecku/2

    souradnice_pacman = (souradnice_pacman_board[0]*velikost_jednoho_ctverecku-stred_jednoho_ctverecku, souradnice_pacman_board[1]*velikost_jednoho_ctverecku-stred_jednoho_ctverecku)

    pacman = image
    pacman.set_colorkey((0,0,0))
    display.blit(image, souradnice_pacman, (SI_CONVERT * (2/3) + 2.2*TILE[0], 0, TILE[0]*2, TILE[0]*2))

def draw_ghost(x):
    global souradnice_pacman_board

    ghost = image
    ghost.set_colorkey((0,0,0))

    velikost_jednoho_ctverecku = TILE[0]
    stred_jednoho_ctverecku = velikost_jednoho_ctverecku / 2

    souradnice_ghost_board = x
    souradnice_ghost = (souradnice_ghost_board[0] * velikost_jednoho_ctverecku - stred_jednoho_ctverecku,
                        souradnice_ghost_board[1] * velikost_jednoho_ctverecku - stred_jednoho_ctverecku)

    display.blit(ghost, souradnice_ghost, (SI_CONVERT*(2/3), TILE[0]*(8+2*i), 50, 50))

def random_neco(souradnice):
    x = souradnice[0]
    y = souradnice[1]

    # nahodny cislo 1-4
    nahodny_cislo = random.randint(1, 4)

    # kazdy cislo znamena neco = +1 x, -1 x, +1y, -1y
    if nahodny_cislo == 1:
        return x + 1, y
    elif nahodny_cislo == 2:
        return x - 1, y
    elif nahodny_cislo == 3:
        return x, y + 1
    else:
        return x, y - 1


def end_screen():
    display.fill("black")
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 100)
    text_surface = my_font.render('rip', True, "white")
    display.blit(text_surface, (250, 250))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


print(len(board))
# print(len(board[2]))

while True:
    background()

    predchozi_souradnice_board = souradnice_pacman_board

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            for i in range(0, 4):
                prozatimni_ghost_board_souradnice = random_neco(souradnice_ghost_board_seznam[i])
                if board[souradnice_pacman_board[1]][souradnice_pacman_board[0]] != 2:
                    souradnice_ghost_board_seznam[i] = prozatimni_ghost_board_souradnice

            if event.key == pygame.K_UP:
                souradnice_pacman_board = (souradnice_pacman_board[0], souradnice_pacman_board[1]-1)
            if event.key == pygame.K_DOWN:
                souradnice_pacman_board = (souradnice_pacman_board[0], souradnice_pacman_board[1]+1)
            if event.key == pygame.K_LEFT:
                souradnice_pacman_board = (souradnice_pacman_board[0]-1, souradnice_pacman_board[1])
            if event.key == pygame.K_RIGHT:
                souradnice_pacman_board = (souradnice_pacman_board[0]+1, souradnice_pacman_board[1])

    if souradnice_pacman_board[0] < 0:
        souradnice_pacman_board = (27, souradnice_pacman_board[1])
    if souradnice_pacman_board[0] > 27:
        souradnice_pacman_board = (0, souradnice_pacman_board[1])

    if board[souradnice_pacman_board[1]][souradnice_pacman_board[0]] == 2:
        souradnice_pacman_board = predchozi_souradnice_board
    elif board[souradnice_pacman_board[1]][souradnice_pacman_board[0]] == 1:
        board[souradnice_pacman_board[1]][souradnice_pacman_board[0]] = 0
        draw_pacman()
    elif board[souradnice_pacman_board[1]][souradnice_pacman_board[0]] == 3:
        board[souradnice_pacman_board[1]][souradnice_pacman_board[0]] = 0
        draw_pacman()
    else:
        draw_pacman()


    draw_ghost()


    pygame.display.flip()

