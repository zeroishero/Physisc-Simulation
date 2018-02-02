import pygame
import math
import sys
import time

pygame.init()
screen=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
pygame.display.set_caption("Wave")
clock=pygame.time.Clock()
pause=False
class wave:
    def __init__(self,freq,amp,wave_len,dir):
        self.freq=freq
        self.amp=amp
        self.wave_len=wave_len
        self.dir=dir
        if dir:
            self.k=2*math.pi/wave_len
        else:
            self.k=-2*math.pi/wave_len
        self.x=[0]*1200

def ctrl(a,b):
    ctrl_font = pygame.font.SysFont(None, 30)
    freq_lbl=ctrl_font.render("Frequency",True,(0,255,255))
    amp_lbl=ctrl_font.render("Amplitude",True,(0,255,255))
    wave_len_lbl=ctrl_font.render("Wave length",True,(0,255,255))
    dir_lbl=ctrl_font.render("Direction",True,(0,255,255))
    screen.blit(freq_lbl,(200,25))
    screen.blit(amp_lbl, (500,25))
    screen.blit(wave_len_lbl, (750,25))
    screen.blit(dir_lbl, (1000,25))
    #a frequency
    #plus
    x=100
    y=25
    pygame.draw.lines(screen,(255,0,0),True,[(x+100,y+25),(x+125,y+25),(x+125,y+50),(x+100,y+50)])
    pygame.draw.lines(screen, (0, 0, 255), True, [(x+110,y+27 ), (x+114, y+27), (x+114, y+48), (x+110, y+48)])
    pygame.draw.lines(screen, (0, 0, 255), True, [(x+102, y+35), (x+123, y+35), (x+123, y+39), (x+102, y+39)])
    #minus
    pygame.draw.lines(screen, (255, 0, 0), True, [(x+250, y+25), (x+275, y+25), (x+275,y+ 50), (x+250, y+50)])
    pygame.draw.lines(screen, (0, 0, 255), True, [(x+253,y+ 35), (x+273, y+35), (x+273, y+39), (x+253, y+39)])
    a_freqs=str(a.freq)
    a_freqs=a_freqs[:4]
    a_freq=ctrl_font.render(a_freqs+" Hz",True,(0,0,255))

    screen.blit(a_freq,(225+x/2,y+25))
    x = 400
    y = 25
    pygame.draw.lines(screen, (255, 0, 0), True,[(x + 100, y + 25), (x + 125, y + 25), (x + 125, y + 50), (x + 100, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,[(x + 110, y + 27), (x + 114, y + 27), (x + 114, y + 48), (x + 110, y + 48)])
    pygame.draw.lines(screen, (0, 0, 255), True,[(x + 102, y + 35), (x + 123, y + 35), (x + 123, y + 39), (x + 102, y + 39)])
    # minus
    pygame.draw.lines(screen, (255, 0, 0), True,[(x + 250, y + 25), (x + 275, y + 25), (x + 275, y + 50), (x + 250, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,[(x + 253, y + 35), (x + 273, y + 35), (x + 273, y + 39), (x + 253, y + 39)])
    a_amps=str(a.amp/20)
    a_amps=a_amps[:4]
    a_amp = ctrl_font.render(a_amps + " cm", True, (0, 0, 255))
    screen.blit(a_amp, (350 + x / 2, y + 25))

    x = 650
    y = 25
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 100, y + 25), (x + 125, y + 25), (x + 125, y + 50), (x + 100, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 110, y + 27), (x + 114, y + 27), (x + 114, y + 48), (x + 110, y + 48)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 102, y + 35), (x + 123, y + 35), (x + 123, y + 39), (x + 102, y + 39)])
    # minus
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 250, y + 25), (x + 275, y + 25), (x + 275, y + 50), (x + 250, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 253, y + 35), (x + 273, y + 35), (x + 273, y + 39), (x + 253, y + 39)])
    a_wave_lens=str(a.wave_len/40)
    a_wave_lens=a_wave_lens[:4]
    a_wave_len = ctrl_font.render(a_wave_lens + " cm", True, (0, 0, 255))
    screen.blit(a_wave_len, (500 + x / 2, y + 25))

    x=900
    y=25
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 100, y + 25), (x + 125, y + 25), (x + 125, y + 50), (x + 100, y + 50)])
    pygame.draw.circle(screen,(0,0,255),(x+112,y+37),10,0)
    if a.dir:
        a_state="On"
    else:
        a_state="Off"
    a_dir=ctrl_font.render(a_state,True,(0,0,255))
    screen.blit(a_dir,(x+130,y+25))

    # b frequency
    # plus
    x = 100
    y = 60
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 100, y + 25), (x + 125, y + 25), (x + 125, y + 50), (x + 100, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 110, y + 27), (x + 114, y + 27), (x + 114, y + 48), (x + 110, y + 48)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 102, y + 35), (x + 123, y + 35), (x + 123, y + 39), (x + 102, y + 39)])
    # minus
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 250, y + 25), (x + 275, y + 25), (x + 275, y + 50), (x + 250, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 253, y + 35), (x + 273, y + 35), (x + 273, y + 39), (x + 253, y + 39)])
    b_freq = ctrl_font.render(str(b.freq) + " Hz", True, (0, 0, 255))

    screen.blit(b_freq, (225 + x / 2, y + 25))
    x = 400
    y = 60
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 100, y + 25), (x + 125, y + 25), (x + 125, y + 50), (x + 100, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 110, y + 27), (x + 114, y + 27), (x + 114, y + 48), (x + 110, y + 48)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 102, y + 35), (x + 123, y + 35), (x + 123, y + 39), (x + 102, y + 39)])
    # minus
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 250, y + 25), (x + 275, y + 25), (x + 275, y + 50), (x + 250, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 253, y + 35), (x + 273, y + 35), (x + 273, y + 39), (x + 253, y + 39)])
    b_amp = ctrl_font.render(str(b.amp / 20) + " cm", True, (0, 0, 255))
    screen.blit(b_amp, (350 + x / 2, y + 25))

    x = 650
    y = 60
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 100, y + 25), (x + 125, y + 25), (x + 125, y + 50), (x + 100, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 110, y + 27), (x + 114, y + 27), (x + 114, y + 48), (x + 110, y + 48)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 102, y + 35), (x + 123, y + 35), (x + 123, y + 39), (x + 102, y + 39)])
    # minus
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 250, y + 25), (x + 275, y + 25), (x + 275, y + 50), (x + 250, y + 50)])
    pygame.draw.lines(screen, (0, 0, 255), True,
                      [(x + 253, y + 35), (x + 273, y + 35), (x + 273, y + 39), (x + 253, y + 39)])
    b_wave_len = ctrl_font.render(str(b.wave_len / 40) + " cm", True, (0, 0, 255))
    screen.blit(b_wave_len, (500 + x / 2, y + 25))

    x = 900
    y = 60
    pygame.draw.lines(screen, (255, 0, 0), True,
                      [(x + 100, y + 25), (x + 125, y + 25), (x + 125, y + 50), (x + 100, y + 50)])
    pygame.draw.circle(screen, (0, 0, 255), (x + 112, y + 37), 10, 0)
    if b.dir:
        b_state = "On"
    else:
        b_state = "Off"
    b_dir = ctrl_font.render(b_state, True, (0, 0, 255))
    screen.blit(b_dir, (x + 130, y + 25))





