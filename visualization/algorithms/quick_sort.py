from algorithms.rectangles import Rectangles
import pygame
from pygame import font
import time

font.init()
font = pygame.font.SysFont('arial', 15)

class QuickSort(Rectangles):
    def __init__(self, window, number_of_rectangles, delay):
        super().__init__(window, number_of_rectangles, delay)
        self.window = window
        self.delay = delay
        self.number_of_rectangles = number_of_rectangles
        self.comparisons = 0
        self.array_accesses = 0
   
    def sort(self):
        self.quick_sort(0, self.number_of_rectangles - 1, super().get_array_of_numbers())
        super().draw() 
        super().draw_finishline()

    # The main function that implements QuickSort
    def quick_sort(self, start, end, array):
        if(start < end):

            # p is partitioning index, array[p]
            # is at right place
            p = self.partition(start, end, array)

            # Sort elements before partition
            # and after partition
            self.quick_sort(start, p - 1, array)
            self.quick_sort(p + 1, end, array)
    
    #This Function handles sorting part of quick sort
    # start and end points to first and last element of
    # an array respectively

    def partition(self, start, end, array):

        # Initializing pivot's index to start
        pivot_index = start
        pivot = array[pivot_index]
        self.array_accesses += 1
        # This loop runs till start pointer crosses
        # end pointer, and when it does we swap the
        # pivot with element on end pointer
        while start < end:

            # Increment the start pointer till it finds an
            # element greater than  pivot
            while start < len(array) and array[start] <= pivot:
                self.comparisons += 2
                self.array_accesses += 1
                start += 1
                time.sleep(self.delay)
                self.draw(start, end, pivot)

            # Decrement the end pointer till it finds an
            # element less than pivot
            while array[end] > pivot:
                self.comparisons += 1
                self.array_accesses += 1
                end -= 1
                time.sleep(self.delay)
                self.draw(start, end, pivot)

            # If start and end have not crossed each other,
            # swap the numbers on start and end
            if(start < end):
                self.comparisons += 1
                array[start], array[end] = array[end], array[start]
                time.sleep(self.delay)
                self.draw(start, end, pivot)

        # Swap pivot element with element on end pointer.
        # This puts pivot on its correct sorted place.
        array[end], array[pivot_index] = array[pivot_index], array[end]
        self.array_accesses += 2
        time.sleep(self.delay)
        self.draw(start, end, pivot_index)

        # Returning end pointer to divide the array into 2
        return end
    
    def set_defaults(self):
        self.comparisons = 0
        self.array_accesses = 0
   
    def get_array_of_numbers(self):
        return super().get_array_of_numbers()
    
    def draw(self,start,end,pivot_index):
        self.window.set_background()
        
        self.information()
        
        for i in self.array_of_numbers:
            val = i
            pos = super().get_array_of_numbers().index(val)
            rectangle = super().get_rectangle_at(pos,val)
            
            if pos == start or pos == end:
                pygame.draw.rect(self.window.get_display(),(255, 0, 0), rectangle)
            elif pos == pivot_index:
                pygame.draw.rect(self.window.get_display(),(0,255,255), rectangle)
            else:
                pygame.draw.rect(self.window.get_display(),(255,255,255), rectangle)

        pygame.display.flip()
    
    def information(self):
        algorithm = font.render(
            "Quick Sort", True, (255, 255, 255), (0, 0, 0))
        rectangles_drawn = font.render(
            f'Rectangles: {len(super().get_array_of_numbers())}', True, (255, 255, 255), (0, 0, 0))
        swaps = font.render(
            f'Comparisons: {self.comparisons}', True, (255, 255, 255), (0, 0, 0))
        array_accesses = font.render(
            f'Array Accesses: {self.array_accesses}', True, (255, 255, 255), (0, 0, 0))
        delays = font.render(
            f'Delay {self.delay * 1000} ms', True, (255, 255, 255), (0, 0, 0))

        self.window.get_display().blit(algorithm, (10, 10))
        self.window.get_display().blit(rectangles_drawn, (10, 30))
        self.window.get_display().blit(swaps, (10, 50))
        self.window.get_display().blit(array_accesses, (10, 70))
        self.window.get_display().blit(delays, (10, 90))