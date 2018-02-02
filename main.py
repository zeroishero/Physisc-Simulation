import pygame
import math
import os
import sys


from settings import arc_main
from settings import ai_settings

import functions as fn
from settings import Line_move
import line_movement as lm
from images import image
import drawings as dr


def program():
    #Pygame Initialize
    pygame.init()
    global angle

    # Set Class and pygame.sprite

    setting = ai_settings()
    arc = arc_main(0, 0)
    angle = arc.angle
    move = Line_move()


    #Set screen
    scr = pygame.display.set_mode((setting.scr_width, setting.scr_height))
    scr.fill(setting.bg_color)
    pygame.display.set_caption("Display")
    width = int(setting.scr_width / 2)


    #Initial straight Dotted Line
    dr.dotted_line(scr,setting)

    img = image(scr, setting)
    dr.set_rect(scr,setting)
    pygame.display.update()
    #Check and run main codes
    while True:

        fn.check_events(move,scr,arc,setting)

        if move.mouse_movement == True:# and event.type == pygame.MOUSEMOTION:
            posi = pygame.mouse.get_pos()
            dr.draw_line(posi,scr, width, setting)
            #Dotted Line
            dr.dotted_line(scr,setting)

        if move.check == True:
            #Process movement and draw Pendulum
            lm.movement(arc.angle, scr, width, setting,move.time,move)
            move.time = move.time + 1
            # Limiting Time variable value as it increases to large value
            if setting.loop >= 10:
                move.time = 0
                setting.loop = 0
        lm.movement(arc.angle, scr, width, setting, move.time, move)
        dr.draw_arc(scr,width,setting)
        dr.draw_limiter(scr,arc,width,setting)

        #Show the display
        pygame.display.update(((setting.left+200,0),(setting.scr_width,setting.scr_height)))
        pygame.display.update(((0, setting.top+200), (setting.left+200, setting.scr_height)))
        scr.fill(setting.bg_color)
        #Slow the clock
        pygame.time.delay(10)

program()