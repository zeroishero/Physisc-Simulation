# Module for the simulation of Elastic collision under Collision topic
import pygame
import sys


def border(screen):
    pygame.draw.line(screen, [0, 0, 0], (10, 10), (1356, 10), 4)
    pygame.draw.line(screen, [0, 0, 0], (10, 10), (10, 758), 4)
    pygame.draw.line(screen, [0, 0, 0], (1356, 10), (1356, 758), 4)
    pygame.draw.line(screen, [0, 0, 0], (10, 758), (1356, 758), 4)
    # For creating the box for displaying the values while simulation
    pygame.draw.line(screen, [0, 0, 0], (950, 25), (1335, 25), 3)
    pygame.draw.line(screen, [0, 0, 0], (950, 25), (950, 120), 3)
    pygame.draw.line(screen, [0, 0, 0], (950, 120), (1335, 120), 3)
    pygame.draw.line(screen, [0, 0, 0], (1335, 25), (1335, 120), 3)


class DisplayDetails:  # Class for displaying the message while rendering the required values
    def __init__(self, screen, pos, message):  # Variable initialization function
        self.font = pygame.font.SysFont("Courier", 18, bold=False)
        self.screen_text = self.font.render(message, True, (0, 0, 255))
        self.location = pos
        self.screen = screen

    def display_details(self):  # Function for displaying the values
        self.screen.blit(self.screen_text, self.location)


class DisplayValues:  # Class for displaying the required values of the variables
    def __init__(self, screen, pos, value):  # Function for variable initialization
        self.font = pygame.font.SysFont("Courier", 18, bold=False)
        self.screen = screen
        self.screen_value = self.font.render(value, True, (0, 0, 255))
        self.location = pos

    def display_value(self):  # Function for rendering the values in variables
        self.screen.blit(self.screen_value, self.location)


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


# Function for checking whether collision has taken place and calculating velocity after collision
def has_collided(x1, x2, r1, r2, u1, u2, m1, m2, collision_type):
    # Condition fulfilling elastic collision(for calculation of velocity)
    if (int(x1) + r1) >= (int(x2) - r2) and collision_type == 1:
        v1 = (((m1 - m2)/(m1 + m2)) * u1) + (((2 * m2)/(m1 + m2)) * u2)
        v2 = (((2 * m1)/(m1 + m2)) * u1) + (((m2 - m1)/(m1 + m2)) * u2)
        # v1 = (u1 * (m1 - m2) + (2 * m2 * u2)) / (m1 + m2)
        # v2 = (u2 * (m2 - m1) + (2 * m1 * u1)) / (m1 + m2)
        return v1, v2
    # Condition fulfilling inelastic collision(for calculation of velocity)
    elif (int(x1) + r1) >= (int(x2) - r2) and collision_type == 2:
        v1 = v2 = ((m1 * u1) + (m2 * u2))/(m1 + m2)
        return v1, v2
    # Condition fulfilling elastic collision in the left boundary
    elif (int(x1) - r1) <= 10 and collision_type == 1:
        v1 = -u1
        v2 = u2
        return v1, v2
    # Condition fulfilling inelastic collision in the left boundary
    elif (int(x1) - r1) <= 10 and collision_type == 2:
        v1 = -u1
        v2 = -u2
        return v1, v2
    # Condition fulfilling elastic collision in the right boundary
    elif (int(x2) + r2) >= 1356 and collision_type == 1:
        v1 = u1
        v2 = -u2
        return v1, v2
    # Condition fulfilling inelastic collision in the right boundary
    elif (int(x2) + r2) >= 1356 and collision_type == 2:
        v1 = -u1
        v2 = -u2
        return v1, v2
    else:
        v1 = u1
        v2 = u2
        return v1, v2


def obj_move(x1, x2, r1, r2, u1, u2, m1, m2, dt, collision_type):  # Function for moving the objects on the screen
    v1, v2 = has_collided(x1, x2, r1, r2, u1, u2, m1, m2, collision_type)  # Checking whether the objects have collided
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
    dt = 0.1
    while not done:  # Infinite program loop
        screen.fill((255, 255, 255))
        border(screen)
        value_mass1 = str(m1)  # Converting the value of mass to string
        value_mass2 = str(m2)
        temp_value1 = u1  # Assigning temporary variable for storing velocity in order to reverse the sign if negative
        temp_value2 = u2
        if u1 < 0:
            temp_value1 = -u1
        if u2 < 0:
            temp_value2 = -u2
        formatted_u1 = '{temp_value:0.3f}'.format(temp_value=temp_value1)  # For displaying only 3 digits after decimal
        formatted_u2 = '{temp_value:0.3f}'.format(temp_value=temp_value2)
        value_velocity1 = str(formatted_u1)  # Converting value of velocity to string
        value_velocity2 = str(formatted_u2)
        mass1 = DisplayDetails(screen, (960, 35), 'Mass of first object: ')
        mass2 = DisplayDetails(screen, (960, 55), 'Mass of second object: ')
        velocity1 = DisplayDetails(screen, (960, 75), 'Velocity of first object: ')
        velocity2 = DisplayDetails(screen, (960, 95), 'Velocity of second object: ')
        mass_value1 = DisplayValues(screen, (1260, 35), value_mass1)
        mass_value2 = DisplayValues(screen, (1260, 55), value_mass2)
        velocity_value1 = DisplayValues(screen, (1260, 75), value_velocity1)
        velocity_value2 = DisplayValues(screen, (1260, 95), value_velocity2)
        mass1.display_details()
        mass2.display_details()
        velocity1.display_details()
        velocity2.display_details()
        mass_value1.display_value()
        mass_value2.display_value()
        velocity_value1.display_value()
        velocity_value2.display_value()
        event_handle()
        pygame.draw.circle(screen, (255, 0, 0), (int(x1), y1), r1, 0)
        pygame.draw.circle(screen, (0, 255, 0), (int(x2), y2), r2, 0)
        x = obj_move(x1, x2, r1, r2, u1, u2, m1, m2, dt, collision_type)
        x1 = x[0]  # Retrieving the coordinate of the point where the body is
        x2 = x[1]
        u1 = x[2]  # Retrieving the velocity with which the body moves
        u2 = x[3]
        pygame.display.flip()


def elastic_collision():
    main_program()
    pygame.quit()
    quit()


if __name__ == '__main__':
    elastic_collision()
