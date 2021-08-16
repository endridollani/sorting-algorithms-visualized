import re
import pygame
import pygame_gui
from window import Window

class Gui(Window):

    def __init__(self):
        super().__init__() 
        self.manager = pygame_gui.UIManager(super().get_window_dimensions(), 'theme.json')
        self.win_dim = super().get_window_dimensions()
        self.side_space = round((self.win_dim[0] - 830)/2)

        self.shuffle_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.side_space, 25), (150, 50)),
            text='Shuffle',
            manager=self.manager)
        
        self.merge_sort_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.side_space+170, 25), (150, 50)),
            text='Merge Sort',manager=self.manager)

      
        self.quick_sort_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.side_space+340, 25), (150, 50)),
            text='Quick Sort',
            manager=self.manager)
        
        self.heap_sort_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.side_space+510, 25), (150, 50)),
            text='Heap Sort',manager=self.manager)

      
        self.bubble_sort_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.side_space+680, 25), (150, 50)),
            text='Bubble Sort',
            manager=self.manager)
        
        # self.sort_btn = pygame_gui.elements.UIButton(
        #     relative_rect=pygame.Rect((self.side_space+850, 25), (150, 50)),
        #     text='Sort',
        #     manager=self.manager)
    

    def get_shuffle_btn(self):
        return self.shuffle_btn
    def get_merge_sort_btn(self):
        return self.merge_sort_btn
    def get_quick_sort_btn(self):
        return self.quick_sort_btn
    def get_heap_sort_btn(self):
        return self.heap_sort_btn
    def get_bubble_sort_btn(self):
        return self.bubble_sort_btn
    # def get_sort_btn(self):
    #     return self.sort_btn

    def display(self,window): 
        self.manager.draw_ui(window)

    def get_manager(self): return self.manager

    def update_delta_time(self, delta_time):
        self.manager.update(delta_time)
