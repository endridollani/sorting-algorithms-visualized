from algorithms.rectangles import Rectangles
import pygame
from pygame import font
import time

font.init()
font = pygame.font.SysFont('arial', 15)

class HeapSort(Rectangles):
    def __init__(self, window, number_of_rectangles, delay):
        super().__init__(window, number_of_rectangles, delay)
        self.window = window
        self.delay = delay
        self.number_of_rectangles = number_of_rectangles
        self.swaps = 0
        self.array_accesses = 0
    
    def sort(self):
        self.heap_sort(super().get_array_of_numbers())

        super().draw() 
        super().draw_finishline()

    # To heapify subtree rooted at index i.
    # n is size of heap
    
    def heapify(self,array, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and array[largest] < array[l]:
            largest = l

            self.array_accesses += 1
            time.sleep(self.delay)
            self.draw(l,largest)
    
        # See if right child of root exists and is
        # greater than root
        if r < n and array[largest] < array[r]:
            largest = r

            time.sleep(self.delay)
            self.draw(r,largest)
    
        # Change root, if needed
        if largest != i:
            array[i], array[largest] = array[largest], array[i]  # swap
           
            time.sleep(self.delay)
            self.draw(i,largest)
            # Heapify the root.
            self.heapify(array, n, largest)

    # The main function to sort an array of given size
    def heap_sort(self,array):
        n = len(array)
    
        # Build a maxheap.
        for i in range(n//2 - 1, -1, -1):
            self.heapify(array, n, i)
    
        # One by one extract elements
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]  # swap
            self.swaps += 1
            self.heapify(array, i, 0)
        

    def set_defaults(self):
        self.swaps = 0
        self.array_accesses = 0
   
    def get_array_of_numbers(self):
        return super().get_array_of_numbers()
    
    def draw(self,index, largest):
        self.window.set_background()
        
        self.information()
        
        for i in self.array_of_numbers:
            val = i
            pos = self.array_of_numbers.index(val)
            rectangle = self.get_rectangle_at(pos,val)
            if pos == index or pos == largest:
                pygame.draw.rect(self.window.get_display(),(0,15,255), rectangle)
            else:
                pygame.draw.rect(self.window.get_display(),(255,255,255), rectangle)

        pygame.display.flip()
    
    def information(self):
        algorithm = font.render(
            "Heap Sort", True, (255, 255, 255), (0, 0, 0))
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
