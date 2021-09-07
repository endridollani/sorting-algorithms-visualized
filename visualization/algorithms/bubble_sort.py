import pygame
from pygame import font
import time




def sort(array_of_numbers):
    array_size = len(array_of_numbers)
    iterations = len(array_of_numbers) - 1

    for i in range(array_size):
        draw_rectangles()
        
        for j in range(iterations):
            
            if array_of_numbers[j] > array_of_numbers[j+1]:
                swap(j)
                draw_rectangles()
        
        array_size -= 1
        iterations -= 1

def display(window, rectangles):
    sort(rectangles.get_array_of_numbers())
    swap_index = -1
    rectangles.draw_rectangles(window.get_window())
    rectangles.sort_finished(window.get_window(), 0.01)

def swap( index):
    number_of_swaps += 1
    swap_index = index
    array_of_numbers[index], array_of_numbers[index +
                                                        1] = array_of_numbers[index+1], array_of_numbers[index]

def draw_rectangles(self,l,r,m,li,ri):
        self.window.set_bg()
        self.rectangles.draw_merge_sort(self.window,l,r,m,li,ri)
        display_sort_algorithm_information(self.window.get_window(),"Merge Sort",self.comparisons,self.array_accesses,self.rectangles.number_of_rectangles,self.delay)
        pygame.display.flip()
