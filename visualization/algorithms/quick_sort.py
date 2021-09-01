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


class QuickSort:
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
        ), "Quick Sort", self.comparisons, self.array_accesses, self.rectangles.number_of_rectangles, self.delay)

    def draw_rectangles(self, start, end, pivot):
        self.window.set_bg()
        self.rectangles.draw_quick_sort(
            self.window.get_window(), start, end, pivot)
        display_sort_algorithm_information(self.window.get_window(
        ), "Quick Sort", self.comparisons, self.array_accesses, self.rectangles.number_of_rectangles, self.delay)
        pygame.display.flip()

    def display(self, window):
        self.window = window
        self.quick_sort(0, len(self.array_of_numbers) - 1, self.array_of_numbers)
        self.rectangles.draw_rectangles(window.get_window())
        self.rectangles.sort_finished(self.window.get_window(), 0.01)

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

    # This Function handles sorting part of quick sort
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
                self.draw_rectangles(start, end, pivot)

            # Decrement the end pointer till it finds an
            # element less than pivot
            while array[end] > pivot:
                self.comparisons += 1
                self.array_accesses += 1
                end -= 1
                time.sleep(self.delay)
                self.draw_rectangles(start, end, pivot)

            # If start and end have not crossed each other,
            # swap the numbers on start and end
            if(start < end):
                self.comparisons += 1
                array[start], array[end] = array[end], array[start]
                time.sleep(self.delay)
                self.draw_rectangles(start, end, pivot)

        # Swap pivot element with element on end pointer.
        # This puts pivot on its correct sorted place.
        array[end], array[pivot_index] = array[pivot_index], array[end]
        self.array_accesses += 2
        time.sleep(self.delay)
        self.draw_rectangles(start, end, pivot_index)

        # Returning end pointer to divide the array into 2
        return end
