import pygame

class EventHandler:
    def __init__(self):
        pass
    
    def handle_event(self, type_of_event):
        if type_of_event == pygame.QUIT:
            quit()
        