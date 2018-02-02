import pygame
import sys
import math
import time
screen=pygame.display.set_mode((1366,768))
pygame.display.set_caption("Electrostatics")

class charge:
    def __init__(self,q,mass,x,y):
        self.q=q*(1.6e-19)
        self.mass=mass
        self.x=x
        self.y=y
        self.F1ang=0
        self.F2ang=0
        self.F1x=0
        self.F2x=0
        self.Fx=0
        self.a1x=0
        self.a2x=0
        self.v1x=0
        self.v2x=0
        self.vx=0
        self.s1x=0
        self.s2x=0
        self.sx=0

        self.F1y=0
        self.F2y=0
        self.Fy=0
        self.a1y=0
        self.a2y=0
        self.ay=0
        self.v1y=0
        self.v2y=0
        self.vy=0
        self.s1y=0
        self.s2y=0
        self.sy=0


def chk():
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()

def calc(a,b,c):
    dt=.01
    #angle calculation for A with b
    slope1=(a.y-b.y)/(a.x-b.x)
    a.F1ang=math.atan(slope1)

    a.F1x=(a.q*b.q)/(4*math.pi*8.85e-12*( (b.x-a.x)**2 +(b.y-a.y)**2))*math.cos(a.F1ang)
    a.a1x=a.F1x/a.mass
    a.v1x=a.a1x*dt
    a.s1x=a.v1x*dt

    a.F1y = (a.q * b.q) / (4 * math.pi * 8.85e-12 * ((b.x - a.x) ** 2 + (b.y - a.y) ** 2)) * math.sin(a.F1ang)
    a.a1y = a.F1y / a.mass
    a.v1y = a.a1y * dt
    a.s1y = a.v1y * dt

    #angle calculation for A with c
    ty=a.y-c.y
    tx=a.x-c.x
    slope=abs(ty/tx)
    if tx>=0 and ty>=0:
        a.F2ang=math.atan(slope)
    elif tx<0 and ty>=0:
        a.F2ang=math.pi-math.atan(slope)
    elif tx<0 and ty<0:
        a.F2ang=math.pi+math.atan(slope)
    elif tx>=0 and ty<0:
        a.F2ang=2*math.pi-math.atan(slope)

    a.F2x = ((a.q * c.q) / (4 * math.pi * 8.85e-12 * ( (abs(c.x - a.x) ** 2) + (abs(c.y - a.y) ** 2)))) * math.cos(a.F2ang)
    a.a2x = a.F2x / a.mass
    a.v2x = a.v2x + a.a2x * dt
    a.s2x = a.v2x * dt

    a.F2y = ((a.q * c.q) / (4 * math.pi * 8.85e-12 * ((abs(c.x - a.x) ** 2) + (abs(c.y - a.y) ** 2)))) * math.sin(a.F2ang)
    a.a2y = a.F2y / a.mass
    a.v2y = a.v2y + a.a2y * dt
    a.s2y = a.v2y * dt

    a.sx=a.s1x+a.s2x
    a.sy=a.s1y+a.s2y
    a.x=a.x+a.sx
    a.y=a.y+a.sy
def run_electro():
    a=charge(100,9.1e-31,0,0)
    b=charge(100,9.1e-31,-100,-100)
    c=charge(100,9.1e-31,100,-100)
    while True:
        loop_time=time.time()
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen,(0,0,255),(int(683+a.x),int(384-a.y)),5)
        pygame.draw.circle(screen, (0, 0, 255), (683 + b.x, 384 - b.y), 5)
        pygame.draw.circle(screen, (0, 0, 255), (683 + c.x, 384 - c.y), 5)
        calc(a,b,c)

        pygame.display.update()
        chk()

run_electro()
