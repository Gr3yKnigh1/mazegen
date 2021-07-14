from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from maze import Maze

import pygame

from direction import Direction, Directions


side = tuple[int, int]
direction = tuple[int, int]


CELL_SIZE = 64, 64 # in pixels
WALL_COLOR = "#B95FD0"
WALL_WIDTH = 1


class Cell(object):

	x: int
	y: int

	maze: Maze
	walls: dict[direction, side]
	visited: bool
	transitions: list[direction]

	def __init__(self, x: int, y: int, maze: Maze) -> str:
		self.x = x
		self.y = y
		self.maze = maze

		rect = pygame.Rect(
			self.x * CELL_SIZE[0],
			self.y * CELL_SIZE[1],
			*CELL_SIZE
			)

		r = rect
		self.walls = {
			Direction.N : (r.topleft, r.topright),
			Direction.E : (r.topright, r.bottomright),
			Direction.S : (r.bottomright, r.bottomleft),
			Direction.W : (r.bottomleft, r.topleft)
		}

		self.visited = False
		self.transitions = []


	def __repr__(self) -> str:
		return f"<Cell {self.x}:{self.y}:{1 if self.visited else 0}>"


	def make_transition(self, cell: Cell) -> None:
		if cell not in self.transitions:
			self.transitions.append(cell)
			cell.make_transition(self)
			# cell.transitions.append(self)

			#--Removing Walls
			direction = self.maze.get_cell_direction(self, cell)
			# opposite_direction = Direction.get_opposite(direction)
			
			self.walls[direction] = None
			# cell.walls[opposite_direction] == None


	def get_neighbours(self) -> list[Cell]:
		neighbours = []
		for direction in Directions:
			try:
				neighbour = self.maze.get_cell(self.x + direction[0], self.y + direction[1])
			except IndexError as e:
				continue

			neighbours.append(neighbour)

		return neighbours


	def draw(self, surface: pygame.Surface) -> None:
		for wall in self.walls.values():
			if wall != None:
				pygame.draw.line(surface, pygame.Color(WALL_COLOR), *wall, WALL_WIDTH)
