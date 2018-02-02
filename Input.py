import pygame
screen = pygame.display.set_mode((1366,768))

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


def input_screen_Collision(screen):
     pygame.init()
     pygame.display.set_caption('Collision')
     screen.fill([18, 47, 53])
     screen.fill([8, 120, 145], rect=[300, 50, 725, 618])
     Title_Mass1 = display_title("Mass of First Body:", [64, 59, 48], (350, 70 + 80), screen, 25)
     Title_Mass1.display()
     Title_Velocity1 = display_title("Velocity of First Body:", [64, 59, 48], (350, 160 + 80), screen, 25)
     Title_Velocity1.display()
     Title_Mass2= display_title("Mass of Second Body:", [64, 59, 48], (350, 260 + 80), screen, 25)
     Title_Mass2.display()
     Title_Velocity2 = display_title("Velocity of second Body:", [64, 59, 48], (350, 350 + 80), screen, 25)
     Title_Velocity2.display()
     title_collision_type11 = display_title("Elastic", [64, 59, 48], (845, 105+85), screen, 18)
     title_collision_type12 = display_title("Collision", [64, 59, 48], (845, 105+85+22), screen, 18)
     title_collision_type21 = display_title("Inelastic", [64, 59, 48], (845, 200+85), screen, 18)
     title_collision_type22 = display_title("Collision", [64, 59, 48], (845, 200+85+22), screen, 18)
     title_direction_type11 = display_title("Same Direction", [64, 59, 48], (820, 295+95), screen, 18)
     title_direction_type21 = display_title("Opposite", [64, 59, 48], (845, 390+85), screen, 18)
     title_direction_type22 = display_title("Direction", [64, 59, 48], (845, 390+85+22), screen, 18)
     Title_submit = display_title("Submit", [255, 255, 255], (911, 583), screen, 20)
     screen.fill([209, 219, 189], rect=[350, 105 + 80, 400, 50])
     screen.fill([209, 219, 189], rect=[350, 200 + 80, 400, 50])
     screen.fill([209, 219, 189], rect=[350, 295 + 80, 400, 50])
     screen.fill([209, 219, 189], rect=[350, 390 + 80, 400, 50])

     screen.fill([209, 219, 189], rect=[810, 105 + 80, 175, 50])
     screen.fill([209, 219, 189], rect=[810, 200 + 80, 175, 50])
     screen.fill([209, 219, 189], rect=[810, 295 + 80, 175, 50])
     screen.fill([209, 219, 189], rect=[810, 390 + 80, 175, 50])
     screen.fill([27, 22, 69], rect=[898, 575, 100, 40])
     title_collision_type11.display()
     title_collision_type12.display()
     title_collision_type21.display()
     title_collision_type22.display()
     title_direction_type11.display()
     title_direction_type21.display()
     title_direction_type22.display()
     Title_submit.display()
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
     direction = 2
     collision_type = 1
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
                 if (810 <= posx <= 985) and (185 <= posy <= 235):
                     collision_type = 1
                 if (810 <= posx <= 985) and (280 <= posy <= 330):
                     collision_type = 2
                 if (810 <=posx <= 985) and (375 <= posy <= 415):
                     direction = 1
                 if (810 <= posx <= 985) and (470 <= posy <= 520):
                     direction = 2
                 if (898 <= posx <= 989) and (575 <= posy <= 615):
                     running = False

         pygame.display.flip()
     mass1 = value_Mass1.value()
     mass2 = value_Mass2.value()
     velocity1 = value_Velocity1.value()
     velocity2 = value_Velocity2.value()
     print(mass1 * velocity1)
     return [mass1, mass2, velocity1, velocity2, direction, collision_type]


# input_screen_Collision(screen)
