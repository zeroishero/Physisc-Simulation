import pygame
import sys

screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)

class display_title:
    def __init__(self,message,colour,location,screen,size):
        self.font = pygame.font.SysFont('courier',size,bold= True,italic= False)
        self.screen_text = self.font.render(message,True,colour)
        self.location = location
        self.screen_text_hover = self.font.render(message,True,[207,71,71])
        self.screen = screen

    def display(self):
        self.screen.blit(self.screen_text,self.location)
    def display_hover(self):
        self.screen.blit(self.screen_text_hover,self.location)


def boxes():
    screen.fill([42,49,50])
    screen.fill([47,52,64],rect = [100,50,1166,668])

def main():
    pygame.init()

    projectile = pygame.image.load('Picture/Projectile.png')
    wave = pygame.image.load('Picture/Wave.png')
    pendulum = pygame.image.load('Picture/SHM.png')
    collision = pygame.image.load('Picture/Collision.png')
    projection = pygame.image.load('Picture/Circular.png')
    title = display_title('PHYSICS SIMULATOR', [0, 255, 255], (366, 60), screen, 54)

    topic1 = display_title('1. Supepostion of Wave', [255, 255, 0], (120, 140), screen, 35)

    topic2 = display_title('2. Simple Pendulum', [255, 255, 0], (120, 185), screen, 35)

    topic3 = display_title('3. Projectile Motion', [255, 255, 0], (120, 230), screen, 35)

    topic4 = display_title('4. Collision', [255, 255, 0], (120, 275), screen, 35)

    topic5 = display_title('5. Projection of Particle', [255, 255, 0], (120, 320), screen, 35)

    topic6 = display_title('   in Circular Motion', [255, 255, 0], (120, 365), screen, 35)

    boxes()
    pygame.display.flip()

    while True:
        #screen.fill([47, 52, 64], rect=[705, 145, 460, 410])
        boxes()
        topic6.display()
        topic5.display()
        topic4.display()
        topic3.display()
        topic2.display()
        topic1.display()
        title.display()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:
                posx,posy = pygame.mouse.get_pos()
                while (110<=posx<=680) and (140<=posy<=175):
                    screen.fill([91, 96, 95], rect=[705, 145, 460, 410])
                    screen.blit(wave,(710,150))
                    pygame.display.update()
                    posx, posy = pygame.mouse.get_pos()
                    for sub_event in pygame.event.get():
                     if sub_event.type == pygame.MOUSEBUTTONDOWN:
                         import wave
                         wave.run_wave()
                while (110 <= posx <= 680) and (185 <= posy <= 225):
                    screen.fill([91, 96, 95], rect=[705, 145, 460, 410])
                    screen.blit(pendulum, (710, 150))
                    pygame.display.update()
                    posx, posy = pygame.mouse.get_pos()
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.MOUSEBUTTONDOWN:
                            import main
                            main.program()
                while (110 <= posx <= 680) and (230 <= posy <= 270):
                    screen.fill([91, 96, 95], rect=[705, 145, 460, 410])
                    screen.blit(projectile, (710, 150))
                    pygame.display.update()
                    posx, posy = pygame.mouse.get_pos()
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.MOUSEBUTTONDOWN:
                            import Projectile
                            Projectile.mainPro()
                while (110 <= posx <= 680) and (275 <= posy <= 315):
                    screen.fill([91, 96, 95], rect=[705, 145, 460, 410])
                    screen.blit(collision, (710, 150))
                    pygame.display.update()
                    posx, posy = pygame.mouse.get_pos()
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.MOUSEBUTTONDOWN:
                            import ElasticCollision
                            ElasticCollision.main_program()
                while (110 <= posx <= 680) and (320 <= posy <= 360):
                    screen.fill([91, 96, 95], rect=[705, 145, 460, 410])
                    screen.blit(projection, (710, 150))
                    pygame.display.update()
                    posx, posy = pygame.mouse.get_pos()
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.MOUSEBUTTONDOWN:
                            import SHM
                            SHM.run_shm()



main()