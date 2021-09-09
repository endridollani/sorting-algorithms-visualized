from pygame import draw
from algorithms.rectangles import Rectangles
import pygame
from pygame import font
import time

font.init()
font = pygame.font.SysFont('arial', 15)

MIN_MERGE = 32

class TimSort(Rectangles):
    def __init__(self, window, number_of_rectangles, delay):
        super().__init__(window, number_of_rectangles, delay)
        self.window = window
        self.delay = delay
        self.number_of_rectangles = number_of_rectangles
        self.swaps = 0
        self.array_accesses = 0
        self.comparisons = 0
        self.array_accesses = 0

    def sort(self):
        self.timSort(super().get_array_of_numbers())
        super().draw() 
        super().draw_finishline()

    def calcMinRun(self,n):
        """Returns the minimum length of a
        run from 23 - 64 so that
        the len(array)/minrun is less than or
        equal to a power of 2.
    
        e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
        ..., 127=>64, 128=>32, ...
        """
        r = 0
        while n >= MIN_MERGE:
            r |= n & 1
            n >>= 1
            self.comparisons += 1
        return n + r

    # This function sorts array from left index to
    # to right index which is of size atmost RUN
    def insertionSort(self,arr, left, right):
        for i in range(left + 1, right + 1):
            j = i
            while j > left and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
                self.swaps += 1
                self.array_accesses +=1
                self.comparisons += 2
                time.sleep(self.delay)
                self.draw(-1,-1,-1,-1,-1,i,j)
                
    
    
    # Merge function merges the sorted runs
    def merge(self,arr, l, m, r):
        
        # original array is broken in two parts
        # left and right array
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(arr[l + i])
            self.array_accesses += 1
        for i in range(0, len2):
            right.append(arr[m + 1 + i])
            self.array_accesses +=1

    
        i, j, k = 0, 0, l
        
        # after comparing, we merge those two array
        # in larger sub array
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                time.sleep(self.delay)
                self.draw(l,r,m,super().get_array_of_numbers().index(left[i]),super().get_array_of_numbers().index(right[j]),-1,-1)
                i += 1
                self.comparisons += 1
                self.array_accesses +=1
    
            else:
                arr[k] = right[j]
                time.sleep(self.delay)
                self.draw(l,r,m,super().get_array_of_numbers().index(arr[k]),super().get_array_of_numbers().index(right[j]),-1,-1)
                j += 1
                self.array_accesses += 2

            k += 1
    
        # Copy remaining elements of left, if any
        while i < len1:
            arr[k] = left[i]
            time.sleep(self.delay)
            self.draw(l,r,m,super().get_array_of_numbers().index(arr[k]),super().get_array_of_numbers().index(left[i]),-1,-1)
            k += 1
            i += 1
            self.comparisons +=1
            self.array_accesses += 2
    
        # Copy remaining element of right, if any
        while j < len2:
            arr[k] = right[j]
            time.sleep(self.delay)
            self.draw(l,r,m,super().get_array_of_numbers().index(arr[k]),super().get_array_of_numbers().index(right[j]),-1,-1)
            j += 1
            k += 1
            self.comparisons += 1
            self.array_accesses += 2 
    
    
    # Iterative Timsort function to sort the
    # array[0...n-1] (similar to merge sort)
    def timSort(self,arr):
        n = len(arr)
        minRun = self.calcMinRun(n)
        
        # Sort individual subarrays of size RUN
        for start in range(0, n, minRun):
            end = min(start + minRun - 1, n - 1)
            self.insertionSort(arr, start, end)
    
        # Start merging from size RUN (or 32). It will merge
        # to form size 64, then 128, 256 and so on ....
        size = minRun
        while size < n:
            
            # Pick starting point of left sub array. We
            # are going to merge arr[left..left+size-1]
            # and arr[left+size, left+2*size-1]
            # After every merge, we increase left by 2*size
            for left in range(0, n, 2 * size):
    
                # Find ending point of left sub array
                # mid+1 is starting point of right sub array
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))
    
                # Merge sub array arr[left.....mid] &
                # arr[mid+1....right]
                if mid < right:
                    self.merge(arr, left, mid, right)
    
            size = 2 * size
    

    def set_defaults(self):
        self.swaps = 0
        self.array_accesses = 0
        self.comparisons = 0
   
    def get_array_of_numbers(self):
        return super().get_array_of_numbers()
    
    def draw(self,l,r,m,li,ri,ins_i,ins_j):
        self.window.set_background()
        
        self.information()
        
        for i in super().get_array_of_numbers():
            val = i
            pos = super().get_array_of_numbers().index(val)
            rectangle = super().get_rectangle_at(pos,val)
            if pos == l or pos == r or pos == ins_i:
                pygame.draw.rect(self.window.get_display(),(0, 255, 0), rectangle)
            elif pos == m:
                pygame.draw.rect(self.window.get_display(),(0, 150, 255), rectangle)
            elif pos == li or pos == ri or pos == ins_j or pos == ins_j+1:
                pygame.draw.rect(self.window.get_display(),(255, 0, 0), rectangle)
            else:
                pygame.draw.rect(self.window.get_display(),(255, 255, 255), rectangle)

        pygame.display.flip()
    
    def information(self):
        algorithm = font.render(
            "Tim Sort", True, (255, 255, 255), (0, 0, 0))
        rectangles_drawn = font.render(
            f'Rectangles: {len(super().get_array_of_numbers())}', True, (255, 255, 255), (0, 0, 0))
        swaps = font.render(
            f'Swaps: {self.swaps}', True, (255, 255, 255), (0, 0, 0))
        array_accesses = font.render(
            f'Array Accesses: {self.array_accesses}', True, (255, 255, 255), (0, 0, 0))
        comparisons = font.render(
            f'Array Accesses: {self.comparisons}', True, (255, 255, 255), (0, 0, 0))
        delays = font.render(
            f'Delay {self.delay * 1000} ms', True, (255, 255, 255), (0, 0, 0))

        self.window.get_display().blit(algorithm, (10, 10))
        self.window.get_display().blit(rectangles_drawn, (10, 30))
        self.window.get_display().blit(swaps, (10, 50))
        self.window.get_display().blit(array_accesses, (10, 70))
        self.window.get_display().blit(comparisons, (10, 90))
        self.window.get_display().blit(delays, (10, 110))