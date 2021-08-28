import pygame
from display import button

class Window:
    def __init__(self):
        self.width ,self.height = 1300,700
        self.window = pygame.display.set_mode((self.width,self.height), pygame.SCALED)
        self.caption = pygame.display.set_caption("Visualized Sorting")
        self.background = pygame.Surface((self.width,self.height))
        self.background.fill(pygame.Color('#000000'))
        self.button = button.Button(self.window,self.width,self.height) 
    
    def set_dimensions(self,width,height):
        self.width,self.height = dimensions

    def set_bg(self):
        self.window.blit(self.background, (0, 0))
        
    def update_manager(self, delta_time):
        self.button.update_delta_time(delta_time)

    def display_buttons(self):
        self.button.display()

    def get_button(self): return self.button

    def get_window(self): return self.window