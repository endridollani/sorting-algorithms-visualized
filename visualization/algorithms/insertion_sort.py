from pygame import draw
from algorithms.rectangles import Rectangles
import pygame
from pygame import font
import time

font.init()
font = pygame.font.SysFont('arial', 15)

class InsertionSort(Rectangles):
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

        # Traverse through 1 to len(arr)
        for i in range(1, self.number_of_rectangles):
        
            key = super().get_array_of_numbers()[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >=0 and key < super().get_array_of_numbers()[j] :
                super().get_array_of_numbers()[j+1] = super().get_array_of_numbers()[j]
                self.swaps += 1
                self.array_accesses +=1
                j -= 1
                time.sleep(self.delay)
                self.draw(i,j) 

        
            super().get_array_of_numbers()[j+1] = key
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
    
    def draw(self,index_i,index_j):
        self.window.set_background()
        
        self.information()
        
        for i in super().get_array_of_numbers():
            val = i
            pos = super().get_array_of_numbers().index(val)
            rectangle = super().get_rectangle_at(pos,val)
            
            

            if pos == index_i:
                pygame.draw.rect(self.window.get_display(),(0,255,0), rectangle)
            elif pos == index_j or pos == index_j+1:
                pygame.draw.rect(self.window.get_display(),(255,0,0), rectangle)
            else:
                pygame.draw.rect(self.window.get_display(),(255,255,255), rectangle)

    
        pygame.display.flip()
    
    def information(self):
        algorithm = font.render(
            "Insertion Sort", True, (255, 255, 255), (0, 0, 0))
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