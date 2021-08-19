import pygame

class Window:
   
    def __init__(self):
        self.window = pygame.display.set_mode((1300,700), pygame.SCALED)
        self.caption = pygame.display.set_caption("Visualized Sorting")
        self.background = pygame.Surface(self.get_window_dimensions())
        self.background.fill(pygame.Color('#000000')) 

    def get_window_dimensions(self): return (pygame.display.Info().current_w, pygame.display.Info().current_h)
    def get_win(self): return self.window
    def set_bg(self):
        self.window.blit(self.background, (0, 0))
        