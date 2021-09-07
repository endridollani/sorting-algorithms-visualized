import pygame
from algorithms.information import display_sort_algorithm_information

class Sort:
    def __init__(self):
        self.window = None
        self.rectangles = None
        self.delay = None
        self.swaps = 0
        self.swap_index = -1
        self.comparisons = 0
        self.array_acceses = 0

    def display(self, sort_index):
        if(sort_index == 0):
            self.bubble_sort()
            self.swap_index = -1
            self.rectangles.draw_rectangles(self.window.get_window())
            self.rectangles.sort_finished(self.window.get_window(), 0.01)
   
    def set(self, window ,rectangles, delay):
        self.window = window
        self.rectangles = rectangles
        self.delay = delay

    def bubble_sort(self):
        array_size = len(self.rectangles.array_of_numbers)
        iterations = len(self.rectangles.array_of_numbers) - 1
       
        def draw_rectangles():
            self.window.set_background()
            self.rectangles.draw_bubble_sort(self.window.get_window(),self.swap_index)
            display_sort_algorithm_information(self.window.get_window(
            ), "Bubble Sort", self.comparisons, self.swaps, self.rectangles.number_of_rectangles, self.delay)
            pygame.display.flip()

        for i in range(array_size):
            draw_rectangles()

            for j in range(iterations):

                if self.rectangles.array_of_numbers[j] > self.rectangles.array_of_numbers[j+1]:
                    self.swap(j)
                    draw_rectangles()

            array_size -= 1
            iterations -= 1


    def swap(self, index):
        self.swaps += 1
        self.swap_index = index
        self.rectangles.array_of_numbers[index], self.rectangles.array_of_numbers[index +
                                                                                  1] = self.rectangles.array_of_numbers[index+1], self.rectangles.array_of_numbers[index]

algorithm = Sort()

def display(sort_index, window, rectangles,delay):
    algorithm.set(window,rectangles,delay)
    algorithm.display(sort_index)
