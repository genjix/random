import sys, pygame, life, random, osc
#pygame.init()
pygame.display.init()

osc = osc.OSC()
osc.connect('localhost', 9001)

# 31x23 cells of 32x32
size = scrwidth, scrheight = 992, 736
cellsize = 32
speed = [2, 2]
black = 0, 0, 0
numcells = scrwidth//cellsize + 1
lifegrid = [[round(0) for cell in range(numcells)] for row in range(numcells)]

screen = pygame.display.set_mode(size)

#background = pygame.image.load("grass.jpg")
#bg_rect = background.get_rect()
# the flowers are 4 32x32 tiles in top left
flower_sheet = pygame.image.load('flowers.png')

def blit_flower(num, pos, screen, flower_sheet):
    x, y, w, h = 0, 0, cellsize, cellsize
    if num == 1:
        x = 0
        y = 0
    elif num == 2:
        x = cellsize
        y = 0
    elif num == 3:
        x = 0
        y = cellsize
    elif num == 4:
        x = cellsize
        y = cellsize
    elif num == 5:
        x = cellsize*2
        y = 0
    screen.blit(flower_sheet, pos, (x, y, w, h))

flower_store = [[0 for cell in range(numcells)] for row in range(numcells)]
drawing = -1
pause = False

while 1:
    if drawing == -1 and not pause:
        lifegrid = life.lifestep(lifegrid)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            elif event.key == pygame.K_a:
                lifegrid = [[round(random.random()) for cell in range(numcells)] for row in range(numcells)] 
            elif event.key == pygame.K_c:
                lifegrid = [[round(0) for cell in range(numcells)] for row in range(numcells)]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos[0]//cellsize, event.pos[1]//cellsize
            drawing = 1 - lifegrid[y][x] 
            lifegrid[y][x] = drawing
        elif event.type == pygame.MOUSEMOTION:
            if drawing != -1:
                x, y = event.pos[0]//cellsize, event.pos[1]//cellsize
                lifegrid[y][x] = drawing
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = -1

    screen.fill(black)
    #screen.blit(background, bg_rect)
    #screen.blit(background, (bg_rect[2], 0, scrwidth-bg_rect[2], bg_rect[3]))
    #screen.blit(background, (0, bg_rect[3], 0, scrheight-bg_rect[3]))
    #screen.blit(background, (bg_rect[2], bg_rect[3], scrwidth-bg_rect[2], scrheight-bg_rect[3]))

    tbirth, tlife, tdeath, tempty = 0, 0, 0, 0
    for y, row in enumerate(lifegrid):
        for x, cell in enumerate(row):
            if cell == 1:
                looksee = flower_store[y][x]
                if looksee == 0:
                    looksee = random.choice((1,2,3,4))
                    flower_store[y][x] = looksee
                    tbirth += 1
                tlife += 1
                blit_flower(looksee, (x*cellsize, y*cellsize), screen, flower_sheet)
            elif cell == 0:
                blit_flower(5, (x*cellsize, y*cellsize), screen, flower_sheet)
                if flower_store[y][x] != 0:
                    flower_store[y][x] = 0
                    tdeath += 1
                tempty += 1
    osc.send('/birth', tbirth)
    osc.send('/life', tlife)
    osc.send('/death', tdeath)
    osc.send('/empty', tempty)

    pygame.display.flip()
    pygame.time.wait(100)
