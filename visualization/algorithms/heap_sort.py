import pygame
from pygame import font
import time

font.init()

font = pygame.font.SysFont('arial', 15)


def display_sort_algorithm_information(window, algorithm, swaps, array_accesses, number_of_rectangles, delay_in_millisecondes):
    algorithm_selected = font.render(
        f'{algorithm}', True, (255, 255, 255), (0, 0, 0))
    algorithm_rect_number = font.render(
        f'Rectangles: {number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
    algorithm_swaps = font.render(
        f'Swaps: {swaps}', True, (255, 255, 255), (0, 0, 0))
    algorithm_accesses = font.render(
        f'Array accesses: {array_accesses}', True, (255, 255, 255), (0, 0, 0))
    delays = font.render(
        f'Delay {delay_in_millisecondes * 1000} ms', True, (255, 255, 255), (0, 0, 0))

    window.blit(algorithm_selected, (10, 10))
    window.blit(algorithm_rect_number, (10, 30))
    window.blit(algorithm_swaps, (10, 50))
    window.blit(algorithm_accesses, (10, 70))
    window.blit(delays, (10, 90))


class HeapSort:
    def __init__(self, rectangles, delay_in_millisecondes,window):
        self.rectangles = rectangles
        self.array_of_numbers = self.rectangles.get_array_of_numbers()
        self.window = window
        self.delay = delay_in_millisecondes / 1000
        self.swaps = 0
        self.array_accesses = 0

    def set_window_and_delay(self, window, delay):
        self.window = window
        self.delay = delay

    def display_information(self):
        display_sort_algorithm_information(self.window.get_window(
        ), "Heap Sort", self.swaps, self.array_accesses, self.rectangles.number_of_rectangles, self.delay)

    def draw_rectangles(self,index, largest):
        self.window.set_bg()
        self.rectangles.draw_heap_sort(
            self.window.get_window(), index, largest)
        display_sort_algorithm_information(self.window.get_window(
        ), "Heap Sort", self.swaps, self.array_accesses, self.rectangles.number_of_rectangles, self.delay)
        pygame.display.flip()

    def display(self):
        self.heap_sort(self.array_of_numbers)
        self.rectangles.draw_rectangles(self.window.get_window())
        self.rectangles.sort_finished(self.window.get_window(), 0.01)

    # Python program for implementation of heap Sort
    
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
            self.draw_rectangles(l,largest)
    
        # See if right child of root exists and is
        # greater than root
        if r < n and array[largest] < array[r]:
            largest = r

            time.sleep(self.delay)
            self.draw_rectangles(r,largest)
    
        # Change root, if needed
        if largest != i:
            array[i], array[largest] = array[largest], array[i]  # swap
           
            time.sleep(self.delay)
            self.draw_rectangles(i,largest)
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
    