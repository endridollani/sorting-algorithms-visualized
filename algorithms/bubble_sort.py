import pygame
import time

class BubbleSort:
	def __init__(self,window,rectangles):
		self.window = window
		self.rectangles = rectangles
		self.swaped = False
		self.array_of_numbers = self.rectangles.get_array_of_numbers()
	
	def display(self,window,delay):
		array_size = len(self.array_of_numbers)
		iterations = len(self.array_of_numbers) - 1
		for i in range(array_size):
			for j in range(iterations):
				if self.array_of_numbers[j] > self.array_of_numbers[j+1]:
					time.sleep(delay)
					self.swap(j,window)
				
				if not self.swaped:
					window.set_bg()
					self.rectangles.draw_rectangles(window.get_window())
					pygame.display.flip()
				self.swaped = False
			array_size -=1
			iterations -=1
		self.rectangles.sort_finished(window.get_window(),delay-0.005)


	def swap(self, index,window):
		self.swaped = True
		self.array_of_numbers[index],self.array_of_numbers[index+1] = self.array_of_numbers[index+1],self.array_of_numbers[index]
		window.set_bg()
		self.rectangles.draw_rectangles(window=window.get_window(),swap1=index,swap2=index+1)
		pygame.display.flip()