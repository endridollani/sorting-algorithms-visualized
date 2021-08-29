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


class MergeSort:
    def __init__(self, rectangles):
        self.rectangles = rectangles
        # self.swaped = False
        # self.number_of_swaps = 0
        self.array_of_numbers = self.rectangles.get_array_of_numbers()
        self.window = None
        self.delay = None
    # def get_swaps_number(self): return self.number_of_swaps
    # def set_swaps_number_to_zero(self): self.number_of_swaps = 0

    # def get_array_writes(self): return self.number_of_swaps * 2
    def set_window_and_delay(self,window,delay): 
        self.window = window
        self.delay = delay 

    def draw_rectangles(self,l,r,k):
        self.window.set_bg()
        self.rectangles.draw_merge_sort(self.window.get_window(),l,r,k)
        pygame.display.flip()

    def display(self, window, delay):
        self.set_window_and_delay(window,delay)
        self.merge_sort(self.array_of_numbers, 0,
                        len(self.array_of_numbers) - 1)

    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                time.sleep(self.delay)
                self.draw_rectangles(l,r,k)
                i += 1
                
            else:
                arr[k] = R[j]
                time.sleep(self.delay)
                self.draw_rectangles(l,r,k)
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            time.sleep(self.delay)
            self.draw_rectangles(l,r,k)
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            time.sleep(self.delay)
            self.draw_rectangles(l,r,k)
            j += 1
            k += 1

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted

    def merge_sort(self,arr, l, r):
        if l < r:

            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l+(r-l)//2

            # Sort first and second halves
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m+1, r)
            self.merge(arr, l, m, r)
