from common.direction import directions


class Cell(object):

    tile_x: int
    tile_y: int
    wall_directions: list[tuple[int, int]]

    def __init__(self, tile_x, tile_y, wall_directions=None) -> None:
        if wall_directions is None:
            self.wall_directions = [direction for direction in directions]
        self.tile_x = tile_x
        self.tile_y = tile_y
