import pygame
import random
from display import rectangles as rects
from window import Window
from pygame import time
from algorithms import bubble_sort as bs

pygame.font.init()

class Algorithm(Window):
    def __init__(self,number_of_rectangles):
        super().__init__()
        self.number_of_rectangles = number_of_rectangles
        self.window = super().get_window()
        self.rectangles = rects.Rectangles(self.number_of_rectangles)
        self.array_of_numbers = self.rectangles.get_array_of_numbers()
        self.sort_state  = False
        self.index_of_algorithm_chosen = None
        
        # self.sort_algorithm = None
        # self.shuffled = True
        # Font & Text
        # self.font = pygame.font.SysFont('arial',15)
        # self.algorithm_selected = self.font.render('Algorithm Selected: None', True, (255, 255, 255), (0, 0, 0))
        # self.algorithm_rect_number = self.font.render(f'Rectangles Drawn: {number}', True, (255, 255, 255), (0, 0, 0))
        # self.algorithm_swaps = self.font.render(f'Swaps: None', True, (255, 255, 255), (0, 0, 0))
        # self.algorithm_writes = self.font.render(f'Array Writes: None', True, (255, 255, 255), (0, 0, 0))
  
    def display_shuffled_array(self):
        # self.draw_text(window)
        self.rectangles.draw_rectangles(self.window)
    
    # def is_shuffled(self): return self.shuffled 
    # # def draw_text(self,window):
    # #     window.blit(self.algorithm_selected,(10,10))
    # #     window.blit(self.algorithm_rect_number,(10,30))
    # #     window.blit(self.algorithm_swaps,(10,50))
    # #     window.blit(self.algorithm_writes,(10,70))
    def is_choosen(self): return self.sort_state
    
    def set_sort_state_to(self,state): self.sort_state = state

    def set_index_of_algorithm_chosen(self,index):
      self.index_of_algorithm_chosen = index
      self.set_sort_state_to(True)

    def shuffle_array(self):
        self.sort_state = False
        random.shuffle(self.array_of_numbers)
        self.rectangles.set_color_to_default_value()
        self.shuffled = True

    
    def visualize(self,window,delay):
        if self.index_of_algorithm_chosen == 0: self.set_sort_state_to(False)
        elif self.index_of_algorithm_chosen == 1: self.set_sort_state_to(False) 
        elif self.index_of_algorithm_chosen == 2: self.set_sort_state_to(False) 
        elif self.index_of_algorithm_chosen == 3: 
            self.bubble_sort = bs.BubbleSort(window, self.rectangles)
            self.bubble_sort.display(window,delay)
            self.set_sort_state_to(False)            