from __future__ import annotations

import sys
import random
import pygame

from app import MazeGenApp


WINDOW_SIZE = MAZE_SIZE[0] * CELL_SIZE[0], MAZE_SIZE[1] * CELL_SIZE[1]


def main() -> int:
	app = MazeGenApp(WINDOW_SIZE)
	app.mainloop()
	return 0


if __name__ == '__main__':
	sys.exit(main())
