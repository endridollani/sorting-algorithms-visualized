import pygame
import pygame_gui
from buttons import button

class Window:
    def __init__(self,width,height):
        self.window = pygame.display.set_mode((width,height), pygame.SCALED)
        self.caption = pygame.display.set_caption("Visualized Sorting")
        self.background = pygame.Surface((width,height))
        
        #Set background color to black
        self.background.fill(pygame.Color('#000000'))
        
        #Set manager to operate in the given dimensions with the given theme
        self.manager = pygame_gui.UIManager((width,height), 'visualization/buttons/theme.json')
        
        #Initializes buttons
        button.init_buttons(self.manager)
    
    #Sets window background to black
    def set_background(self):
        self.window.blit(self.background, (0, 0))

    #Updates pygame_gui manager    
    def update_gui_manager(self, delta_time):
        self.manager.update(delta_time)

    #Displays buttons to the screen
    def display_buttons(self):
        self.manager.draw_ui(self.window)

    #Returns window
    def get_window(self): return self.window

    def get_manager(self): return self.manager