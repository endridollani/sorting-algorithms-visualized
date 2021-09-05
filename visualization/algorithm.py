import pygame
import random
from display import rectangles as rects
from window import Window
from pygame import time
from algorithms import bubble_sort as bs
from algorithms import merge_sort as ms
from algorithms import quick_sort as qs
from algorithms import heap_sort as hs

pygame.font.init()
font = pygame.font.SysFont('arial',15)

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
        self.bubble_sort = bs.BubbleSort(self.rectangles,delay_in_millisecondes, super())
        self.merge_sort = ms.MergeSort(self.rectangles,delay_in_millisecondes,super())
        self.quick_sort = qs.QuickSort(self.rectangles,delay_in_millisecondes,super())
        self.heap_sort = hs.HeapSort(self.rectangles,delay_in_millisecondes,super())
        self.shuffled = False
        self.array_sorted = [False,-1]

    def display_information(self):
        number_of_rectangles_displayed = font.render(f'Rectangles Drawn: {self.number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
        delay = font.render(f'Delay {self.delay_in_millisecondes} ms', True, (255, 255, 255), (0, 0, 0))
        
        self.window.blit(number_of_rectangles_displayed,(10,10))
        self.window.blit(delay,(10,30))

    def display_rectangles(self):
        if self.index_of_algorithm_chosen == 0 and not self.shuffled and self.array_sorted[1] == 0:
            self.bubble_sort.display_information()
        elif self.index_of_algorithm_chosen == 3 and not self.shuffled and self.array_sorted[1] == 3:
            self.merge_sort.display_information()
        elif self.index_of_algorithm_chosen == 4 and not self.shuffled and self.array_sorted[1] == 4:
            self.quick_sort.display_information()
        elif self.index_of_algorithm_chosen == 5 and not self.shuffled and self.array_sorted[1] == 5:
            self.heap_sort.display_information()
        else:
            self.display_information()
        self.rectangles.draw_rectangles(self.window)
    

    def is_choosen(self): return self.sort_state
    
    def set_sort_state_to(self,state): self.sort_state = state

    def set_index_of_algorithm_chosen(self,index):
      self.index_of_algorithm_chosen = index
      self.set_sort_state_to(True)

    def shuffle_array(self):
        self.sort_state = False
        random.shuffle(self.array_of_numbers)
        self.shuffled = True
        
        self.array_sorted = [False,-1]
        
        self.bubble_sort.number_of_swaps,self.heap_sort.swaps = 0,0
        self.quick_sort.array_accesses,self.heap_sort.array_accesses,self.merge_sort.array_accesses = 0,0,0
        self.quick_sort.comparisons,self.merge_sort.comparisons = 0,0

    
    def visualize(self):
        if self.array_sorted[0]:
            self.display_rectangles()
        else:      
            if self.index_of_algorithm_chosen == 0:
                self.array_sorted = [True,0] 
                self.shuffled = False
                self.bubble_sort.display()
                self.set_sort_state_to(False)
            elif self.index_of_algorithm_chosen == 1:
                # self.array_sorted = [True,1] 
                # self.shuffled = False
                # self.selection_sort.display()
                self.set_sort_state_to(False)
            elif self.index_of_algorithm_chosen == 2:
                # self.array_sorted = [True,2] 
                # self.shuffled = False
                # self.insertion_sort.display()
                self.set_sort_state_to(False)
            elif self.index_of_algorithm_chosen == 3:
                self.array_sorted = [True,3]
                self.shuffled = False
                self.merge_sort.display()
                self.set_sort_state_to(False)
            elif self.index_of_algorithm_chosen == 4: 
                self.array_sorted = [True,4]
                self.shuffled = False
                self.quick_sort.display()
                self.set_sort_state_to(False) 
            elif self.index_of_algorithm_chosen == 5: 
                self.array_sorted = [True,5]
                self.shuffled = False
                self.heap_sort.display()
                self.set_sort_state_to(False)
            elif self.index_of_algorithm_chosen == 6:
                # self.array_sorted = [True,6] 
                # self.shuffled = False
                # self.tim_sort.display()
                self.set_sort_state_to(False)
            elif self.index_of_algorithm_chosen == 7:
                # self.array_sorted = [True,7] 
                # self.shuffled = False
                # self.intro_sort.display()
                self.set_sort_state_to(False)