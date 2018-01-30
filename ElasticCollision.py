# Module for the simulation of Elastic collision under Collision topic
import pygame
import sys


def border(screen):
    pygame.draw.line(screen, [0, 0, 0], (10, 10), (1356, 10), 4)
    pygame.draw.line(screen, [0, 0, 0], (10, 10), (10, 758), 4)
    pygame.draw.line(screen, [0, 0, 0], (1356, 10), (1356, 758), 4)
    pygame.draw.line(screen, [0, 0, 0], (10, 758), (1356, 758), 4)


# def display_value():


def pause_program():  # Function for pausing the program
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()


def event_handle():  # Event handling function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause_program()
            if event.key == pygame.K_ESCAPE:
                sys.exit()


def size_obj(m1, m2):  # Function for determining which of the two objects is bigger
    if m1 > m2:
        r1 = 60
        r2 = 40
    elif m1 < m2:
        r1 = 40
        r2 = 60
    else:
        r1 = r2 = 50
    return r1, r2


def has_collided(x1, x2, r1, r2, u1, u2, m1, m2, collision_type):  # Function for checking collision and calculating velocity
    # Condition fulfilling elastic collision(for calculation of velocity)
    if (int(x1) + r1) > (int(x2) - r2) and collision_type == 1:
        v1 = (((m1 - m2)/(m1 + m2)) * u1) + (((2 * m2)/(m1 + m2)) * u2)
        v2 = (((2 * m1)/(m1 + m2)) * u1) + (((m2 - m1)/(m1 + m2)) * u2)
        # v1 = (u1 * (m1 - m2) + (2 * m2 * u2)) / (m1 + m2)
        # v2 = (u2 * (m2 - m1) + (2 * m1 * u1)) / (m1 + m2)
        return v1, v2
    # Condition fulfilling inelastic collision(for calculation of velocity)
    elif (int(x1) + r1) > (int(x2) - r2) and collision_type == 2:
        v1 = v2 = ((m1 * u1) + (m2 * u2))/(m1 + m2)
        return v1, v2
    # Condition fulfilling elastic collision in the left boundary
    elif (int(x1) - r1) < 10 and collision_type == 1:
        v1 = -u1
        v2 = u2
        return v1, v2
    # Condition fulfilling inelastic collision in the left boundary
    elif (int(x1) - r1) < 10 and collision_type == 2:
        v1 = -u1
        v2 = -u2
        return v1, v2
    # Condition fulfilling elastic collision in the right boundary
    elif (int(x2) + r2) > 1356 and collision_type == 1:
        v1 = u1
        v2 = -u2
        return v1, v2
    # Condition fulfilling inelastic collision in the right boundary
    elif (int(x2) + r2) > 1356 and collision_type == 2:
        v1 = -u1
        v2 = -u2
        return v1, v2
    else:
        v1 = u1
        v2 = u2
        return v1, v2


def obj_move(x1, x2, r1, r2, u1, u2, m1, m2, dt, collision_type):  # Function for moving the objects on the screen
    v = has_collided(x1, x2, r1, r2, u1, u2, m1, m2, collision_type)  # Checking whether the objects have collided
    v1 = v[0]
    v2 = v[1]
    x1 += v1 * dt
    x2 += v2 * dt
    return x1, x2, v1, v2


def main_program():  # Function for the main program loop
    # Taking input from user (from CLI at the moment)
    collision_type = int(input('''Type of collision:
    1) Elastic
    2) Inelastic '''))
    m1 = int(input('Mass of first object: '))
    m2 = int(input('Mass of second object: '))
    u1 = int(input('Velocity of first body: '))
    u2 = int(input('Velocity of second body: '))
    direction = int(input('''Is the direction? 
    1) Same? or 
    2) Opposite? '''))
    if direction == 2:
        u2 = -u2
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("Physics Simulation")
    pygame.display.flip()
    done = 0
    # For the position of the objects in different conditions
    x1 = 200
    x2 = 1000
    if u1 == 0 and u2 != 0:
        x1 = 550
        x2 = 1000
    elif (u1 != 0 and u2 == 0) or (direction == 1):
        x1 = 200
        x2 = 650
    y1 = y2 = 384
    # For the size of the objects under different conditions
    r = size_obj(m1, m2)
    r1 = r[0]  # Retrieving the radius of the objects
    r2 = r[1]
    dt = 0
    while not done:  # Infinite program loop
        screen.fill((255, 255, 255))
        border(screen)
        # display_value()
        event_handle()
        pygame.draw.circle(screen, (255, 0, 0), (int(x1), y1), r1, 0)
        pygame.draw.circle(screen, (255, 0, 0), (int(x2), y2), r2, 0)
        x = obj_move(x1, x2, r1, r2, u1, u2, m1, m2, dt, collision_type)
        x1 = x[0]  # Retrieving the coordinate of the point where the body is
        x2 = x[1]
        u1 = x[2]  # Retrieving the velocity with which the body moves
        u2 = x[3]
        dt += 0.0001
        pygame.display.flip()
        pygame.display.update()


def elastic_collision():
    main_program()
    pygame.quit()
    quit()


if __name__ == 'main':
    elastic_collision()
