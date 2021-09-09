from pygame import draw
from algorithms.rectangles import Rectangles
import pygame
from pygame import font
import time

font.init()
font = pygame.font.SysFont('arial', 15)

class TimSort(Rectangles):
    def __init__(self, window, number_of_rectangles, delay):
        super().__init__(window, number_of_rectangles, delay)
        self.window = window
        self.delay = delay
        self.number_of_rectangles = number_of_rectangles
        self.swaps = 0
        self.swap_index = 0
        self.swap_min_index = 0
        self.array_accesses = 0

    def sort(self):
        # Traverse through all array elements
        for i in range(self.number_of_rectangles):
            # Find the minimum element in remaining 
            # unsorted array
            min_idx = i
            for j in range(i+1, self.number_of_rectangles):
                if super().get_array_of_numbers()[min_idx] > super().get_array_of_numbers()[j]:
                    min_idx = j
                    self.array_accesses += 1
                    
                self.draw(i,j,min_idx)
                    
            # Swap the found minimum element with 
            # the first element
            time.sleep(self.delay)
            self.swap(i,min_idx)

            self.array_accesses += 1
        
            
        super().draw() 
        super().draw_finishline()
            

    def set_defaults(self):
        self.swaps = 0
        self.swap_index = 0
        self.swap_min_index = 0
        self.array_accesses = 0
   
    def get_array_of_numbers(self):
        return super().get_array_of_numbers()
    
    def draw(self,index_i,index_j,min_index):
        self.window.set_background()
        
        self.information()
        
        for i in super().get_array_of_numbers():
            val = i
            pos = super().get_array_of_numbers().index(val)
            rectangle = super().get_rectangle_at(pos,val)
            

            if pos == index_i:
                pygame.draw.rect(self.window.get_display(),(0,255,0), rectangle)
            elif pos == index_j:
                pygame.draw.rect(self.window.get_display(),(255,0,0), rectangle)
            elif pos == min_index:
                pygame.draw.rect(self.window.get_display(),(0,0,255), rectangle)
            else:
                pygame.draw.rect(self.window.get_display(),(255,255,255), rectangle)

        pygame.display.flip()
    
    def information(self):
        algorithm = font.render(
            "Selection Sort", True, (255, 255, 255), (0, 0, 0))
        rectangles_drawn = font.render(
            f'Rectangles: {len(super().get_array_of_numbers())}', True, (255, 255, 255), (0, 0, 0))
        swaps = font.render(
            f'Swaps: {self.swaps}', True, (255, 255, 255), (0, 0, 0))
        array_accesses = font.render(
            f'Array Accesses: {self.array_accesses}', True, (255, 255, 255), (0, 0, 0))
        delays = font.render(
            f'Delay {self.delay * 1000} ms', True, (255, 255, 255), (0, 0, 0))

        self.window.get_display().blit(algorithm, (10, 10))
        self.window.get_display().blit(rectangles_drawn, (10, 30))
        self.window.get_display().blit(swaps, (10, 50))
        self.window.get_display().blit(array_accesses, (10, 70))
        self.window.get_display().blit(delays, (10, 90))

    def swap(self,index,min_index):
        self.swaps += 1
        self.swap_index = index
        self.swap_min_index = min_index
        super().get_array_of_numbers()[index], super().get_array_of_numbers()[min_index] = super().get_array_of_numbers()[min_index], super().get_array_of_numbers()[index]
