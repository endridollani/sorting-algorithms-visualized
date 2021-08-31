import pygame
import random
from display import rectangles as rects
from window import Window
from pygame import time
from algorithms import bubble_sort as bs
from algorithms import merge_sort as ms

pygame.font.init()

class Algorithm(Window):
    def __init__(self,number_of_rectangles,delay_in_millisecondes):
        super().__init__()
        self.number_of_rectangles = number_of_rectangles
        self.window = super().get_window()
        self.rectangles = rects.Rectangles(self.number_of_rectangles)
        self.array_of_numbers = self.rectangles.get_array_of_numbers()
        self.delay_in_millisecondes = delay_in_millisecondes
        self.sort_state  = False
        self.index_of_algorithm_chosen = None
        self.bubble_sort = bs.BubbleSort(self.rectangles,delay_in_millisecondes)
        self.merge_sort = ms.MergeSort(self.rectangles,delay_in_millisecondes)
        self.shuffled = False
        # Font & Text
        self.font = pygame.font.SysFont('arial',15)
        self.algorithm_selected = self.font.render('No algorithm Selected!', True, (255, 255, 255), (0, 0, 0))
        self.algorithm_rect_number = self.font.render(f'Rectangles Drawn: {number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
        self.array_swaps = self.font.render(f'Swaps: None', True, (255, 255, 255), (0, 0, 0))
        self.writes = self.font.render(f'Array Writes: None', True, (255, 255, 255), (0, 0, 0))
        self.delay = self.font.render(f'Delay {self.delay_in_millisecondes} ms', True, (255, 255, 255), (0, 0, 0))

    def set_default_information(self):
        self.algorithm_selected = self.font.render('No algorithm Selected!', True, (255, 255, 255), (0, 0, 0))
        self.algorithm_rect_number = self.font.render(f'Rectangles Drawn: {self.number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
        # self.array_swaps = self.font.render(f'Swaps: None', True, (255, 255, 255), (0, 0, 0))
        # self.writes = self.font.render(f'Array Writes: None', True, (255, 255, 255), (0, 0, 0))
  
    def display_rectangles(self):
        # self.window.blit(self.algorithm_selected,(10,10))
        # self.window.blit(self.algorithm_rect_number,(10,30))
        # self.window.blit(self.array_swaps,(10,50))
        # self.window.blit(self.writes,(10,70))
        # self.window.blit(self.delay,(10,90))
        if self.index_of_algorithm_chosen == 0 and not self.shuffled:
            self.merge_sort.display_information()
        elif self.index_of_algorithm_chosen == 3 and not self.shuffled:
            self.merge_sort.display_information()
        self.rectangles.draw_rectangles(self.window)
    
    # def is_shuffled(self): return self.shuffled 
    def set_sort_information(self,algorithm,swaps,array_writes):
        self.algorithm_selected = self.font.render(f'{algorithm} finished!', True, (255, 255, 255), (0, 0, 0))
        self.algorithm_rect_number = self.font.render(f'Rectangles Drawn: {self.number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
        self.array_swaps = self.font.render(f'Swaps: {swaps}', True, (255, 255, 255), (0, 0, 0))
        self.writes = self.font.render(f'Array Writes: {array_writes}', True, (255, 255, 255), (0, 0, 0))

    def display_information(self):
        pass

    def is_choosen(self): return self.sort_state
    
    def set_sort_state_to(self,state): self.sort_state = state

    def set_index_of_algorithm_chosen(self,index):
      self.index_of_algorithm_chosen = index
      self.set_sort_state_to(True)

    def shuffle_array(self):
        self.sort_state = False
        random.shuffle(self.array_of_numbers)
        self.rectangles.set_color_to_default_value()
        self.set_default_information()
        self.shuffled = True
        self.merge_sort.array_accesses = 0
        self.merge_sort.comparisons = 0

    
    def visualize(self,window):
        
        if self.index_of_algorithm_chosen == 0:
            self.shuffled = False
            self.merge_sort.display(window,self.delay_in_millisecondes/1000)
            self.set_sort_state_to(False)
            # self.merge_sort.array_accesses = 0
            # self.merge_sort.comparisons = 0
            
            self.set_sort_state_to(False)
        elif self.index_of_algorithm_chosen == 1: self.set_sort_state_to(False) 
        elif self.index_of_algorithm_chosen == 2: self.set_sort_state_to(False) 
        elif self.index_of_algorithm_chosen == 3: 
            self.shuffled = False
            self.bubble_sort.display(window,self.delay_in_millisecondes/1000)
            swaps = self.bubble_sort.get_swaps_number()
            array_writes = self.bubble_sort.get_array_writes()
            self.set_sort_state_to(False)
            self.set_sort_information("Bubble Sort",swaps,array_writes)
            self.bubble_sort.set_swaps_number_to_zero()

