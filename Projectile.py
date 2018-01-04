#impoting libraries
import math
import pygame
import time
import sys
import numpy

#Horizontal Projectile calculation function
def horiz(v0,Ang,dt):
    cosA = math.cos(math.radians(Ang))
    sinA = math.sin(math.radians(Ang))
    x = v0*dt*cosA
    y = v0 *dt *sinA - (1/2)*9.8*dt*dt
    return plot(x , y)
#Vertical Projectile Calculation Functio
def Vert(u,h,dt):
    x = u * dt
    y = h - (1 / 2) * 10 * dt * dt
    return plot(x, y)
#Function for ploting
def plot(x,y):
   return [60 + x, 733 - y,y]
#Function for drawing borderline
def border(screen):
    pygame.draw.line(screen,[0,0,0],(10,10),(10,758),4)
    pygame.draw.line(screen, [0,0,0], (10, 10), (1356,10), 4)
    pygame.draw.line(screen, [0,0,0], (10, 758), (1356, 758), 4)
    pygame.draw.line(screen, [0,0,0], (1356, 10), (1356, 758), 4)

#Function for axes
def axes(screen):
    pygame.draw.line(screen,[0,0,0], (60,35), (60,733),2)
    pygame.draw.line(screen, [0, 0, 0], (60, 733),(1306, 733),2)

#function for displaying the image
def mainPro():
    Velocity = float(input("Enter a velocity"))
    Angle = float(input("Enter a angle"))
    dt = 0
    pygame.init()
    pygame.display.set_caption('Projectile Motion')
    screen = pygame.display.set_mode((1366,768))
    running = True
    gameExit = False
    screen.fill([255,255,255])
    border(screen)
    axes(screen)
    pygame.display.flip()

    while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

            x,y,check= horiz(Velocity,Angle,dt)
            if check < 0:
                running = False

            dt =dt + 0.001
            pygame.draw.line(screen, [0, 0, 0], (x, y), (x,y), 4)
            pygame.display.update()
            pygame.draw.line(screen, [255,0,0], (x,y), (x,y),4)





mainPro()



