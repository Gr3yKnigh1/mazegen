from __future__ import annotations

import sys
import pygame

from maze import Maze
from consts import MAZE_SIZE, BACKGROUND_COLOR

class MazeGenApp(object):

	screen_surface: pygame.Surface
	clock: pygame.time.Clock 

	is_running: bool
	fps_limit: int

	maze: Maze

	def __init__(self, window_size: tuple[int, int], fps_limit: int=60) -> None:
		pygame.init()
		
		self.screen_surface = pygame.display.set_mode(window_size)
		self.clock = pygame.time.Clock()
		
		pygame.display.set_caption("Maze Generator [v0.5]")
		
		self.is_running = False
		self.fps_limit = fps_limit

		self.maze = None


	def run(self) -> None:
		self.on_load()
		self.mainloop()


	def on_load(self) -> None:
		self.maze = Maze(MAZE_SIZE)
		self.maze.generate()


	def on_event_handle(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.stop()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					self.maze.generate()
				elif event.key == pygame.K_ESCAPE:
					self.stop()


	def on_draw(self) -> None:
		self.screen_surface.fill(BACKGROUND_COLOR)
		self.maze.draw(self.screen_surface)


	def stop(self) -> None:
		self.is_running = False
		pygame.quit()
		sys.exit()


	def mainloop(self) -> None:
		self.is_running = True
		while self.is_running:
			self.clock.tick(self.fps_limit)
			self.on_event_handle()
			self.on_draw()
			pygame.display.flip()
