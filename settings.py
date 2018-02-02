import pygame
import os

class ai_settings():
    def __init__(self):
        self.scr_width=1366
        self.scr_height=768
        self.bg_color=(0,0,0)
        self.wire_length=10
        self.arc_color=(0,200,0)
        self.line_color=(200, 200, 0)
        self.limiter_color=(0, 255, 0)
        self.dottedline_color=(200, 200, 0)
        self.ang_arc_color=(0, 0, 255)
        self.bob_color=(255, 0, 0)
        self.gravity=float(9.8)
        self.loop=0

        self.img_size = (30, 30)
        self.img_width,self.img_height=self.img_size
        self.img_radius=self.img_width/2
        self.set_rect_topleft=(10,10)
        self.top,self.left=self.set_rect_topleft
        self.gr_add_pos=(self.left+180,self.top+80)
        self.gr_subtract_pos=(self.left+20,self.top+80)
        self.ln_add_pos = (self.left+180, self.top+170)
        self.ln_subtract_pos = (self.left+20, self.top+170)

        self.box_color=(255,255,255)
class arc_main:
    def __init__(self,ang,repeat):
        self.angle=ang
        self.loop_angle=ang
        self.repeat=repeat


class Line_move():
    def __init__(self):
        self.mouse_movement=False
        self.check=False
        self.check_position=True
        self.time=0