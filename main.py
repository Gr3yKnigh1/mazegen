import pygame
import random


MAZE_SIZE = 10, 10 # in cells
CELL_SIZE = 64, 64 # in pixels
WINDOW_SIZE = MAZE_SIZE[0] * CELL_SIZE[0], MAZE_SIZE[1] * CELL_SIZE[1]
WALL_COLOR = "#B95FD0"
BACKGROUND_COLOR = "#FCC4C4"
WALL_WIDTH = 1


class Direction:
	N = (0, -1)
	E = (+1, 0)
	S = (0, +1)
	W = (-1, 0)

	@staticmethod
	def get_opposite(direction):
		return [direction[0]//-1, direction[1]//-1]


Directions = [Direction.N, Direction.E, Direction.S, Direction.W]


class Cell(object):
	
	def __init__(self, x, y, maze):
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


	def __repr__(self):
		return f"<Cell {self.x}:{self.y}:{1 if self.visited else 0}>"


	def make_transition(self, cell):
		if cell not in self.transitions:
			self.transitions.append(cell)
			cell.make_transition(self)
			# cell.transitions.append(self)

			#--Removing Walls
			direction = self.maze.get_cell_direction(self, cell)
			# opposite_direction = Direction.get_opposite(direction)
			
			self.walls[direction] = None
			# cell.walls[opposite_direction] == None


	def get_neighbours(self):
		neighbours = []
		for direction in Directions:
			try:
				neighbour = self.maze.get_cell(self.x + direction[0], self.y + direction[1])
			except IndexError as e:
				continue

			neighbours.append(neighbour)

		return neighbours


	def draw(self, surface):
		for wall in self.walls.values():
			if wall != None:
				pygame.draw.line(surface, pygame.Color(WALL_COLOR), *wall, WALL_WIDTH)


class Maze(object):
	
	def __init__(self, size):
		self.size = size
		self.cells = []

		self.start_position = (0, 0)


	def __repr__(self):
		string = ""
		for cell in self.cells:
			if cell.x == self.size[0] - 1:
				string += repr(cell) + "\n"
			else:
				string += repr(cell) + " "

		return string


	def add(self, cell: Cell):
		if cell not in self.cells:
			self.cells.append(cell)
		else:
			cells_repr = repr(self.cells)[0:50] + "..." if len(repr(self.cells)) > 51 else self.cells
			raise ValueError(f"{cell} already added in Maze {cells_repr}")


	def get_cell(self, x, y):
		if x < 0 or y < 0 or x > self.size[0]-1 or y > self.size[1]-1:
			raise IndexError(f"Out of range coordinates: x: {x}, y: {y}. Size: {self.size}")

		for cell in self.cells:
			if (cell.x, cell.y) == (x, y):
				return cell
		print(x, y)
		

	def get_cell_direction(self, c1, c2):
		neighbours = c1.get_neighbours()

		if c2 not in neighbours:
			return None

		for direction in Directions:
			if (c1.x + direction[0], c1.y + direction[1]) == (c2.x, c2.y):
				return direction


	def generate(self):
		#--Add new Cells
		self.cells.clear()

		for row in range(self.size[1]):
			for col in range(self.size[0]):
				self.add(Cell(col, row, self))

		#--Setting up
		to_visit = self.get_cell(*self.start_position)
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


	def draw(self, surface):
		for cell in self.cells:
			cell.draw(surface)



class Application(object):

	def __init__(self, window_size, fullscreen, caption, fps_limit):
		pygame.init()
		
		self.screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN if fullscreen else 0)
		self.clock = pygame.time.Clock()
		
		pygame.display.set_caption(caption)
		
		self.fps_limit = fps_limit
		self.run = True


	def setup(self):
		self.maze = Maze(MAZE_SIZE)
		self.maze.generate()

		# print(self.maze)

		# print(
		# 	self.maze.get_cell_direction(
		# 		self.maze.get_cell(0, 1),
		# 		self.maze.get_cell(0, 0)
		# 		)

		# 	)

		# for cell in self.maze.cells:
		# 	print(f"{cell}:")
		# 	for direction, wall in cell.walls.items():
		# 		print(f"-> {direction} : {wall}")

		# 	print(f"-> Transitions: {cell.transitions}")
		# 	print()


	def stop(self):
		self.run = False


	def mainloop(self):
		
		bg_color = pygame.Color(BACKGROUND_COLOR)
		while (self.run):
			dt = self.clock.tick(self.fps_limit) / 1000.0

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.stop()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_r:
						self.maze.generate()
					elif event.key == pygame.K_ESCAPE:
						self.stop()

			self.screen.fill(bg_color)
			self.maze.draw(self.screen)

			pygame.display.flip()


def main():
	app = Application(WINDOW_SIZE, False, "Maze Generator Version 0.2", 60)
	app.setup()
	app.mainloop()
	app.stop()


if (__name__ == '__main__'):
	main()
