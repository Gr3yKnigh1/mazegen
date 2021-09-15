from __future__ import annotations
from typing import TYPE_CHECKING
import random
if TYPE_CHECKING:
	from pygame.surface import Surface

from direction import Directions
from cell import Cell


class Maze(object):

	_size: tuple[int, int]
	_start_position: tuple[int, int]
	_cells: list[Cell]

	def __init__(self, _size: tuple[int, int], starting_position=(0, 0)) -> None:
		self._size = _size
		self._start_position = starting_position
		self._cells = []


	def add(self, cell: Cell) -> None:
		if cell not in self._cells:
			self._cells.append(cell)
		else:
			raise ValueError(f"{cell} already added")


	def get_cell(self, x: int, y: int) -> Cell:
		if x < 0 or y < 0 or x > self._size[0]-1 or y > self._size[1]-1:
			raise IndexError(f"Out of range coordinates: x: {x}, y: {y}. _size: {self._size}")

		for cell in self._cells:
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

		self._clear_cells()

		to_visit = self.get_cell(*self._start_position)
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
		while len(visited_cells) < self._size[0] * self._size[1]:
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


	def draw(self, surface: Surface) -> None:
		for cell in self._cells:
			cell.draw(surface)


	# private:
	def _clear_cells(self) -> None:
		self._cells.clear()

		for row in range(self._size[1]):
			for col in range(self._size[0]):
				self.add(Cell(col, row, self))