def chk(a,b):
    global pause
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                import Menu
                Menu.menu()
                sys.exit()
            if event.key == pygame.K_SPACE:
                pause=not pause
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos_x,pos_y=pygame.mouse.get_pos()
            #for a
            if pos_x>=200 and pos_x<=225 and pos_y>=50 and pos_y<=75 and a.freq<2:
                a.freq+=.1
            if pos_x >= 350 and pos_x <= 375 and pos_y >= 50 and pos_y <= 75 and a.freq > .5:
                a.freq -= .1

            if pos_x>=500 and pos_x<=525 and pos_y>=50 and pos_y<=75 and a.amp<200:
                a.amp+=10
            if pos_x >= 650 and pos_x <= 675 and pos_y >= 50 and pos_y <= 75 and a.amp >50:
                a.amp -= 10

            if pos_x>=750 and pos_x<=775 and pos_y>=50 and pos_y<=75 and a.wave_len<1200:
                a.wave_len+=20
                if a.dir:
                    a.k = 2 * math.pi / a.wave_len
                    print(a.k)
                else:
                    a.k = -2 * math.pi / a.wave_len
            if pos_x >= 900 and pos_x <= 925 and pos_y >= 50 and pos_y <= 75 and a.wave_len >20:
                a.wave_len -= 20
                if a.dir:
                    a.k = 2 * math.pi / a.wave_len
                    print(a.k)
                else:
                    a.k = -2 * math.pi / a.wave_len
            if pos_x>=1000 and pos_x<=1025 and pos_y>=50 and pos_y<=75 :
                a.dir=not a.dir
                if a.dir:
                    a.k = 2 * math.pi / a.wave_len
                    print(a.k)
                else:
                    a.k = -2 * math.pi / a.wave_len
            #for b
            if pos_x>=200 and pos_x<=225 and pos_y>=85 and pos_y<=110 and a.freq<2:
                b.freq+=.1
            if pos_x >= 350 and pos_x <= 375 and pos_y >= 85 and pos_y <= 110 and b.freq > .5:
                b.freq -= .1

            if pos_x>=500 and pos_x<=525 and pos_y>=85 and pos_y<=110 and b.amp<200:
                b.amp+=10
            if pos_x >= 650 and pos_x <= 675 and pos_y >= 85 and pos_y <= 110 and b.amp >50:
                b.amp -= 10

            if pos_x>=750 and pos_x<=775 and pos_y>=85 and pos_y<=110 and b.wave_len<1200:
                b.wave_len+=20
                if b.dir:
                    b.k = 2 * math.pi / b.wave_len
                else:
                    b.k = -2 * math.pi / b.wave_len
            if pos_x >= 900 and pos_x <= 925 and pos_y >= 85 and pos_y <= 110 and b.wave_len >20:
                b.wave_len -= 20
                if b.dir:
                    b.k = 2 * math.pi / b.wave_len
                else:
                    b.k = -2 * math.pi / b.wave_len
            if pos_x>=1000 and pos_x<=1025 and pos_y>=85 and pos_y<=110:
                b.dir=not b.dir
                if b.dir:
                    b.k = 2 * math.pi / b.wave_len
                else:
                    b.k = -2 * math.pi / b.wave_len



