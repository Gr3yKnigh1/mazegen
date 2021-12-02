from common.direction import Direction


class Cell(object):

    tile_x: int
    tile_y: int
    wall_directions: list[Direction | None]

    def __init__(self, tile_x, tile_y, wall_directions=None) -> None:
        if wall_directions is None:
            self.wall_directions = [direction for direction in Direction]
        self.tile_x = tile_x
        self.tile_y = tile_y

    def __repr__(self) -> str:
        return f"<Cell [{self.tile_x},{self.tile_y}]>"
