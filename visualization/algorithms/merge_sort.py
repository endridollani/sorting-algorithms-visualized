from algorithms.rectangles import Rectangles
import pygame
from pygame import font
import time

font.init()
font = pygame.font.SysFont('arial', 15)

class MergeSort(Rectangles):
    def __init__(self, window, number_of_rectangles, delay):
        super().__init__(window, number_of_rectangles, delay)
        self.window = window
        self.delay = delay
        self.number_of_rectangles = number_of_rectangles
        self.comparisons = 0
        self.array_accesses = 0

    def sort(self):
        self.merge_sort(super().get_array_of_numbers(), 0, self.number_of_rectangles - 1)
            
        super().draw() 
        super().draw_finishline()

    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]
            self.array_accesses +=1

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
            self.array_accesses +=1

        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                time.sleep(self.delay)
                self.draw(l,r,m,super().get_array_of_numbers().index(L[i]),super().get_array_of_numbers().index(R[j]))
                i += 1
                self.comparisons += 1
                self.array_accesses +=1
                
            else:
                arr[k] = R[j]
                time.sleep(self.delay)
                self.draw(l,r,m,super().get_array_of_numbers().index(arr[k]),super().get_array_of_numbers().index(R[j]))
                j += 1
                self.array_accesses += 2
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            time.sleep(self.delay)
            self.draw(l,r,m,super().get_array_of_numbers().index(arr[k]),super().get_array_of_numbers().index(L[i]))
            i += 1
            k += 1
            self.comparisons +=1
            self.array_accesses += 2


        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            time.sleep(self.delay)
            self.draw(l,r,m,super().get_array_of_numbers().index(arr[k]),super().get_array_of_numbers().index(R[j]))
            j += 1
            k += 1
            self.comparisons += 1
            self.array_accesses += 2 


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


    def set_defaults(self):
        self.comparisons = 0
        self.array_accesses = 0
   
    def get_array_of_numbers(self):
        return super().get_array_of_numbers()
    
    def draw(self,l,r,m,li,ri):
        self.window.set_background()
        
        self.information()
        
        for i in super().get_array_of_numbers():
            val = i
            pos = super().get_array_of_numbers().index(val)
            rectangle = super().get_rectangle_at(pos,val)
            if pos == l or pos == r:
                pygame.draw.rect(self.window.get_display(),(0, 255, 0), rectangle)
            elif pos == m:
                pygame.draw.rect(self.window.get_display(),(0, 150, 255), rectangle)
            elif pos == li or pos == ri:
                pygame.draw.rect(self.window.get_display(),(255, 0, 0), rectangle)
            else:
                pygame.draw.rect(self.window.get_display(),(255, 255, 255), rectangle)

        pygame.display.flip()
    
    def information(self):
        algorithm = font.render(
            "Merge Sort", True, (255, 255, 255), (0, 0, 0))
        rectangles_drawn = font.render(
            f'Rectangles: {len(super().get_array_of_numbers())}', True, (255, 255, 255), (0, 0, 0))
        swaps = font.render(
            f'Comparisons: {self.comparisons}', True, (255, 255, 255), (0, 0, 0))
        array_accesses = font.render(
            f'Array Accesses: {self.array_accesses}', True, (255, 255, 255), (0, 0, 0))
        delays = font.render(
            f'Delay {self.delay * 1000} ms', True, (255, 255, 255), (0, 0, 0))

        self.window.get_display().blit(algorithm, (10, 10))
        self.window.get_display().blit(rectangles_drawn, (10, 30))
        self.window.get_display().blit(swaps, (10, 50))
        self.window.get_display().blit(array_accesses, (10, 70))
        self.window.get_display().blit(delays, (10, 90))