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
#Function for Combined Projectile
def combined(v0,Ang,h,dt):
    cosA = math.cos(math.radians(Ang))
    sinA = math.sin(math.radians(Ang))
    x = v0 * dt * cosA
    y = v0 * dt * sinA - (1 / 2) * 9.8 * dt * dt + h
    return plot(x,y)
#Function that convert right hand co-ordinate to left hand
def plot(x,y):
   return [60 + x, 733 - y,y]
#Function for drawing borderline
def border(screen):
    pygame.draw.line(screen,[0,0,0],(10,10),(10,758),4)
    pygame.draw.line(screen, [0,0,0], (10, 10), (1356,10), 4)
    pygame.draw.line(screen, [0,0,0], (10, 758), (1356, 758), 4)
    pygame.draw.line(screen, [0,0,0], (1356, 10), (1356, 758), 4)
#function that returns integer value of plot
def int_plot(x,y):
    return(int(x),int(y))
#function that reverses left hand co-ordinate to right hand.
#Function for axes
def axes(screen):
    pygame.draw.line(screen,[0,0,0], (58,35), (58,733),2)
    pygame.draw.line(screen, [0, 0, 0], (58, 733),(1306, 733),2)
#function that calculate instaneous for horizontal projectile




#function for displaying the image
def mainPro():
    Velocity = float(input("Enter a velocity"))
    Angle = float(input("Enter a angle"))
    Height = float(input("Enter a height"))
    dt = 0
    color_circle = [255,204,0]
    pygame.init()
    pygame.display.set_caption('Projectile Motion')
    screen = pygame.display.set_mode((1366,768))
    running = True
    gameExit = False
    screen.fill([255,255,255])
    border(screen)
    #axes(screen)
    pygame.display.flip()
    circle = pygame.image.load('Picture\Circle.png')#Use for Indicating current position
    circle2 = pygame.image.load('Picture\Circle2.png')#Use For Erasing the before position
    points =[]
    int_points = []
    dic_time = {}
    while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            x,y,check = combined(Velocity,Angle,Height,dt)
            if check < 0:
                running = False
            points.append((x,y))
            int_points.append(int_plot(x,y))
            n = len(int_points)
            if n > 2 and int_points[n-2] == int_points[n-1]:
                del int_points[n-1]
                dic_time.update({int_points[n-2]:dt})
            else:
                dic_time.update({int_points[n-2]:dt})
            dt =dt + 0.001
            #pygame.draw.circle(screen, (0, 0, 255), (int(x),int(y)), 1.5, 1)
            #pygame.draw.line(screen, [0, 0, 0], (x, y), (x,y), 3)
            if y <= 723 and x > 5:
                #screen.blit(circle,(x,y))
                pygame.draw.circle(screen,[255,204,0],int_plot(x,y),5)
                axes(screen)
                pygame.display.update()
                #screen.blit(circle2, (x, y))
                pygame.draw.circle(screen, [255, 255, 255], int_plot(x, y),5)
                # pygame.draw.aaline(screen, [255,0,0], (x,y), (x,y),0)


    inform(points,int_points,screen,dic_time)
#function for displaying information
def inform(points,int_points,screen,dict):
    pygame.init()
    screen.fill([255, 255, 255])
    border(screen)
    pygame.display.flip()
    showing =True
    x = 0

    while x < (len(points) - 1):
        pygame.draw.aaline(screen,[255,0,0],points[x],points[x+1],0)
        x = x + 1
    print(points)
    print(int_points)
    print(dict)
    while showing:
        axes(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showing = False

            posx,posy = pygame.mouse.get_pos()
            if int_points.count((posx,posy)) == 1:
                print(dict[(posx,posy)])




mainPro()



