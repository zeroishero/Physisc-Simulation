import pygame
import sys
import math
import drawings as dr
from images import image

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)


def check_events(move,screen,arc,setting):

    width = int(setting.scr_width / 2)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            import Main_Final
            Main_Final.main()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                import Menu
                Menu.menu()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            posi = pygame.mouse.get_pos()
            posi_x,posi_y=posi

            if not(posi_x<210 and posi_y<210):
                move.mouse_movement = True
                move.check = False
                setting.loop = 0
                dr.draw_line(posi, screen, width, setting)
            else:
                if dist(posi, setting.gr_add_pos) < setting.img_radius:
                    setting.gravity += .1
                if dist(posi, setting.gr_subtract_pos) < setting.img_radius:
                    setting.gravity -= .1
                if dist(posi, setting.ln_add_pos) < setting.img_radius:
                    setting.wire_length += .1
                if dist(posi, setting.ln_subtract_pos) < setting.img_radius:
                    setting.wire_length -= .1
                img = image(screen, setting)
                dr.set_rect(screen, setting)
                pygame.display.update((setting.left,setting.top,200,200))

        elif event.type == pygame.MOUSEBUTTONUP:
            #Check pendulum start from left or right
            posi_x,posi_y=posi=pygame.mouse.get_pos()
            if move.mouse_movement:
                move.time = 0
                if posi_x > width:
                    move.check_position = False
                else:
                    move.check_position = True
                arc.angle = (ang(posi, width, setting))
                arc.repeat = 0
                # draw pendulum
                dr.draw_line(posi, screen, width, setting)
                # print angle
                textsurface = myfont.render(str(ang(posi, width, setting)), False, (255, 0, 0))
                screen.blit(textsurface, (width - 10, 0))
                # dotted line
                dr.dotted_line(screen, setting)
                move.mouse_movement = False
                move.check = True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                move.check=False
        else:
            move.check=True

def ang(pt1,width,setting):
    pt1_x,pt1_y=pt1
    (x1,y1)=(pt1_x-width,pt1_y)
    (x2,y2)=(0,setting.scr_height)
    inner_product = x1 * x2 + y1 * y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    #cosX=(|(a,b)|)/(|a||b|)
    deg=math.degrees(math.acos(inner_product/(len1*len2)))
    return int(deg)

def dist(posi_mouse,posi_img):
    x1,y1=posi_mouse
    x2,y2=posi_img
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance




