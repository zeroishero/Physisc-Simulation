import pygame
import math
import sys
def border(screen):

    #horizontal line above
    pygame.draw.line(screen, (0,0,255), [0, 0], [1366, 0], 1)
    pygame.draw.line(screen, (0,0,255), [0, 1], [1366, 1], 1)
    pygame.draw.line(screen, (0,0,255), [0, 2], [1366, 2], 1)
    pygame.draw.line(screen, (0,0,255), [0, 3], [1366, 3], 1)

    # horizontal line below
    pygame.draw.line(screen, (0,0,255), [0, 768], [1366, 768], 1)
    pygame.draw.line(screen, (0,0,255), [0, 767], [1366, 767], 1)
    pygame.draw.line(screen, (0,0,255), [0, 766], [1366, 766], 1)
    pygame.draw.line(screen, (0,0,255), [0, 765], [1366, 765], 1)

    # vertical line left
    pygame.draw.line(screen, (0,0,255), [0, 0], [0, 768], 1)
    pygame.draw.line(screen, (0,0,255), [1, 0], [1, 768], 1)
    pygame.draw.line(screen,(0,0,255), [2, 0], [2, 768], 1)
    pygame.draw.line(screen, (0,0,255), [3, 0], [3, 768], 1)

    # vertical line right
    pygame.draw.line(screen, (0,0,255), [1366, 0], [1366, 768], 1)
    pygame.draw.line(screen, (0,0,255), [1365, 0], [1365, 768], 1)
    pygame.draw.line(screen, (0,0,255), [1364, 0], [1364, 768], 1)
    pygame.draw.line(screen, (0,0,255), [1363, 0], [1363, 768], 1)

    '''for i in range(4,51):
        pygame.draw.line(screen,(255,0,0),[i,4],[i,764],1)'''
    ang=0.0

    #sine above
    for i in range(50,1317):
        pygame.draw.line(screen,(255,0,0),[i,4],[i,50-20*math.sin(ang)])
        ang=ang + 2*3.141592653/(1317-50)
    #sine down
    for i in range(50, 1317):
        pygame.draw.line(screen, (255, 0, 0), [i, 764], [i, 768-50 - 20 * math.sin(ang)])
        ang = ang + 2 * 3.141592653 / (1317 - 50)
    for i in range(50, 768-50):
        pygame.draw.line(screen, (255, 0, 0), [i, 764], [i, 768-50 - 20 * math.sin(ang)])
        ang = ang + 2 * 3.141592653 / (1317 - 50)




    pygame.display.flip()
pygame.init()
screen=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
pygame.display.set_caption("Physics Simulation")
def menu():
    border(screen)
    done=0
    #list()
    #action()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key:
                    sys.exit()


menu()
