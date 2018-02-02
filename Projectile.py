#impoting libraries
import math
import pygame
import sys
import InputScreen

def input_types():#for choosing types of projecctile motion.
    #pygame.init()
    #screen.fill([247,247,247])
    #border(screen)
    #Title_Types = display_title("Choose Types of Projectile Motion",[20,225,245],(450,35),screen,25)
    #Title_Types.display()
    #pygame.display.flip()
    print("The types of projectile :")
    print("1. Horizontal")
    print("2. Vertical")
    print("3. Combined")

    return int(input("Enter your choice"))

def variables(x):#Function for inputing variables
    if x == 1:
        Velocity = float(input("Enter a velocity"))
        Angle = float(input("Enter a angle"))
        Height = 0
    elif x == 2:
        Velocity = float(input("Enter a velocity"))
        Angle = 0
        Height = float(input("Enter a height"))
    elif x == 3:
        Velocity = float(input("Enter a velocity"))
        Angle = float(input("Enter a angle"))
        Height = float(input("Enter a height"))
    else:
        print("You have entered wrong option")
        x = input("Press any key to continue ")
        return 0;
    return (Velocity,Angle,Height)

def combined(v0,Ang,h,dt,k):
    cosA = math.cos(math.radians(Ang))
    sinA = math.sin(math.radians(Ang))
    x = v0 * dt * cosA
    y = v0 * dt * sinA - (1 / 2) * 9.8 * dt * dt + h
    return plot(k*x,k*y)

#function for calculation of values:
def calc_projectile(dict_time,position,Values):
    u , ang, h = Values
    cosA = math.cos(math.radians(ang))
    sinA = math.sin(math.radians(ang))
    dt = dict_time[position]
    Vx = u * cosA
    Vy = u * sinA - 9.8 * dt
    V = math.sqrt(math.pow(Vx, 2) + math.pow(Vy, 2))
    Dx =  u * cosA * dt
    Dy = u * sinA *dt - (1/2) * 9.8 * dt * dt
    D = math.sqrt(math.pow(Dx,2)+math.pow(Dy,2))
    return [V,D]

#function for calculation of standard values
def calc_standardValues(u,Ang,h):
    cosA = math.cos(math.radians(Ang))
    sinA = math.sin(math.radians(Ang))
    max_height = u * u * sinA *sinA /(2 * 9.8) + h
    total_time = (u*sinA + math.sqrt(u*u*sinA*sinA + 2*9.8*h))/9.8
    Range = u * cosA * total_time
    return [Range , max_height, total_time]

class display_test:
    def __init__(self,message,colour,location,screen):
        self.font =  pygame.font.SysFont('courier',16, bold=True,italic=True)
        self.screen_text = self.font.render(message, True, colour)
        self.location = location
        self.screen = screen
    def display(self):
        self.screen.blit(self.screen_text,self.location)

class display_Values:
    def __init__(self,message,colour,location,screen):
        self.font =  pygame.font.SysFont('courier',16,bold=False,italic=True)
        self.screen_text = self.font.render(message, True, colour)
        self.screen_erase = self.font.render(message,True,[0,0,0])
        self.location = location
        self.screen = screen
    def display(self):
        self.screen.blit(self.screen_text,self.location)
    def display_erase(self):
        self.screen.blit(self.screen_erase,self.location)

# Function for calculation instant velocity and displacement
def instant_velocity_displacement(dt,values):
    u, ang, h = values
    cosA = math.cos(math.radians(ang))
    sinA = math.sin(math.radians(ang))
    Vx = u * cosA
    Vy = u * sinA - 9.8 * dt
    V = math.sqrt(math.pow(Vx, 2) + math.pow(Vy, 2))
    Dx = u * cosA * dt
    Dy = u * sinA * dt - (1 / 2) * 9.8 * dt * dt
    D = math.sqrt(math.pow(Dx, 2) + math.pow(Dy, 2))
    return [V , D]

