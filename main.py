import pygame

print("pacman time :)")
"https://docs.google.com/document/d/15NM6PDM-4rxv42vfmq85V0iRdOQ-7rnTjBvFhplXGLs/edit"

"ZMENA"

with open("board") as f:
    lines = f.read().splitlines()

board = []
entry = 3

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
    display.blit(image, (0, 0), (SI_CONVERT * (2/3) + 2*TILE[0], 0, TILE[0]*K, TILE[0]*K))


print(len(board))
# print(len(board[2]))

while True:
    background()
    draw_pacman()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()

