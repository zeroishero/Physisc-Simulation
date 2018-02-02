import pygame
import drawings as dr

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)
class image():
    def __init__(self,screen,setting):
        self.add_image = pygame.image.load('add.png')
        self.add_image = pygame.transform.scale(self.add_image, setting.img_size)
        self.add_rect = self.add_image.get_rect()
        self.subtract_image = pygame.image.load('subtract.png')
        self.subtract_image = pygame.transform.scale(self.subtract_image, setting.img_size)
        self.subtract_rect = self.subtract_image.get_rect()


        self.add_rect.center = setting.gr_add_pos
        screen.blit(self.add_image, self.add_rect)

        self.subtract_rect.center = setting.gr_subtract_pos
        screen.blit(self.subtract_image, self.subtract_rect)

        self.add_rect.center = setting.ln_add_pos
        screen.blit(self.add_image, self.add_rect)

        self.subtract_rect.center = setting.ln_subtract_pos
        screen.blit(self.subtract_image, self.subtract_rect)

        screen.blit(myfont.render("Settings", False, (255, 0, 0)), (setting.left+70, setting.top+5))
        screen.blit(myfont.render("Gravity", False, (255, 255, 255)), (setting.left + 70, setting.top + 35))
        screen.blit(myfont.render(str("%.1f" % round(setting.gravity,1)), False, (255, 0, 0)), (setting.left + 80, setting.top + 70))
        screen.blit(myfont.render("Wire Length", False, (255, 255, 255)), (setting.left + 60, setting.top + 125))
        screen.blit(myfont.render(str("%.1f" % round(setting.wire_length, 1)), False, (255, 0, 0)),(setting.left + 80, setting.top +160))

