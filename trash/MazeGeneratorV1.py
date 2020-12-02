import random
import pygame


maze_size = (4, 4)
cell_size = (64, 64)

class Direction:
	N = (0, +1)
	S = (0, -1)
	E = (+1, 0)
	W = (-1, 0)


Directions = [Direction.N, Direction.E, Direction.S, Direction.W]

class Cell:
	_cells = []

	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.transitions = []
		self._transitions = []
		self.visited = False

		self._rect = pygame.Rect(self.x * cell_size[0], self.y * cell_size[1], *cell_size)
		self.wall_positions = {
			Direction.N : (self._rect.topleft, self._rect.topright),
			Direction.E : (self._rect.topright, self._rect.bottomright),
			Direction.S : (self._rect.bottomright, self._rect.bottomleft),
			Direction.W : (self._rect.bottomleft, self._rect.topleft)
		}

		self.__class__._cells.append(self)

	def __repr__(self):
		return f"<Cell {self.x}:{self.y}:{1 if self.visited else 0}>"

	def make_transition(self, cell):
		if cell not in self.transitions and self not in cell.transitions:
			self.transitions.append(cell)
			self._transitions.append(cell)
			cell.transitions.append(self)

	def get_neighbors(self):
		neighbors = []

		for direction in Directions:
			n_x, n_y = self.x + direction[0], self.y + direction[1]

			# print(f"{(self.x, self.y)}->{direction}  {n_x} : {n_y}")
			if n_x >= 0 and n_x <= maze_size[0] - 1:
				if n_y >= 0 and n_y <= maze_size[1] - 1:
					neighbor = self.__class__.get_cell(n_x, n_y)
					neighbors.append(neighbor)
		return neighbors

	@classmethod
	def get_cell(cls, x, y):
		for cell in cls._cells:
			if cell.x == x and cell.y == y:
				return cell


	def draw(self, surface):
		for wall_position in self.wall_positions.values():
			pygame.draw.line(surface, pygame.Color('#9C74E4'), *wall_position, 1)


def draw_maze(cells):
	pygame.init()
	screen = pygame.display.set_mode((maze_size[0] * cell_size[0], maze_size[1] * cell_size[1]))
	pygame.display.set_caption("Maze Generator Version 0.1")

	for cell in cells:
		#--Get Cell position
		# rect = pygame.Rect(
		# 	cell.x * cell_size[0],
		# 	cell.y * cell_size[1],
		# 	*cell_size
		# 	)

		#--Draw Cell
		# pygame.draw.rect(screen, pygame.Color('#9C74E4'), rect, 1)
		cell.draw(screen)

	clock = pygame.time.Clock()
	loop = True
	while loop:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False

		pygame.display.flip()


def main():
	visited_cells = []
	cell_stack = []

	for row in range(maze_size[1]):
		for col in range(maze_size[0]):
			Cell(col, row)

	cells = Cell._cells
	print_neighbors = lambda index: print(f"{cells[index]}'s neighbors: {cells[index].get_neighbors()}")


	def print_cells():
		# --Print cells
		for cell in cells:
			print(cell, end=" ")
			if cell.x + 1 >= maze_size[0]:
				print()


	def print_transitions():
		for cell in cells:
			print(f"{cell} -> {cell._transitions}")

	
	def visit(cell):

		cell.visited = True
		visited_cells.append(cell)
		print(f"Visiting: {cell}")
		cell_stack.append(cell)


	to_visit_cell = cells[0]
	while (len(visited_cells) <= maze_size[0]*maze_size[1]):
		
		visit(to_visit_cell)
		not_visited_neighbors = [cell for cell in to_visit_cell.get_neighbors() if not cell.visited]
		
		if len(not_visited_neighbors) > 0:
			next_cell = random.choice(not_visited_neighbors)
			to_visit_cell.make_transition(next_cell)
			to_visit_cell = next_cell
		else:
			cell_stack.pop()
			to_visit_cell = cell_stack[-1]
	
	for cell in cells:
		neighbors = cell.get_neighbors()

		for n in neighbors:
			if n in cell.transitions:

				if n.x > cell.x and n.y == cell.y:
					cell.wall_positions.pop(Direction.E)
				elif n.x == cell.x and n.y > cell.y:
					cell.wall_positions.pop(Direction.S)
				elif n.x < cell.x and n.y == cell.y:
					cell.wall_positions.pop(Direction.W)
				elif n.x == cell.x and n.y < cell.y:
					cell.wall_positions.pop(Direction.N)


	print_cells()
	print()
	print_transitions()

	print()
	print(visited_cells)

	draw_maze(cells)



if __name__ == '__main__':
	main()