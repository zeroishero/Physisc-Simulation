# Module for the simulation of collision in 2 dimension
import ElasticCollision
import pygame
import sys


class Circle:
    def __init__(self, screen, r, x, y):
        self.screen = screen
        self.radius = r
        self.pos = (x, y)

    def draw_circle(self):
        pygame.draw.circle(self.screen, (255, 0, 0), self.pos, self.radius, 0)


def draw_circle(screen, x1, y1, x2, y2, r1, r2):  # Function for drawing the balls and borders on the screen
    screen.fill((255, 255, 255))
    ElasticCollision.border(screen)
    pygame.draw.circle(screen, (255, 0, 0), (int(x1), int(y1)), r1, 0)
    pygame.draw.circle(screen, (255, 0, 0), (int(x2), int(y2)), r2, 0)
    pygame.display.flip()


def plot_circle(circles_plotted):
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            circles_plotted += 1
    ElasticCollision.event_handle()
    return pos, circles_plotted


# Function for the movement of the object using mouse and event handling
'''def mouse_move_object(screen, x1, y1, x2, y2, r1, r2):
    pos1 = (x1, y1)
    pos2 = (x2, y2)
    moving = True
    for event in pygame.event.get():
        # Getting the initial position of the mouse cursor for checking the remaining conditions
        initial_pos = pygame.mouse.get_pos()
        initial_x = initial_pos[0]
        initial_y = initial_pos[1]
        # Checking whether the mouse cursor is inside the first ball or not
        if (x1 + r1) > initial_x > (x1 - r1) and (y1 + r1) > initial_y > (y1 - r1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                while moving:  # Loop for the movement of the ball until the mouse button is pressed
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.MOUSEMOTION:
                            pos1 = pygame.mouse.get_pos()
                            x1 = pos1[0]
                            y1 = pos1[1]
                            draw_circle(screen, x1, y1, x2, y2, r1, r2)
                        if sub_event.type == pygame.MOUSEBUTTONUP:
                            moving = False
        # Checking whether the mouse cursor is inside the second ball or not
        elif (x2 + r2) > initial_x > (x2 - r2) and (y2 + r2) > initial_y > (y2 - r2):
            if event.type == pygame.MOUSEBUTTONDOWN:
                while moving:  # Loop for the movement of the ball until the mouse button is pressed
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.MOUSEMOTION:
                            pos2 = pygame.mouse.get_pos()
                            x2 = pos2[0]
                            y2 = pos2[1]
                            draw_circle(screen, x1, y1, x2, y2, r1, r2)
                        if sub_event.type == pygame.MOUSEBUTTONUP:
                            moving = False
        # Event handling conditions as per the requirement
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ElasticCollision.pause_program()
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    return pos1, pos2'''


def main_program():  # Function for the main program loop
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Physics Simulation')
    pygame.display.flip()
    done = False
    plotted = False
    x1 = 200
    y1 = 384
    x2 = 1000
    y2 = 384
    r1 = 50
    r2 = 50
    circle_made = 0
    count = 0
    while not done:  # Infinite program loop
        screen.fill((255, 255, 255))
        ElasticCollision.border(screen)
        # display_value()
        ElasticCollision.event_handle()
        while not plotted:
            ElasticCollision.event_handle()
            pygame.display.flip()
            pos = plot_circle(circle_made)
            if pos[1] == 1 and count == 0:
                x1 = pos[0][0]
                y1 = pos[0][1]
                count += 1
                pygame.draw.circle(screen, (255, 0, 0), (x1, y1), r1, 0)
            if pos[1] == 2:
                x2 = pos[0][0]
                y2 = pos[0][1]
                pygame.draw.circle(screen, (255, 0, 0), (x2, y2), r2, 0)
                plotted = True
            circle_made = pos[1]
        circle1 = Circle(screen, r1, int(x1), int(y1))
        circle2 = Circle(screen, r2, int(x2), int(y2))
        circle1.draw_circle()
        circle2.draw_circle()
        move
        '''x1 = pos1[0]
        x2 = pos2[0]
        y1 = pos1[1]
        y2 = pos2[1]'''
        pygame.display.flip()


def collision2d():
    main_program()
    pygame.quit()
    quit()


if __name__ == '__main__':
    collision2d()
