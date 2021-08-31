import pygame
from pygame import font
import time

font.init()

font = pygame.font.SysFont('arial', 15)

def display_sort_algorithm_information(window, algorithm, swap_number, array_writes, number_of_rectangles, delay_in_millisecondes):
    algorithm_selected = font.render(
        f'{algorithm}', True, (255, 255, 255), (0, 0, 0))
    algorithm_rect_number = font.render(
        f'Rectangles: {number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
    algorithm_swaps = font.render(
        f'Swaps: {swap_number}', True, (255, 255, 255), (0, 0, 0))
    algorithm_writes = font.render(
        f'Array Writes: {array_writes}', True, (255, 255, 255), (0, 0, 0))
    delays = font.render(
        f'Delay {delay_in_millisecondes * 1000} ms', True, (255, 255, 255), (0, 0, 0))

    window.blit(algorithm_selected, (10, 10))
    window.blit(algorithm_rect_number, (10, 30))
    window.blit(algorithm_swaps, (10, 50))
    window.blit(algorithm_writes, (10, 70))
    window.blit(delays, (10, 90))

class BubbleSort:
    def __init__(self, rectangles, delay_in_millisecondes):
        self.rectangles = rectangles
        self.array_of_numbers = self.rectangles.get_array_of_numbers()
        self.window = None
        self.number_of_swaps = 0
        self.delay = delay_in_millisecondes / 1000
        self.swap_index = -1

    def draw_rectangles(self):
        time.sleep(self.delay)
        self.window.set_bg()
        self.display_information()
        self.rectangles.draw_bubble_sort(self.window.get_window(),self.swap_index)
        pygame.display.flip()

    def display_information(self):
        display_sort_algorithm_information(self.window.get_window(
        ), "Bubble Sort", self.number_of_swaps, self.number_of_swaps * 2, len(self.array_of_numbers), self.delay)        

    def bubble_sort(self):
        array_size = len(self.array_of_numbers)
        iterations = len(self.array_of_numbers) - 1

        for i in range(array_size):
            self.draw_rectangles()
            
            for j in range(iterations):
                
                if self.array_of_numbers[j] > self.array_of_numbers[j+1]:
                    self.swap(j)
                    self.draw_rectangles()
            
            array_size -= 1
            iterations -= 1

    def display(self, window):
        self.window = window
        self.bubble_sort()
        self.rectangles.sort_finished(self.window.get_window(), self.delay)

    def swap(self, index):
        self.number_of_swaps += 1
        self.swap_index = index
        self.array_of_numbers[index], self.array_of_numbers[index +
                                                            1] = self.array_of_numbers[index+1], self.array_of_numbers[index]