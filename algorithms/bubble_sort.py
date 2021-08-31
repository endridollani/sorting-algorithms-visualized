import pygame
from pygame import font
import time

font.init()

font = pygame.font.SysFont('arial', 15)


def display_sort_algorithm_information(window, algorithm, swap_number, array_writes, number_of_rectangles, delay_in_millisecondes):
    algorithm_selected = font.render(
        f'Algorithm Selected: {algorithm}', True, (255, 255, 255), (0, 0, 0))
    algorithm_rect_number = font.render(
        f'Rectangles Drawn: {number_of_rectangles}', True, (255, 255, 255), (0, 0, 0))
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
        self.window = None
        self.swaped = False
        self.number_of_swaps = 0
        self.array_of_numbers = self.rectangles.get_array_of_numbers()
        self.delay = delay_in_millisecondes / 1000

    def get_swaps_number(self): return self.number_of_swaps
    def set_swaps_number_to_zero(self): self.number_of_swaps = 0

    def get_array_writes(self): return self.number_of_swaps * 2

    def display_information(self):
        pass

    def display(self, window):
        self.window = window
        array_size = len(self.array_of_numbers)
        iterations = len(self.array_of_numbers) - 1
        for i in range(array_size):
            for j in range(iterations):
                if self.array_of_numbers[j] > self.array_of_numbers[j+1]:
                    time.sleep(delay)
                    self.swap(j, window, delay)

                if not self.swaped:
                    window.set_bg()
                    self.rectangles.draw_rectangles(window.get_window())
                    display_sort_algorithm_information(window.get_window(
                    ), "Bubble Sort", self.number_of_swaps, self.number_of_swaps * 2, len(self.array_of_numbers), delay)
                    pygame.display.flip()
                self.swaped = False
            array_size -= 1
            iterations -= 1
        self.rectangles.sort_finished(window.get_window(), delay*2)

    def swap(self, index, window, delay):
        self.swaped = True
        self.number_of_swaps += 1
        self.array_of_numbers[index], self.array_of_numbers[index +
                                                            1] = self.array_of_numbers[index+1], self.array_of_numbers[index]
        window.set_bg()
        self.rectangles.draw_rectangles(
            window=window.get_window(), swap1=index, swap2=index+1)
        display_sort_algorithm_information(window.get_window(
        ), "Bubble Sort", self.number_of_swaps, self.number_of_swaps * 2, len(self.array_of_numbers), delay_in_millisecondes=delay)
        pygame.display.flip()
