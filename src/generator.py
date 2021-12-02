from __future__ import annotations
from cell import Cell
from common.direction import Direction


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
