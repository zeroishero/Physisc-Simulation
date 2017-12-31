import pygame
import sys
import math
pygame.init()
screen=pygame.display.set_mode((1366,768))
pygame.display.set_caption("Physics Simiulation")

def check_ev():
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
def cir(screen,h,k,r):
    font=pygame.font.SysFont(None,10)
    l1=font.render("1",True,(255,255,255))
    l2 = font.render("2", True, (255, 255, 255))
    l3 = font.render("3", True, (255, 255, 255))
    l4 = font.render("4", True, (255, 255, 255))
    l5 = font.render("5", True, (255, 255, 255))
    i=0
    while i <= 360:
        # screen.fill((0,0,0))
        x = h + r * math.cos((i / 180) * 3.1415926)
        y = k+ r * math.sin(i / 180 * 3.1415926)
        pygame.draw.line(screen, (255, 0, 0), [x, y], [x, y])
        i = i + 0.5
    #axes line
    pygame.draw.line(screen,(255,0,0),[h+0,k+r],[h+0,k-r],1)
    pygame.draw.line(screen, (255, 0, 0), [h + r, k + 0], [h -r, k - 0], 1)

    #marker line horizontal
    pygame.draw.line(screen,(0,255,0,),[200+1*20,200+2],[200+1*20,200-2],1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 2 * 20, 200 + 2], [200 + 2 * 20, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 3 * 20, 200 + 2], [200 + 3 * 20, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 4 * 20, 200 + 2], [200 + 4 * 20, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 5 * 20-1, 200 + 2], [200 + 5 * 20-1, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 0 * 20, 200 + 2], [200 + 0 * 20, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 - 1 * 20, 200 + 2], [200 - 1 * 20, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 - 2 * 20, 200 + 2], [200 - 2 * 20, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 - 3 * 20, 200 + 2], [200 - 3 * 20, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 - 4 * 20, 200 + 2], [200 - 4 * 20, 200 - 2], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 - 5 * 20 + 1, 200 + 2], [200 - 5 * 20 + 1, 200 - 2], 1)

    # marker line vertical;
    pygame.draw.line(screen, (0, 255, 0,), [200 + 2, 200 + 1*20], [200 -2, 200 +1*20], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 2, 200 + 2*20], [200 -2, 200 +2*20], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 2, 200 + 3*20], [200 -2, 200 +3*20], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 2, 200 + 4*20], [200 -2, 200 +4*20], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 2, 200 + 5*20], [200 -2, 200 +5*20], 1)
    pygame.draw.line(screen,(0,255,0),[200+2,200+0*20],[200-2,200+0*20],1)
    pygame.draw.line(screen, (0, 255, 0,), [200 + 2, 200 -1*20], [200 -2, 200 - 1*20], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 +2 , 200 -2*20], [200 -2 , 200 - 2*20], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 +2 , 200 -3*20], [200 -2 , 200 - 3*20], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 +2 , 200 -4*20], [200 -2, 200 - 4*20], 1)
    pygame.draw.line(screen, (0, 255, 0,), [200 +2 , 200 -5*20], [200 -2 , 200 - 5*20], 1)

    #check_ev()


while True:
    i=0
    for i in range(0,360):
        x=100 * math.cos((i / 180) * 3.1415926)
        y=100 * math.sin(i / 180 * 3.1415926)
        screen.fill((0,0,0))
        cir(screen,200,200,100)
        cir(screen,200 + x,200 + y,5)
        check_ev()
        #xgraph(screen,x)

        pygame.display.flip()



