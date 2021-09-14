from __future__ import annotations
from typing import TYPE_CHECKING
import random
if TYPE_CHECKING:
	import pygame

from direction import Directions
from cell import Cell


class Maze(object):

	size: tuple[int, int]
	cells: list[Cell]

	__starting_position: tuple[int, int]

	def __init__(self, size: tuple[int, int]) -> None:
		self.size = size
		self.cells = []

		self.__starting_position = (0, 0)


	def __repr__(self) -> str:
		string = ""
		for cell in self.cells:
			if cell.x == self.size[0] - 1:
				string += repr(cell) + "\n"
			else:
				string += repr(cell) + " "

		return string


	def add(self, cell: Cell) -> None:
		if cell not in self.cells:
			self.cells.append(cell)
		else:
			cells_repr = repr(self.cells)[0:50] + "..." if len(repr(self.cells)) > 51 else self.cells
			raise ValueError(f"{cell} already added in Maze {cells_repr}")


	def get_cell(self, x: int, y: int) -> Cell:
		if x < 0 or y < 0 or x > self.size[0]-1 or y > self.size[1]-1:
			raise IndexError(f"Out of range coordinates: x: {x}, y: {y}. Size: {self.size}")

		for cell in self.cells:
			if (cell.x, cell.y) == (x, y):
				return cell


	def get_cell_direction(self, c1: Cell, c2: Cell) -> tuple[int, int]:
		neighbours = c1.get_neighbours()

		if c2 not in neighbours:
			return None

		for direction in Directions:
			if (c1.x + direction[0], c1.y + direction[1]) == (c2.x, c2.y):
				return direction


	def generate(self) -> None:
		#--Add new Cells
		self.cells.clear()

		for row in range(self.size[1]):
			for col in range(self.size[0]):
				self.add(Cell(col, row, self))

		#--Setting up
		to_visit = self.get_cell(*self.__starting_position)
		visited_cells = []
		visited_stack = []

		def visit(cell):
			if not cell.visited:
				# print(f"Visiting {cell}")
				cell.visited = True
				visited_cells.append(cell)
				visited_stack.append(cell)
			else:
				pass

		#--Generate start
		while len(visited_cells) < self.size[0] * self.size[1]:
			visit(to_visit)
			neighbours = to_visit.get_neighbours()
			not_visited_neighbours = [cell for cell in neighbours if not cell.visited]

			if len(not_visited_neighbours) > 0:
				next_cell = random.choice(not_visited_neighbours)
				to_visit.make_transition(next_cell)
				to_visit = next_cell
			else:
				# print(f"Pop {visited_stack[-1]}")
				visited_stack.pop()
				to_visit = visited_stack[-1]


	def draw(self, surface: pygame.Surface) -> None:
		for cell in self.cells:
			cell.draw(surface)
