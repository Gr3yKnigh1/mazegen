from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from pygame.surface import Surface
import sys
import pygame
from maze import Maze


__version__ = "0.7.0"


IS_RUNNING = False
FPS_LIMIT = 60
BACKGROUND_COLOR = "#FCC4C4"

CELL_SIZE = 64, 64 # in pixels
WALL_COLOR = "#B95FD0"
WALL_WIDTH = 1
MAZE_SIZE = 10, 10
WINDOW_SIZE = MAZE_SIZE[0] * CELL_SIZE[0], MAZE_SIZE[1] * CELL_SIZE[1]


def stop() -> None:
	global IS_RUNNING
	IS_RUNNING = False


def on_event_handle(maze: Maze) -> None:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			stop()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				maze.generate()
			elif event.key == pygame.K_ESCAPE:
				stop()


def on_draw(screen_surface: Surface, maze: Maze) -> None:
	screen_surface.fill(BACKGROUND_COLOR)
	maze.draw(screen_surface)


def main() -> int:
	global IS_RUNNING

	# Pygame setup
	screen_surface = pygame.display.set_mode(WINDOW_SIZE)
	clock = pygame.time.Clock()
	pygame.display.set_caption(f"Maze Generator [{__version__}]")

	# Maze setup
	maze = Maze(size=MAZE_SIZE)
	maze.generate()

	# Mainloop
	IS_RUNNING = True
	while IS_RUNNING:
		clock.tick(FPS_LIMIT)
		on_event_handle(maze)
		on_draw(screen_surface, maze)
		pygame.display.flip()
	pygame.quit()
	return 0


if __name__ == '__main__':
	sys.exit(main())
