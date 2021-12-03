directions = (
    (0, -1),
    (0, +1),
    (-1, 0),
    (+1, 0),
)


class Direction:
    UP = directions[0]
    DOWN = directions[1]
    LEFT = directions[2]
    RIGHT = directions[3]


def opposite(direction: tuple[int, int]) -> tuple[int, int]:
    return -direction[0], -direction[1]
