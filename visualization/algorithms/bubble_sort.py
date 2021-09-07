from algorithms.rectangles import Rectangles
import pygame
from pygame import font
import time


font.init()
pygame.init()
font = pygame.font.SysFont('arial', 15)

class BubbleSort(Rectangles):
    def __init__(self, window, number_of_rectangles, delay):
        super().__init__(window, number_of_rectangles, delay)
        self.window = window
        self.delay = delay
        self.swap_index = -1
        self.swaps = 0
        self.array_accesses = 0

    def sort(self):
        array_size = len(super().get_array_of_numbers())
        iterations = len(super().get_array_of_numbers()) - 1

        for i in range(array_size):
            self.draw()
            
            for j in range(iterations):
                
                if super().get_array_of_numbers()[j] > super().get_array_of_numbers()[j+1]:
                    time.sleep(self.delay)
                    self.swap(j)
                    self.draw()
            
            array_size -= 1
            iterations -= 1
        
        self.swap_index = -1
        super().draw()
        super().draw_finishline()
        
    def draw(self):
        self.window.set_background()
        
        self.information()
        
        for i in super().get_array_of_numbers():
            val = i
            pos = super().get_array_of_numbers().index(val)
            rectangle = super().get_rectangle_at(pos,val)
            

            if pos == self.swap_index or pos == self.swap_index+1:
                pygame.draw.rect(self.window.get_display(),(255,0,0), rectangle)
            
            else:
                pygame.draw.rect(self.window.get_display(),(255,255,255), rectangle)

        pygame.display.flip()
    def information(self):
        algorithm = font.render(
            "Bubble Sort", True, (255, 255, 255), (0, 0, 0))
        rectangles_drawn = font.render(
            f'Rectangles: {len(super().get_array_of_numbers())}', True, (255, 255, 255), (0, 0, 0))
        swaps = font.render(
            f'Swaps: {self.swaps}', True, (255, 255, 255), (0, 0, 0))
        array_accesses = font.render(
            f'Array Writes: {self.swaps * 2}', True, (255, 255, 255), (0, 0, 0))
        delays = font.render(
            f'Delay {self.delay * 1000} ms', True, (255, 255, 255), (0, 0, 0))

        self.window.get_display().blit(algorithm, (10, 10))
        self.window.get_display().blit(rectangles_drawn, (10, 30))
        self.window.get_display().blit(swaps, (10, 50))
        self.window.get_display().blit(array_accesses, (10, 70))
        self.window.get_display().blit(delays, (10, 90))

    def swap(self,index):
        self.swaps += 1
        self.swap_index = index
        super().get_array_of_numbers()[index], super().get_array_of_numbers()[index +1] = super().get_array_of_numbers()[index+1], super().get_array_of_numbers()[index]

# def sort(array_of_numbers):
#     array_size = len(array_of_numbers)
#     iterations = len(array_of_numbers) - 1

#     for i in range(array_size):
#         draw_rectangles()
        
#         for j in range(iterations):
            
#             if array_of_numbers[j] > array_of_numbers[j+1]:
#                 swap(j)
#                 draw_rectangles()
        
#         array_size -= 1
#         iterations -= 1

# def display(window, rectangles):
#     sort(rectangles.get_array_of_numbers())
#     swap_index = -1
#     rectangles.draw_rectangles(window.get_window())
#     rectangles.sort_finished(window.get_window(), 0.01)

# def swap( index):
#     number_of_swaps += 1
#     swap_index = index
#     array_of_numbers[index], array_of_numbers[index +
#                                                         1] = array_of_numbers[index+1], array_of_numbers[index]

# def draw_rectangles(self,l,r,m,li,ri):
#         self.window.set_bg()
#         self.rectangles.draw_merge_sort(self.window,l,r,m,li,ri)
#         display_sort_algorithm_information(self.window.get_window(),"Merge Sort",self.comparisons,self.array_accesses,self.rectangles.number_of_rectangles,self.delay)
#         pygame.display.flip()