def border():

    #horizontal line above
    screen.fill((0,0,0))
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

def graph():
    pygame.draw.line(screen, (100, 100, 100), [200, 150], [200, 750])
    pygame.draw.line(screen, (50, 50, 50), [150, 450], [1200, 450])

def run_wave():
    a=wave(1,100,400,True)
    b=wave(1,100,400,False)
    beg_time = time.time()
    while True:
        border()
        graph()
        i=200
        while i<=1200:
            loop_time=time.time()
            t=time.time()-beg_time
            a.x[i-200]=i-200
            b.x[i-200]=i-200
            a_disp=a.amp*math.sin(2*math.pi*a.freq*t-a.k*a.x[i-200])
            b_disp=b.amp*math.sin(2*math.pi*b.freq*t-b.k*b.x[i-200])
            if int(a_disp)==int(b_disp):
                pygame.draw.circle(screen, (200, 200, 0), (int(200 + a.x[i - 200]), int(450 + a_disp)), 5, 0)
            else:
                pygame.draw.circle(screen, (100, 0, 0), (int(200 + a.x[i - 200]), int(450 + a_disp)), 5, 0)
                pygame.draw.circle(screen, (0, 100, 0), (int(200 + b.x[i - 200]), int(450 + b_disp)), 5, 0)

            pygame.draw.circle(screen, (0, 0, 255), (int(200 + b.x[i - 200]), int(450 + a_disp+b_disp)), 5, 0)
            if not pause:
                i+=20
            else:
                loop_time = time.time()
                while True:
                    chk(a,b)
                    if not pause:
                        break
                beg_time=beg_time+time.time()-loop_time

        ctrl(a,b)
        chk(a,b)
        pygame.display.update()
        clock.tick(60)
#run_wave()