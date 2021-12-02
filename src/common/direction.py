import enum
from common.vector import Vector2Int


class Direction(enum.Enum):
    UP = Vector2Int(-1, 0)
    DOWN = Vector2Int(+1, 0)
    LEFT = Vector2Int(0, -1)
    RIGHT = Vector2Int(0, +1)
