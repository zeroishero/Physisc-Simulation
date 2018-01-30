# Module for the simulation of collision in 2 dimension
import ElasticCollision
import pygame
import sys


def mouse_button(screen, x1, y1, x2, y2, r1, r2):
    pos1 = (x1, y1)
    pos2 = (x2, y2)
    moving = True
    for event in pygame.event.get():
        initial_pos = pygame.mouse.get_pos()
        initial_x = initial_pos[0]
        initial_y = initial_pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN and (x1+r1) > initial_x > (x1-r1) and (y1+r1) > initial_y > (y1-r1):
            while moving:
                for sub_event in pygame.event.get():
                    if sub_event.type == pygame.MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        screen.fill((255, 255, 255))
                        ElasticCollision.border(screen)
                        pygame.draw.circle(screen, (255, 0, 0), pos, r1, 0)
                        pygame.draw.circle(screen, (255, 0, 0), pos, r2, 0)
                        pygame.display.flip()
                        pygame.display.update()
                    if sub_event.type == pygame.MOUSEBUTTONUP:
                        moving = False
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ElasticCollision.pause_program()
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    return pos1, pos2


def collision2d():  # Function for the main program loop
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Physics Simulation')
    pygame.display.flip()
    done = 0
    x1 = 200
    y1 = 384
    x2 = 1000
    y2 = 384
    r1 = 50
    r2 = 50
    while not done:  # Infinite program loop
        screen.fill((255, 255, 255))
        ElasticCollision.border(screen)
        # ElasticCollision.display_value()
        pygame.draw.circle(screen, (255, 0, 0), (int(x1), int(y1)), r1, 0)
        pygame.draw.circle(screen, (255, 0, 0), (int(x2), int(y2)), r2, 0)
        pos = mouse_button(screen, x1, y1, x2, y2, r1, r2)
        x1 = pos[0]
        y1 = pos[1]
        pygame.display.flip()
        pygame.display.update()


collision2d()
pygame.quit()
quit()
