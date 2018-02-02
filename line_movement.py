import functions as fn
import drawings as dr
import pygame
import math

def movement(angle,screen, width,setting,time,move):

    rad = setting.wire_length*40
    for_cos=(math.sqrt(setting.gravity/setting.wire_length)*time)
    if move.check_position==True:
        ang=90+angle*math.cos(math.radians(for_cos))

    else:
        ang = 90 - angle * math.cos(math.radians(for_cos))
    #checking for pendulum loop
    if int(math.cos(math.radians(for_cos)) * 10000) == 9999:
        setting.loop += 1



    x2 = width + rad * math.cos(math.radians(ang))
    y2 = 0 + rad * math.sin(math.radians(ang))
    #screen.fill(setting.bg_color)
    #print wire and bob during movement
    pygame.draw.aaline(screen, setting.line_color, (width, 0), (x2, y2), 1)
    pygame.draw.circle(screen,setting.bob_color,(int(x2),int(y2)),10,2)

    dr.dotted_line(screen,setting)

