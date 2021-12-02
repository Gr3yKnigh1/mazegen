from __future__ import annotations
import enum


class Vector2Int(list):

    def __init__(self, x: int, y: int) -> None:
        self.extend((x, y))

    @property
    def x(self) -> int:
        return self[0]

    @property
    def y(self) -> int:
        return self[1]


class Direction(enum.Enum):
    UP = Vector2Int(-1, 0)
    DOWN = Vector2Int(+1, 0)
    LEFT = Vector2Int(0, -1)
    RIGHT = Vector2Int(0, +1)


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


def generate_maze(
        rows_count: int, columns_count: int, 
        first_cell_pos: tuple[int, int]) -> list[list[Cell]]:

    cells = get_empty_maze(rows_count, columns_count)

    # for c in range(columns_count):
    #     for r in range(rows_count):
    #         print(
    #             f"[{c},{r}] -> {get_cell_neighbour(cells, c, r)}"
    #         )

    return cells


def get_empty_maze(r: int, c: int) -> list[list[Cell]]:
    cells = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(
                Cell(j, i)
            )
        cells.append(row)
    return cells


def get_cell_neighbour(cells: list[list[Cell]], x: int, y: int) -> list[Cell]:
    neighbours = []

    for direction in Direction:
        dx, dy =  direction = direction.value
        nx, ny = dx + x, dy + y

        if (nx < 0) or (ny < 0) or (ny > len(cells) - 1) or (nx > len(cells[0]) - 1):
            continue

        try:
            neighbours.append(
                cells[ny][nx]
            )
        except IndexError as e:
            print(f"{dx=} {dy=}")
            print(f"{nx=} {ny=}")
            raise IndexError from e

    return neighbours
