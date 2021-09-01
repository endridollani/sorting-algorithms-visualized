import pygame
from pygame import font
import time

font.init()

font = pygame.font.SysFont('arial', 15)


def display_sort_algorithm_information(window, algorithm, comparisons, array_accesses, number_of_rectangles, delay_in_millisecondes):
    algorithm_selected = font.render(
        f'{algorithm}', True, (255, 255, 255), (0, 0, 0))
    algorithm_rect_number = font.render(
        f'Rectangles: {number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
    algorithm_comparisons = font.render(
        f'Comparisons: {comparisons}', True, (255, 255, 255), (0, 0, 0))
    algorithm_accesses = font.render(
        f'Array accesses: {array_accesses}', True, (255, 255, 255), (0, 0, 0))
    delays = font.render(
        f'Delay {delay_in_millisecondes * 1000} ms', True, (255, 255, 255), (0, 0, 0))

    window.blit(algorithm_selected, (10, 10))
    window.blit(algorithm_rect_number, (10, 30))
    window.blit(algorithm_comparisons, (10, 50))
    window.blit(algorithm_accesses, (10, 70))
    window.blit(delays, (10, 90))


class HeapSort:
    def __init__(self, rectangles, delay_in_millisecondes):
        self.rectangles = rectangles
        self.array_of_numbers = self.rectangles.get_array_of_numbers()
        self.window = None
        self.delay = delay_in_millisecondes / 1000
        self.comparisons = 0
        self.array_accesses = 0

    def set_window_and_delay(self, window, delay):
        self.window = window
        self.delay = delay

    def display_information(self):
        display_sort_algorithm_information(self.window.get_window(
        ), "Heap Sort", self.comparisons, self.array_accesses, self.rectangles.number_of_rectangles, self.delay)

    def draw_rectangles(self, start, end, pivot):
        self.window.set_bg()
        self.rectangles.draw_heap_sort(
            self.window.get_window(), start, end, pivot)
        display_sort_algorithm_information(self.window.get_window(
        ), "Heap Sort", self.comparisons, self.array_accesses, self.rectangles.number_of_rectangles, self.delay)
        pygame.display.flip()

    def display(self, window):
        self.window = window
        self.heap_sort()
        self.rectangles.draw_rectangles(window.get_window())
        self.rectangles.sort_finished(self.window.get_window(), 0.01)
