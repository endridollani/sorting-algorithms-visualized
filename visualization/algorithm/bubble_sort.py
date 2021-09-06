import pygame
from pygame import font
import time

def draw(self,array_of_numbers):
    array_size = len(array_of_numbers)
    iterations = len(array_of_numbers) - 1

    for i in range(array_size):
        self.draw_rectangles()
        
        for j in range(iterations):
            
            if self.array_of_numbers[j] > self.array_of_numbers[j+1]:
                swap(j)
                draw_rectangles()
        
        array_size -= 1
        iterations -= 1

def display(self):
    self.bubble_sort()
    self.swap_index = -1
    self.rectangles.draw_rectangles(self.window.get_window())
    self.rectangles.sort_finished(self.window.get_window(), 0.01)

def swap(self, index):
    self.number_of_swaps += 1
    self.swap_index = index
    self.array_of_numbers[index], self.array_of_numbers[index +
                                                        1] = self.array_of_numbers[index+1], self.array_of_numbers[index]