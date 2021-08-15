import pygame
import pygame_gui
from window import Window

class Gui(Window):

    def __init__(self):
        super().__init__() 
        self.manager = pygame_gui.UIManager(super().get_window_dimensions(), 'theme.json')
       
        self.shuffle_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 25), (200, 50)),
                                             text='Shuffle',
                                             manager=self.manager)
        self.array_size_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 25), (200, 50)),
                                             text='Array Size',
                                             manager=self.manager)
        self.algorithm_picker_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 25), (200, 50)),
                                             text='Pick an Algorithm',
                                             manager=self.manager)
        self.sort_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((850, 25), (200, 50)),
                                             text='Sort',
                                             manager=self.manager)

   
    def get_shuffle_btn(self):
        return self.shuffle_btn
    def get_array_size_btn(self):
        return self.array_size_btn
    def get_algorithm_picker_btn(self):
        return self.algorithm_picker_btn
    def get_sort_btn(self):
        return self.sort_btn

    def display(self,window): 
        self.manager.draw_ui(window)

    def get_manager(self): return self.manager

    def update_delta_time(self, delta_time):
        self.manager.update(delta_time)