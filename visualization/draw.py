import pygame
import random
import rectangles as rects
from pygame import time

from algorithms import sort

pygame.font.init()
font = pygame.font.SysFont('arial',15)


class Draw():
    def __init__(self,window,number_of_rectangles,delay_in_millisecondes):
        self.number_of_rectangles = number_of_rectangles
        self.window = window.get_window()
        self.win = window
        self.rectangles = rects.Rectangles(self.number_of_rectangles)
        self.array_of_numbers = self.rectangles.get_array_of_numbers()
        self.delay_in_millisecondes = delay_in_millisecondes / 1000
        self.sort_state  = False
        self.sort_index = -1
        self.shuffled = False
        self.array_sorted = [False,-1]

    # def display_information(self):
    #     number_of_rectangles_displayed = font.render(f'Rectangles Drawn: {self.number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
    #     delay = font.render(f'Delay {self.delay_in_millisecondes} ms', True, (255, 255, 255), (0, 0, 0))
        
    #     self.window.blit(number_of_rectangles_displayed,(10,10))
    #     self.window.blit(delay,(10,30))

    def rectangle_bar_chart(self):
        # if self.sort_index == 0 and not self.shuffled and self.array_sorted[1] == 0:
        #     self.bubble_sort.display_information()
        # elif self.sort_index == 3 and not self.shuffled and self.array_sorted[1] == 3:
        #     self.merge_sort.display_information()
        # elif self.sort_index == 4 and not self.shuffled and self.array_sorted[1] == 4:
        #     self.quick_sort.display_information()
        # elif self.sort_index == 5 and not self.shuffled and self.array_sorted[1] == 5:
        #     self.heap_sort.display_information()
        # else:
        #     self.display_information()
        self.rectangles.draw_rectangles(self.window)
    

    def is_choosen(self): return self.sort_state
    
    def set_sort_state_to(self,bool): self.sort_state = bool

    def set_index_of_algorithm_chosen(self,index):
      self.sort_index = index
      self.set_sort_state_to(True)

    def shuffle_array(self):
        self.sort_state = False
        random.shuffle(self.array_of_numbers)
        self.shuffled = True
        
        self.array_sorted = [False,-1]
        
        # self.bubble_sort.number_of_swaps,self.heap_sort.swaps = 0,0
        # self.quick_sort.array_accesses,self.heap_sort.array_accesses,self.merge_sort.array_accesses = 0,0,0
        # self.quick_sort.comparisons,self.merge_sort.comparisons = 0,0

    
    def rectangle_visualization(self):
        self.array_sorted[0] = True
        self.array_sorted[1] = self.sort_index
        self.shuffled = False
        sort.display(self.sort_index,self.win,self.rectangles,self.delay_in_millisecondes)
        self.set_sort_state_to(False)
