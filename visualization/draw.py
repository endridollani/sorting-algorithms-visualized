import pygame
import random
from algorithms import rectangles
from algorithms import bubble_sort
from algorithms import quick_sort
from algorithms import heap_sort
from algorithms import merge_sort
from algorithms import selection_sort
from algorithms import insertion_sort
from algorithms import timsort

class Draw(rectangles.Rectangles):
    def __init__(self,window,number_of_rectangles,delay_in_millisecondes):
        super().__init__(window, number_of_rectangles, delay_in_millisecondes)
        
        self.window = window
        self.number_of_rectangles = number_of_rectangles
        self.delay_in_millisecondes = delay_in_millisecondes

        self.bs = bubble_sort.BubbleSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)
        self.qs = quick_sort.QuickSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)
        self.hs = heap_sort.HeapSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)
        self.ms = merge_sort.MergeSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)
        self.ss = selection_sort.SelectionSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)
        self.ins = insertion_sort.InsertionSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)
        self.tim = timsort.TimSort(self.window,self.number_of_rectangles,self.delay_in_millisecondes)

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
        self.ms.set_defaults()
        self.ss.set_defaults()
        self.ins.set_defaults()
        self.tim.set_defaults()
        
    def sort_visualization(self):
        if self.sort_index == 0 and not self.array_sorted:
            self.bs.sort()
            super().set_array_of_numbers(self.bs.get_array_of_numbers())
        elif self.sort_index == 1 and not self.array_sorted:
            self.ss.sort()
            super().set_array_of_numbers(self.ss.get_array_of_numbers())
        elif self.sort_index == 2 and not self.array_sorted:
            self.ins.sort()
            super().set_array_of_numbers(self.ins.get_array_of_numbers())
        elif self.sort_index == 3 and not self.array_sorted:
            self.ms.sort()
            super().set_array_of_numbers(self.ms.get_array_of_numbers())
        elif self.sort_index == 4 and not self.array_sorted:
            self.qs.sort()
            super().set_array_of_numbers(self.qs.get_array_of_numbers())
        elif self.sort_index == 5 and not self.array_sorted:
            self.hs.sort()
            super().set_array_of_numbers(self.hs.get_array_of_numbers())
        elif self.sort_index == 6 and not self.array_sorted:
            self.tim.sort()
            super().set_array_of_numbers(self.tim.get_array_of_numbers())

        super().draw()
        self.is_required_for_sorting = False
        self.shuffled = False
        self.array_sorted = True
    
    def rectangle_bar_chart(self):
        if self.sort_index == 0:
            self.bs.information()
        elif self.sort_index == 1:
            self.ss.information()
        elif self.sort_index == 2:
            self.ins.information()
        elif self.sort_index == 3:
            self.ms.information()
        elif self.sort_index == 4:
            self.qs.information()
        elif self.sort_index == 5:
            self.hs.information()
        elif self.sort_index == 6:
            self.tim.information()
        super().draw()