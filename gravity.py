import pygame
import sys
import math
import random

pygame.init()

# display window
display_size = display_width, display_height = 1366, 768
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption('Gravity Simulation')

# colors:
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
golden = (255, 215, 0)

# constants
G = 6.67 * 10**(-11)
gravity_angle = math.pi
gravity_mag = 0.002
air_res = 0.999     #air resistance

# state of simulation:
animationExit = False

# border line
'''def border():
    pygame.draw.rect(screen, black, [0, 0, display_width, display_height], 10)
'''


# event handling function
"""def event_handle(x, y, radius):
    for event in pygame.event.get():
        # quit program X or escape
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# get mouse position
#def event_mouse(x, y, radius):
    #for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if math.hypot(x - mouseX, y - mouseY) <= radius:
                x = mouseX
                y = mouseY
                """



'''  # check if mouse is clicked on the object
def mouse_click(x, y, radius):
    mouse_x, mouse_y = event_mouse()
    if math.hypot(x - mouse_x, y - mouse_y) <= radius:
        golden = white
        return golden'''


    # draw circular objects on screen
def display_obj(x, y, radius):
    pygame.draw.circle(screen, golden, [int(x), int(y)], radius)

# generate random objects
def random_obj():
    radius = random.randint(15, 40)
    x = random.randint(radius, display_width - radius)
    y = display_height - radius
    return x, y, radius

# vector addition function
def vector_add(angle1, l1, angle2, l2):
    x = math.sin(angle1) * l1 + math.sin(angle2) * l2
    y = math.cos(angle1) * l1 + math.cos(angle2) * l2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return angle, length

# moving particles
def move_obj(speed, angle, x, y):
    angle, speed = vector_add(angle, speed, gravity_angle, gravity_mag)
    x += math.sin(angle) * speed
    y -= math.cos(angle) * speed
    speed *= air_res
    return x, y, speed, angle

# strike boundary
def boundary(x, y, angle, radius):
    # left boundary
    if x < radius:
        x = 2*radius - x
        angle = -angle

    # right boundary
    elif x > display_width - radius:
        x = 2*(display_width - radius) - x
        angle = -angle

    # top boundary
    if y < radius:
        y = 2*radius - y
        angle = math.pi - angle

    # bottom boundary
    elif y > display_height - radius:
        y = 2*(display_height - radius) - y
        angle = math.pi - angle

    return x, y, angle





# main function
def main():
    # speeds and angles of object
    speed = -2
    angle = 3*math.pi/4

    # random object position and dimension
    x, y, radius = random_obj()
    # x_initial, y_initial = x, y

    mouse_click = False

    # main program loop
    while not animationExit:
        # event handling
        for event in pygame.event.get():
            # quit program X or escape
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # detect mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if math.hypot(x - mouseX, y - mouseY) <= radius:
                    mouse_click = True
                    #x = mouseX
                    #y = mouseY

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_click = False

        if mouse_click == True:
            (mouseX, mouseY) = pygame.mouse.get_pos()

            dx = mouseX - x
            dy = mouseY - y
            #x = mouseX
            #y = mouseY
            angle = 0.5 * math.pi + math.atan2(dy, dx)
            speed = math.hypot(dx, dy)*0.01


        screen.fill(black)
        #border()
        if mouse_click == False:
            x, y, speed, angle = move_obj(speed, angle, x, y)
            x, y, angle = boundary(x, y, angle, radius)

        display_obj(x, y, radius)

        pygame.display.update()


main()

pygame.quit()
sys.exit()
