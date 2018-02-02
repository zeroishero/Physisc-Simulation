import pygame
# screen = pygame.display.set_mode((1366,768))

class display_title:
    def __init__(self,message,colour,location,screen,size):
        self.font = pygame.font.SysFont('courier',size,bold= True,italic= False)
        self.screen_text = self.font.render(message,True,colour)
        self.location = location
        self.screen = screen
    def display(self):
        self.screen.blit(self.screen_text,self.location)



class display_value:
    def __init__(self,message,colour,location,screen):
        self.message = message
        self.colour = colour
        self.font = pygame.font.SysFont('courier',22,bold= False,italic= False)
        self.location = location
        self.screen = screen
    def add(self,value):
        self.message += value
    def sub(self):
        temp_value = self.message
        self.message = temp_value[:len(temp_value)-1]
    def value(self):
        return float(self.message)

    def display(self):
        screen_text = self.font.render(self.message, True, self.colour)
        self.screen.blit(screen_text,self.location)


def input_screen_projectile(screen):
    screen.fill([18,47,53])
    screen.fill([8,120,145],rect = [300,50,718,618])
    Title_Velocity = display_title("Enter a Velocity:",[64,59,48],(350,70+80),screen,25)
    Title_Velocity.display()
    Title_Angle = display_title("Enter a Angle:", [64,59,48], (350,160+80), screen, 25)
    Title_Angle.display()
    Title_height = display_title("Enter a Height:", [64,59,48],(350,260+80),screen,25)
    Title_submit = display_title("Submit",[255,255,255],(911, 583), screen,20)
    screen.fill([209,219,189],rect = [350,105+80,400,50])
    screen.fill([209, 219, 189], rect=[350, 200+80, 400, 50])
    screen.fill([209, 219, 189], rect=[350, 295+80, 400, 50])
    screen.fill([27,22,69],rect = [898,575,100,40])
    Title_height.display()
    Title_submit.display()
    pygame.display.flip()
    running = True
    velocity = ''
    value_velocity = display_value(velocity,[0,0,0],(355,105+93),screen)
    value_velocity.display()
    angle = ''
    value_angle = display_value(angle,[0,0,0],(355,200+93),screen)
    value_angle.display()
    height = ''
    value_height = display_value(height,[0,0,0],(355,295+93),screen)
    value_height.display()
    while running:
        velocity_input = False
        angle_input = False
        height_input = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()
                #for event2 in pygame.event.get():
                if (350 <= posx <= 750) and (185 <= posy <= 235):
                    while not velocity_input:

                        for sub_event in pygame.event.get():
                            if sub_event.type == pygame.KEYDOWN:
                                if sub_event.key == pygame.K_0:
                                    value_velocity.add('0')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_1:
                                    value_velocity.add('1')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_2:
                                    value_velocity.add('2')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_3:
                                    value_velocity.add('3')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_4:
                                    value_velocity.add('4')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_5:
                                    value_velocity.add('5')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_6:
                                    value_velocity.add('6')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_7:
                                    value_velocity.add('7')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_8:
                                    value_velocity.add('8')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_9:
                                    value_velocity.add('9')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_PERIOD:
                                    value_velocity.add('.')
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_BACKSPACE:
                                    value_velocity.sub()
                                    value_velocity.display()
                                elif sub_event.key == pygame.K_RETURN:
                                    velocity_input = True
                                screen.fill([209, 219, 189], rect=[350, 105 + 80, 400, 50])
                                value_velocity.display()

                                pygame.display.flip()
                if (350 <= posx <= 750) and (280 <= posy <= 330):
                    while not angle_input:
                        for sub_event in pygame.event.get():
                            if sub_event.type == pygame.KEYDOWN:
                                if sub_event.key == pygame.K_0:
                                    value_angle.add('0')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_1:
                                    value_angle.add('1')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_2:
                                    value_angle.add('2')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_3:
                                    value_angle.add('3')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_4:
                                    value_angle.add('4')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_5:
                                    value_angle.add('5')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_6:
                                    value_angle.add('6')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_7:
                                    value_angle.add('7')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_8:
                                    value_angle.add('8')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_9:
                                    value_angle.add('9')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_PERIOD:
                                    value_angle.add('.')
                                    value_angle.display()
                                elif sub_event.key == pygame.K_BACKSPACE:
                                    value_angle.sub()
                                    value_angle.display()
                                elif sub_event.key == pygame.K_RETURN:
                                    angle_input = True
                                screen.fill([209, 219, 189], rect=[350, 200 + 80, 400, 50])
                                value_angle.display()
                                pygame.display.flip()
                if (350 <= posx <= 750) and (375 <= posy <= 415 ):
                    while not height_input:
                        for sub_event in pygame.event.get():
                            if sub_event.type == pygame.KEYDOWN:
                                if sub_event.key == pygame.K_0:
                                    value_height.add('0')
                                    value_height.display()
                                elif sub_event.key == pygame.K_1:
                                    value_height.add('1')
                                    value_height.display()
                                elif sub_event.key == pygame.K_2:
                                    value_height.add('2')
                                    value_height.display()
                                elif sub_event.key == pygame.K_3:
                                    value_height.add('3')
                                    value_height.display()
                                elif sub_event.key == pygame.K_4:
                                    value_height.add('4')
                                    value_height.display()
                                elif sub_event.key == pygame.K_5:
                                    value_height.add('5')
                                    value_height.display()
                                elif sub_event.key == pygame.K_6:
                                    value_height.add('6')
                                    value_height.display()
                                elif sub_event.key == pygame.K_7:
                                    value_height.add('7')
                                    value_height.display()
                                elif sub_event.key == pygame.K_8:
                                    value_height.add('8')
                                    value_height.display()
                                elif sub_event.key == pygame.K_9:
                                    value_height.add('9')
                                    value_height.display()
                                elif sub_event.key == pygame.K_PERIOD:
                                    value_height.add('.')
                                    value_height.display()
                                elif sub_event.key == pygame.K_BACKSPACE:
                                    value_height.sub()
                                    value_height.display()
                                elif sub_event.key == pygame.K_RETURN:
                                    height_input = True
                                screen.fill([209, 219, 189], rect=[350, 295 + 80, 400, 50])
                                value_height.display()
                                pygame.display.flip()

                if (898<=posx<=989) and (575<=posy<=615):
                    running = False


        pygame.display.flip()
    Velocity = value_velocity.value()
    Angle = value_angle.value()
    Height = value_height.value()
    return [Velocity,Angle,Height]