#Function that convert right hand co-ordinate to left hand
def plot(x,y):
   return [60 + x, 733 - y,y]

#Function for drawing borderline
def border(screen):
    pygame.draw.line(screen,[0,0,0],(10,10),(10,758),4)
    pygame.draw.line(screen, [0,0,0], (10, 10), (1356,10), 4)
    pygame.draw.line(screen, [0,0,0], (10, 758), (1356, 758), 4)
    pygame.draw.line(screen, [0,0,0], (1356, 10), (1356, 758), 4)

#function that returns integer value of plot
def int_plot(x,y):
    return(int(x),int(y))

#Function for axes
def axes(screen):
    pygame.draw.line(screen,[0,0,0], (58,35), (58,733),2)
    pygame.draw.line(screen, [0, 0, 0], (58, 733),(1306, 733),2)

#function for displaying the image
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

#function for scaling
def Scaling(standard):
    Range,height,Time = standard
    scale = [0.5,1,2]
    k = 1
    if (k * Range) > 1200 or (k * height) > 690:
        k = scale[0]
    if (k * Range <=400 ) and (k * height) <= 250:
        k = scale[2]
    return k


#MainPragram
def mainPro():
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption('Projectile Motion')
    Values = [Velocity, Angle, Height] = InputScreen.input_screen_projectile(screen)
    dt = 0
    # enter = input_types()
    # Velocity,Angle,Height = variables(enter)#inputScreen.input_screen(screen)
    running = True
    standard_values = calc_standardValues(Velocity,Angle,Height)
    screen.fill([247,247,247])
    border(screen)
    pygame.display.flip()
    circle = pygame.image.load('Picture\Circle.png')#Use for Indicating current position
    circle2 = pygame.image.load('Picture\Circle2.png')#Use For Erasing the before position #circle3 = pygame.image.load('Picture\Circle3.png')
    points =[] #to store points
    int_points = [] #integer value of points
    dic_time = {} #dictionary that contains time period cooresponding to the location in terms of x-cordinate
    textInstant_Velocity = display_test('Instant Velocity = ', [0, 255, 0], (1000, 30), screen)
    textInstant_Displacement = display_test('Displacement = ',[0,255,0],(1000,45),screen)
    textInstant_time = display_test('Time period = ',[0,255,0],(1000,60),screen)
    textInstant_Velocity.display()
    textInstant_Displacement.display()
    textInstant_time.display()
    pygame.display.flip()
    k = Scaling(standard_values)

    while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        pause_program()
            x,y,check = combined(Velocity,Angle,Height,dt,k)
            if check <= 0 and x != 60:
                running = False
            points.append((x,y))
            int_points.append(int_plot(x,y))
            n = len(int_points)
            if n > 2 and int_points[n-2] == int_points[n-1]:
                del int_points[n-1]
                dic_time.update({int_points[n-2]:dt})
            else:
                dic_time.update({int_points[n-2]:dt})
            dt =dt + 0.005
            if y <= 733:
                screen.blit(circle,(x,y))
                axes(screen)
                temp_values = instant_velocity_displacement(dt,Values)
                formatted_instant = "{instant:0.3f}".format(instant = temp_values[0])
                ValuesInstan = display_Values(formatted_instant,[0,0,255],(1200,30),screen)
                ValuesInstan.display()
                formatted_instant = "{instant:0.3f}".format(instant=temp_values[1])
                ValuesInstan1 = display_Values(formatted_instant, [0, 0, 255], (1200, 45), screen)
                ValuesInstan1.display()
                formatted_instant = "{instant:0.3f}".format(instant=dt)
                ValuesInstan2 = display_Values(formatted_instant, [0, 0, 255], (1200, 60), screen)
                ValuesInstan2.display()
                pygame.display.update()
                screen.blit(circle2, (x,y))
                screen.fill([247,247,247],rect = [1200,30,100,100])
                pygame.draw.aaline(screen,[255,0,0],(x,y),(x,y),0)
    inform(points,int_points,screen,dic_time,Values,standard_values)


