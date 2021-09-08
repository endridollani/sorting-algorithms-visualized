import pygame
import random
from algorithms import rectangles
from algorithms import bubble_sort
from algorithms import quick_sort
from algorithms import heap_sort

class Draw(rectangles.Rectangles):
    def __init__(self,window,number_of_rectangles,delay_in_millisecondes):
        super().__init__(window, number_of_rectangles, delay_in_millisecondes)
        
        self.window = window
        self.number_of_rectangles = number_of_rectangles
        self.delay_in_millisecondes = delay_in_millisecondes

        self.bs = bubble_sort.BubbleSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)
        self.qs = quick_sort.QuickSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)
        self.hs = heap_sort.HeapSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)

        self.is_required_for_sorting  = False
        self.sort_index = -1
        self.shuffled = False
        self.array_sorted = False

    def index_of_algorithm_chosen(self, index):
        self.sort_index = index
        self.is_required_for_sorting = True

    def shuffle_array(self):
        self.sort_state = False
        self.sort_index = -1
        random.shuffle(super().get_array_of_numbers())
        self.shuffled = True
        self.is_required_for_sorting = False
        self.array_sorted = False
        
        self.bs.set_defaults()
        self.qs.set_defaults()
        self.hs.set_defaults()
        
    def sort_visualization(self):
        if self.sort_index == 0 and not self.array_sorted:
            self.bs.sort()
            super().set_array_of_numbers(self.bs.get_array_of_numbers())
        elif self.sort_index == 4 and not self.array_sorted:
            self.qs.sort()
            super().set_array_of_numbers(self.qs.get_array_of_numbers())
        elif self.sort_index == 5 and not self.array_sorted:
            self.hs.sort()
            super().set_array_of_numbers(self.hs.get_array_of_numbers())

        super().draw()
        self.is_required_for_sorting = False
        self.shuffled = False
        self.array_sorted = True
    
    def rectangle_bar_chart(self):
        if self.sort_index == 0:
            self.bs.information()
        elif self.sort_index == 4:
            self.qs.information()
        elif self.sort_index == 5:
            self.hs.information()
        super().draw()