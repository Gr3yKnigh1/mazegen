from __future__ import annotations


class Direction(object):

	N = (0, -1)
	E = (+1, 0)
	S = (0, +1)
	W = (-1, 0)

	@staticmethod
	def get_opposite(direction):
		return [direction.x//-1, direction.y//-1]

Directions: list[tuple[int, int]] = [Direction.N, Direction.E, Direction.S, Direction.W]