def inform(points,int_points,screen,dict,Values,standard_values):  # function for displaying information
    showing = True
    pygame.init()
    pygame.display.flip()
    screen.fill([247, 247, 247])
    axes(screen)
    border(screen)
    Range , Max_Height, Time = standard_values
    textInstant_velocity_remarks = display_test('Instant Velocity = ', [0, 255, 0], (1050, 30), screen)
    textInstant_velocity_remarks.display()
    textInstant_Displacement_remarks = display_test('Displacement = ', [0, 255, 0], (1050, 45), screen)
    textInstant_Displacement_remarks.display()
    textInstant_Time_remarks = display_test('Instant time =',[0,255,0],(1050,60),screen)
    textInstant_Time_remarks.display()
    textRange_remarks = display_test('Total Range =',[0,255,0],(1050,75),screen)
    textMaxHeight_remarks = display_test('Maximum Height =',[0,255,0],(1050,90),screen)
    textTime_remarks = display_test('Total Time =',[0,255,0],(1050,105),screen)
    textRange_remarks.display()
    textMaxHeight_remarks.display()
    textTime_remarks.display()
    formatted_Range = "{Temp_range:0.3f}".format(Temp_range=Range)
    formatted_MaxHeight = "{Temp_height:0.3f}".format(Temp_height = Max_Height)
    formatted_Time = "{Temp_time:0.3f}".format(Temp_time=Time)
    value_Range = display_Values(formatted_Range,[0,0,255],(1230,75),screen)
    value_Height = display_Values(formatted_MaxHeight,[0,0,255],(1230,90),screen)
    value_time = display_Values(formatted_Time,[0,0,255],(1230,105),screen)
    value_Range.display()
    value_Height.display()
    value_time.display()
    if Values[0] == 0:
        points2,int_points2,dict_time = alternative_projectile(Values)
        del int_points2[-1]
    del int_points[-1]
    x = 0
    while x < (len(points) - 1):
        pygame.draw.aaline(screen, [255, 0, 0], points[x], points[x + 1])
        x = x + 1
    while showing:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    showing = False
            posx,posy = pygame.mouse.get_pos()
            while int_points.count((posx,posy)) == 1:
               Position = (posx,posy)
               Vel , Dis = calc_projectile(dict,Position,Values)
               formatted_vel = "{VelC:0.3f}".format(VelC = Vel)
               textInstant_velocity = display_Values(formatted_vel,[0,0,255],(1230,30),screen)
               textInstant_velocity.display()
               formatted_dis = "{Disc:0.3f}".format(Disc=Dis)
               textInstant_displacement = display_Values(formatted_dis,[0,0,255],(1230,45),screen)
               textInstant_displacement.display()
               dt = dict[Position]
               formatted_time = "{time:0.3f}".format(time=dt)
               textInstant_time = display_Values(formatted_time,[0,0,255],(1230,60),screen)
               textInstant_time.display()
               pygame.display.update()
               for subevent in pygame.event.get():
                   posx,posy = pygame.mouse.get_pos()
                   screen.fill([247, 247, 247], rect=[1230, 30, 100, 45])



def alternative_projectile(Values):
    Velocity = Values[0]
    Angle = 90 - Values[1]
    Height = Values[2]
    dt = 0
    calculating = True
    points = []
    int_points = []
    dic_time = {}
    while calculating:
        x,y,check = combined(Velocity,Angle,Height,dt)
        dt = dt + 0.0001
        if check <= 0 and x != 60:
            calculating = False
        points.append((x, y))
        int_points.append(int_plot(x, y))
        n = len(int_points)
        if n > 2 and int_points[n - 2] == int_points[n - 1]:
            del int_points[n - 1]
            dic_time.update({int_points[n - 2]: dt})
        else:
            dic_time.update({int_points[n - 2]: dt})
    return [points,int_points,dic_time]


#mainPro()



