import pygame
import sys
import math
import time

pygame.init()
screen = pygame.display.set_mode((1366, 768),pygame.FULLSCREEN)
pygame.display.set_caption("Physics Simiulation")
Clock = pygame.time.Clock()
pause=False
sp=1
slider=0
def check_ev():
    global pause
    global sp
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                import Main_Final
                Main_Final.main()
                sys.exit()
            if event.key == pygame.K_SPACE:
                pause=not pause
            if event.key == pygame.K_a and sp>.5:
                sp-=.1
            if event.key == pygame.K_d:
                if sp<2:
                    sp+=.1
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x,pos_y=pygame.mouse.get_pos()
            if pos_x >=250 and pos_x<=275 and pos_y>=400 and pos_y<=425 and sp<2:
                sp+=.1
            elif pos_x >=100 and pos_x<=125 and pos_y>=400 and pos_y<=425 and sp>.5:
                sp-=.1


def s_cir(screen, h, k, r):
    '''sub=1
    while sub<=r:
    	i=1
    	while i <= 360:
    		x = h + sub * math.cos((i / 180) * 3.1415926)
    		y = k+ sub * math.sin(i / 180 * 3.1415926)
    		pygame.draw.line(screen, (255, 0, 0), [x, y], [x, y])
    		i = i + 0.5
    	print (sub,r)
    	sub=sub+1'''
    pygame.draw.circle(screen, (0, 0, 255), [int(h), int(k)], r, 0)


def cir(screen, h, k, r):
    # marker line horizontal
    pygame.draw.line(screen, (0, 50, 0,), [200 + 1 * 20, 100], [200 + 1 * 20, 300], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 + 2 * 20, 101], [200 + 2 * 20, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 + 3 * 20, 101], [200 + 3 * 20, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 + 4 * 20, 101], [200 + 4 * 20, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 + 5 * 20 - 1, 101], [200 + 5 * 20 - 1, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 + 0 * 20, 101], [200 + 0 * 20, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 - 1 * 20, 101], [200 - 1 * 20, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 - 2 * 20, 101], [200 - 2 * 20, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 - 3 * 20, 101], [200 - 3 * 20, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 - 4 * 20, 101], [200 - 4 * 20, 301], 1)
    pygame.draw.line(screen, (0, 50, 0,), [200 - 5 * 20 + 1, 101], [200 - 5 * 20 + 1, 301], 1)

    # marker line vertical;
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 + 1 * 20], [301, 200 + 1 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 + 2 * 20], [301, 200 + 2 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 + 3 * 20], [301, 200 + 3 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 + 4 * 20], [301, 200 + 4 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 + 5 * 20], [301, 200 + 5 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0), [101, 200 + 0 * 20], [301, 200 + 0 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 - 1 * 20], [301, 200 - 1 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 - 2 * 20], [301, 200 - 2 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 - 3 * 20], [301, 200 - 3 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 - 4 * 20], [301, 200 - 4 * 20], 1)
    pygame.draw.line(screen, (0, 50, 0,), [101, 200 - 5 * 20], [301, 200 - 5 * 20], 1)

    i = 1
    while i <= 360:
        # screen.fill((0,0,0))
        x = h + r * math.cos((i / 180) * 3.1415926)
        y = k + r * math.sin(i / 180 * 3.1415926)
        pygame.draw.line(screen, (255, 0, 0), [x, y], [x, y])
        i = i + 0.5
    # axes line
    pygame.draw.line(screen, (255, 0, 0), [h + 0, k + r], [h + 0, k - r], 1)
    pygame.draw.line(screen, (255, 0, 0), [h + r, k + 0], [h - r, k - 0], 1)

    # check_ev()


def xgraph(screen, x, t, xlines):
    xfont = pygame.font.SysFont(None, 20)
    xv=str(x/20)
    xv=xv[:4]
    xt=str(t/100)
    xt=xt[:4]
    tpv = str(3.60 / sp)
    tpv = tpv[:4]
    xval = xfont.render("Value of x: "+xv, True, (255, 255, 255))
    xtime=xfont.render("Value of t: "+xt,True,(255,255,255))
    tpval=xfont.render("Vallue of Time period: " + tpv,True,(255,255,255))
    screen.blit(xval,(400,25))
    screen.blit(xtime,(550,25))
    screen.blit(tpval,(700,25))
    pygame.draw.line(screen, (255, 0, 0), [400, 50], [400, 350])
    pygame.draw.line(screen, (255, 0, 0), [350, 200], [1200, 200])
    xlines.append((400 + t, 200 - x))
    pygame.draw.lines(screen, (255, 0, 0), False, xlines, 1)
    s_cir(screen, 400 + t, 200 - x, 5)


def ygraph(screen, y, t, ylines):
    yfont=pygame.font.SysFont(None,20)
    yv=str(-y/20)
    yv=yv[:4]
    yt=str(t/100)
    yt=yt[:4]
    yval=yfont.render("Value of y: " + yv,True,(255,255,255))
    ytime=yfont.render("Value of t: "+ yt,True,(255,255,255))
    screen.blit(yval,(400,375))
    screen.blit(ytime,(550,375))
    pygame.draw.line(screen, (255, 0, 0), [400, 400], [400, 700])
    pygame.draw.line(screen, (255, 0, 0), [350, 550], [1200, 550])
    ylines.append((400 + t, 550 + y))
    pygame.draw.lines(screen, (255, 0, 0), False, ylines, 1)
    s_cir(screen, 400 + t, 550 + y, 5)

def ctrl():
    global sp
    pygame.draw.lines(screen,(255,0,0),True,[(100,400),(125,400),(125,425),(100,425)])
    pygame.draw.lines(screen, (0, 0, 255), True, [(110,402 ), (114, 402), (114, 423), (110, 423)])
    pygame.draw.lines(screen, (0, 0, 255), True, [(102, 410), (123, 410), (123, 414), (102, 414)])

    pygame.draw.lines(screen, (255, 0, 0), True, [(250, 400), (275, 400), (275, 425), (250, 425)])
    pygame.draw.lines(screen, (0, 0, 255), True, [(253, 410), (273, 410), (273, 414), (253, 414)])

    ctrl_font=pygame.font.SysFont(None,40)
    tpv = str(3.60 / sp)
    tpv = tpv[:4]
    tpval=ctrl_font.render(tpv,True,(0,0,255))
    screen.blit(tpval,(170,405))

def run_shm():
    while True:
        i = 0
        t=0
        xlines = [(400, 200)]
        ylines = [(400, 550)]
        # time1=pygame.time.get_ticks()
        beg_time = time.time()
        while (time.time() - beg_time) <= 7.20:
            rot_time = time.time()
            x = 100 * math.cos(((i - 90) / 180) * 3.1415926)
            y = 100 * math.sin((i -90) / 180 * 3.1415926)
            screen.fill((0, 0, 0))
            cir(screen, 200, 200, 100)
            s_cir(screen, 200 + x, 200 + y, 5)
            xgraph(screen, x, t, xlines)
            ygraph(screen, y, t, ylines)
            ctrl()
            check_ev()
            pygame.display.update()
            while (time.time() - rot_time) <= .01:
                pass
            if not pause:
                i = i + sp
                t=t+1

            else:
                beg_time = beg_time + time.time() - rot_time
