import pygame
import math



import functions as fn

pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 15)

def draw_arc(scr, width, setting):
    for ang in range(0, 181, 1):
        x1 = width + 150 * math.cos(math.radians(ang))
        y1 = 0 + 150 * math.sin(math.radians(ang))
        if ang % 10 != 0 and ang % 5 != 0:
            rad = 155
        elif ang % 10 == 0:
            rad = 165
        else:
            rad = 160
        x2 = width + rad * math.cos(math.radians(ang))
        y2 = 0 + rad * math.sin(math.radians(ang))
        # Draw the arc
        pygame.draw.aaline(scr,setting.arc_color,  (x1, y1), (x2, y2), 1)

def draw_limiter(scr, arc, width, setting):
    for i in range(1, 3):
        if i == 1:
            ang = math.radians(90 + arc.angle)
        else:
            ang = math.radians(90 - arc.angle)

        if arc.angle != 0 and arc.repeat == 0:
            arc.repeat = 1
        x1 = width + 140 * math.cos(ang)
        y1 = 0 + 140 * math.sin(ang)
        rad = 146
        x2 = width + rad * math.cos(ang)
        y2 = 0 + rad * math.sin(ang)
        # Draw the arc
        pygame.draw.aaline(scr, setting.limiter_color, (x1, y1), (x2, y2), 1)

def dotted_line(screen, setting):
    width = int(setting.scr_width / 2)
    for i in range(0, width, 20):
        pygame.draw.aaline(screen,setting.dottedline_color,(width, i), (width, i + 10),1)

def draw_line(posi,screen,width,setting):
    #Check for left and right ; and process
    #end_rad for arc angle and angle for wire of pendulum
    posi_x, posi_y = posi
    if posi_x < width:
        angle = 90 + fn.ang(posi, width, setting)
        end_rad=math.radians(270-fn.ang(posi, width, setting))
        #rect=[left,top,width,height]
        rect=[width - 60, -60, 120, 120]
        pygame.draw.arc(screen, setting.ang_arc_color, rect, end_rad, math.radians(270), 1)
    else:
        angle = 90 - fn.ang(posi, width, setting)
        end_rad = math.radians(270+fn.ang(posi, width, setting))
        # rect=[left,top,width,height]
        rect=[width - 60, -60, 120, 120]
        pygame.draw.arc(screen, setting.ang_arc_color, rect, math.radians(270), end_rad, 1)
    #print angle
    textsurface = myfont.render(str(fn.ang(posi, width, setting)), False, (255, 0, 0))
    screen.blit(textsurface, (width-10, 0))
    #check ending position of wire
    rad = setting.wire_length*40
    x2 = width + rad * math.cos(math.radians(angle))
    y2 = 0 + rad * math.sin(math.radians(angle))
    #draw wire and bob before movement
    pygame.draw.aaline(screen, setting.line_color, (width, 0), (x2, y2), 1)
    pygame.draw.circle(screen, setting.bob_color, (int(x2), int(y2)), 10, 2)

def set_rect(screen, setting):
    pygame.draw.rect(screen, setting.box_color,(setting.top,setting.left,200,200),1)
    pygame.draw.rect(screen, setting.box_color, (setting.top, setting.left, 200, 35), 1)
    pygame.draw.rect(screen, setting.box_color, (setting.top, setting.left, 200, 120), 1)