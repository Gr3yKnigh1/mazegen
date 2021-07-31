from __future__ import annotations

import sys

from app import MazeGenApp
from consts import WINDOW_SIZE


def main() -> int:
	app = MazeGenApp(WINDOW_SIZE)
	app.run()
	return 0


if __name__ == '__main__':
	sys.exit(main())