def input_screen_Collision(screen):
     pygame.init()
     screen.fill([18, 47, 53])
     screen.fill([8, 120, 145], rect=[300, 50, 718, 618])
     Title_Mass1 = display_title("Mass of First Body:", [64, 59, 48], (350, 70 + 80), screen, 25)
     Title_Mass1.display()
     Title_Velocity1 = display_title("Velocity of First Body:", [64, 59, 48], (350, 160 + 80), screen, 25)
     Title_Velocity1.display()
     Title_Mass2= display_title("Mass of Second Body:", [64, 59, 48], (350, 260 + 80), screen, 25)
     Title_Mass2.display()
     Title_Velocity2 = display_title("Velocity of second Body:", [64, 59, 48], (350, 350 + 80), screen, 25)
     Title_Velocity2.display()
     Title_submit = display_title("Submit", [255, 255, 255], (911, 583), screen, 20)
     Title_submit.display()
     screen.fill([209, 219, 189], rect=[350, 105 + 80, 400, 50])
     screen.fill([209, 219, 189], rect=[350, 200 + 80, 400, 50])
     screen.fill([209, 219, 189], rect=[350, 295 + 80, 400, 50])
     screen.fill([209, 219, 189], rect=[350, 390 + 80, 400, 50])
     screen.fill([27, 22, 69], rect=[898, 575, 100, 40])
     Mass1 = ''
     value_Mass1 = display_value(Mass1, [0, 0, 0], (355, 105 + 93), screen)
     value_Mass1.display()
     Velocity1 = ''
     value_Velocity1= display_value(Velocity1, [0, 0, 0], (355, 200 + 93), screen)
     value_Velocity1.display()
     Mass2 = ''
     value_Mass2 = display_value(Mass2, [0, 0, 0], (355, 295 + 93), screen)
     value_Mass2.display()
     Velocity2 = ''
     value_Velocity2 = display_value(Velocity2, [0, 0, 0], (355, 390 + 93), screen)
     value_Velocity2.display()
     pygame.display.flip()
     running = True
     while running:
         Mass1_input = False
         Mass2_input = False
         Velocity1_input = False
         Velocity2_input = False
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             if event.type == pygame.MOUSEBUTTONDOWN:
                 posx, posy = pygame.mouse.get_pos()
                 # for event2 in pygame.event.get():
                 if (350 <= posx <= 750) and (185 <= posy <= 235):
                     while not Mass1_input:

                         for sub_event in pygame.event.get():
                             if sub_event.type == pygame.KEYDOWN:
                                 if sub_event.key == pygame.K_1:
                                     value_Mass1.add('1')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_0:
                                     value_Mass1.add('0')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_2:
                                     value_Mass1.add('2')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_3:
                                     value_Mass1.add('3')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_4:
                                     value_Mass1.add('4')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_5:
                                     value_Mass1.add('5')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_6:
                                     value_Mass1.add('6')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_7:
                                     value_Mass1.add('7')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_8:
                                     value_Mass1.add('8')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_9:
                                     value_Mass1.add('9')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_PERIOD:
                                     value_Mass1.add('.')
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_BACKSPACE:
                                     value_Mass1.sub()
                                     value_Mass1.display()
                                 elif sub_event.key == pygame.K_RETURN:
                                     Mass1_input = True
                                 screen.fill([209, 219, 189], rect=[350, 105 + 80, 400, 50])
                                 value_Mass1.display()

                                 pygame.display.flip()
                 if (350 <= posx <= 750) and (280 <= posy <= 330):
                     while not Velocity1_input:
                         for sub_event in pygame.event.get():
                             if sub_event.type == pygame.KEYDOWN:
                                 if sub_event.key == pygame.K_1:
                                     value_Velocity1.add('1')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_0:
                                     value_Velocity1.add('0')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_2:
                                     value_Velocity1.add('2')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_3:
                                     value_Velocity1.add('3')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_4:
                                     value_Velocity1.add('4')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_5:
                                     value_Velocity1.add('5')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_6:
                                     value_Velocity1.add('6')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_7:
                                     value_Velocity1.add('7')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_8:
                                     value_Velocity1.add('8')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_9:
                                     value_Velocity1.add('9')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_PERIOD:
                                     value_Velocity1.add('.')
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_BACKSPACE:
                                     value_Velocity1.sub()
                                     value_Velocity1.display()
                                 elif sub_event.key == pygame.K_RETURN:
                                     Velocity1_input= True
                                     screen.fill([209, 219, 189], rect=[350, 200 + 80, 400, 50])
                                 value_Velocity1.display()
                                 pygame.display.flip()
                 if (350 <= posx <= 750) and (375 <= posy <= 415):
                     while not Mass2_input:
                         for sub_event in pygame.event.get():
                             if sub_event.type == pygame.KEYDOWN:
                                 if sub_event.key == pygame.K_1:
                                     value_Mass2.add('1')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_0:
                                     value_Mass2.add('0')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_2:
                                     value_Mass2.add('2')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_3:
                                     value_Mass2.add('3')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_4:
                                     value_Mass2.add('4')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_5:
                                     value_Mass2.add('5')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_6:
                                     value_Mass2.add('6')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_7:
                                     value_Mass2.add('7')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_8:
                                     value_Mass2.add('8')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_9:
                                     value_Mass2.add('9')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_PERIOD:
                                     value_Mass2.add('.')
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_BACKSPACE:
                                     value_Mass2.sub()
                                     value_Mass2.display()
                                 elif sub_event.key == pygame.K_RETURN:
                                     Mass2_input = True
                                 screen.fill([209, 219, 189], rect=[350, 295 + 80, 400, 50])
                                 value_Mass2.display()
                                 pygame.display.flip()
                 if (350 <= posx <= 750) and (470 <= posy <= 520):
                     while not Velocity2_input:
                         for sub_event in pygame.event.get():
                             if sub_event.type == pygame.KEYDOWN:
                                 if sub_event.key == pygame.K_1:
                                     value_Velocity2.add('1')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_0:
                                     value_Velocity2.add('0')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_2:
                                     value_Velocity2.add('2')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_3:
                                     value_Velocity2.add('3')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_4:
                                     value_Velocity2.add('4')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_5:
                                     value_Velocity2.add('5')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_6:
                                     value_Velocity2.add('6')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_7:
                                     value_Velocity2.add('7')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_8:
                                     value_Velocity2.add('8')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_9:
                                     value_Velocity2.add('9')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_PERIOD:
                                     value_Velocity2.add('.')
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_BACKSPACE:
                                     value_Velocity2.sub()
                                     value_Velocity2.display()
                                 elif sub_event.key == pygame.K_RETURN:
                                     Velocity2_input= True
                                     screen.fill([209, 219, 189], rect=[350, 390 + 80, 400, 50])
                                 value_Velocity2.display()
                                 pygame.display.flip()

                 if (898 <= posx <= 989) and (575 <= posy <= 615):
                     running = False

         pygame.display.flip()
     mass1 = value_Mass1.value()
     mass2 = value_Mass2.value()
     velocity1 = value_Velocity1.value()
     velocity2 = value_Velocity2.value()
     print(mass1 * velocity1)

#input_screen_Collision(screen)

#input_screen_projectile(screen)