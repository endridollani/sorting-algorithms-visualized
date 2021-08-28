import pygame
import time

class BubbleSort:
	def __init__(self,window,rectangles):
		self.window = window
		self.rectangles = rectangles
		self.array_of_numbers = self.rectangles.get_array_of_numbers()
	
	def display(self,window):
		for i in range(len(self.array_of_numbers)):
			for j in range(len(self.array_of_numbers) - 1):
				if self.array_of_numbers[j] > self.array_of_numbers[j+1]:
					time.sleep(0.005)
					self.swap(j)
				window.set_bg()
				self.rectangles.draw_rectangles(window.get_window())
				pygame.display.flip()

	
	def swap(self, index):
		self.array_of_numbers[index],self.array_of_numbers[index+1] = self.array_of_numbers[index+1],self.array_of_numbers[index]				

