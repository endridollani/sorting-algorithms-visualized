import pygame

class Window:
   
    def __init__(self):
        self.window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.caption = pygame.display.set_caption("Visualized Sorting")
        self.background = pygame.Surface(self.get_window_dimensions())
        self.background.fill(pygame.Color('#000000')) 

    def get_window_dimensions(self): return (pygame.display.Info().current_w, pygame.display.Info().current_h)
    def get_win(self): return self.window
    def redraw(self, gui):
        self.window.blit(self.background, (0, 0))
        gui.display(self.window)
        
        pygame.display.flip()