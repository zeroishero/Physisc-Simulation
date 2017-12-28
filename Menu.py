import pygame
import math
import sys
global counter
counter=0

def option(screen):
    font=pygame.font.SysFont("comicsansms",20)
    op1=font.render("1. Projectile",True,(0,0,255))
    op2=font.render("2. Simple Pendulum",True,(0,0,255))
    op3=font.render("3. Projection of a Particle in Circular motion on axes",True,(0,0,255))
    screen.blit(op1,(200,200))
    screen.blit(op2,(200,230))
    screen.blit(op3,(200,260))
def border(screen):

    #horizontal line above
    screen.fill((0,0,0))
    option(screen)
    pygame.draw.line(screen, (0,0,255), [0, 0], [1366, 0], 1)
    pygame.draw.line(screen, (0,0,255), [0, 1], [1366, 1], 1)
    pygame.draw.line(screen, (0,0,255), [0, 2], [1366, 2], 1)
    pygame.draw.line(screen, (0,0,255), [0, 3], [1366, 3], 1)
    pygame.draw.line(screen, (0, 0, 255), [0, 4], [1366, 4], 1)
    pygame.draw.line(screen, (0, 0, 255), [0, 5], [1366, 5], 1)
    pygame.draw.line(screen, (0, 0, 255), [0, 6], [1366, 6], 1)
    pygame.draw.line(screen, (0, 0, 255), [0, 7], [1366, 7], 1)

    # horizontal line below
    pygame.draw.line(screen, (0,0,255), [0, 768], [1366, 768], 1)
    pygame.draw.line(screen, (0,0,255), [0, 767], [1366, 767], 1)
    pygame.draw.line(screen, (0,0,255), [0, 766], [1366, 766], 1)
    pygame.draw.line(screen, (0,0,255), [0, 765], [1366, 765], 1)
    pygame.draw.line(screen, (0, 0, 255), [0, 764], [1366, 764], 1)
    pygame.draw.line(screen, (0, 0, 255), [0, 763], [1366, 763], 1)
    pygame.draw.line(screen, (0, 0, 255), [0, 762], [1366, 762], 1)
    pygame.draw.line(screen, (0, 0, 255), [0, 761], [1366, 761], 1)
    # vertical line left
    pygame.draw.line(screen, (0,0,255), [0, 0], [0, 768], 1)
    pygame.draw.line(screen, (0,0,255), [1, 0], [1, 768], 1)
    pygame.draw.line(screen,(0,0,255), [2, 0], [2, 768], 1)
    pygame.draw.line(screen, (0,0,255), [3, 0], [3, 768], 1)
    pygame.draw.line(screen, (0, 0, 255), [4, 0], [4, 768], 1)
    pygame.draw.line(screen, (0, 0, 255), [5, 0], [5, 768], 1)
    pygame.draw.line(screen, (0, 0, 255), [6, 0], [6, 768], 1)
    pygame.draw.line(screen, (0, 0, 255), [7, 0], [7, 768], 1)

    # vertical line right
    pygame.draw.line(screen, (0,0,255), [1366, 0], [1366, 768], 1)
    pygame.draw.line(screen, (0,0,255), [1365, 0], [1365, 768], 1)
    pygame.draw.line(screen, (0,0,255), [1364, 0], [1364, 768], 1)
    pygame.draw.line(screen, (0,0,255), [1363, 0], [1363, 768], 1)
    pygame.draw.line(screen, (0, 0, 255), [1362, 0], [1362, 768], 1)
    pygame.draw.line(screen, (0, 0, 255), [1361, 0], [1361, 768], 1)
    pygame.draw.line(screen, (0, 0, 255), [1360, 0], [1360, 768], 1)
    pygame.draw.line(screen, (0, 0, 255), [1359, 0], [1359, 768], 1)


    ang=0.0+counter

    #sine above
    for i in range(8,1358):
        pygame.draw.line(screen,(255,0,0),[i,8],[i,50-20*math.sin(ang)])
        ang=ang + 2*3.141592653/(1317-50)
    #sine down
    for i in range(8, 1358):
        pygame.draw.line(screen, (255, 0, 0), [i, 760], [i, 768-50 - 20 * math.sin(ang)])
        ang = ang + 2 * 3.141592653 / (1317 - 50)
    #sine left
    for i in range(8, 760):
        pygame.draw.line(screen, (255, 0, 0), [8,i], [(50+ 20 * math.sin(ang)),i])
        ang = ang + 2 * 3.141592653 / (1317 - 50)
    #sine right
    for i in range(8, 760):
        pygame.draw.line(screen, (255, 0, 0), [1358,i], [(1366-50+ 20 * math.sin(ang)),i])
        ang = ang + 2 * 3.141592653 / (1317 - 50)

    pygame.display.flip()



pygame.init()
screen=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
pygame.display.set_caption("Physics Simulation")

def menu():
    global counter
    counter=0

    done=0
    #list()
    #action()
    while not done:
        border(screen)
        counter+=0.01
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key:
                    sys.exit()
        #pygame.time.delay(100)


menu()
