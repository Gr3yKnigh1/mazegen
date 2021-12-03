from __future__ import annotations

import random

from cell import Cell
from common.direction import directions
from common.direction import opposite


def generate_maze(rows: int, cols: int, first_cell_pos: tuple[int, int]) -> list[list[Cell]]:

    cells = get_empty_maze(rows, cols)

    stack: list[Cell] = [
        cells[first_cell_pos[1]][first_cell_pos[0]]
    ]
    visited: list[Cell] = []

    current_cell = stack[0]

    while len(visited) < rows * cols:

        if current_cell not in visited:
            visited.append(current_cell)

        not_visited_neighbours = get_not_visited_neighbours(
            cells, current_cell, visited
        )
        
        if len(not_visited_neighbours) == 0:
            current_cell = stack.pop()
        else:
            next_cell = random.choice(not_visited_neighbours)
            stack.append(next_cell)
            current_cell, next_cell = remove_wall_between(current_cell, next_cell)
            current_cell = next_cell

    return cells


def remove_wall_between(c1: Cell, c2: Cell) -> tuple[Cell, Cell]:
    d1 = c2.tile_x - c1.tile_x, c2.tile_y - c1.tile_y 
    d2 = opposite(d1)
    c1.wall_directions = remove_wall_in_direction(c1, d1)
    c2.wall_directions = remove_wall_in_direction(c2, d2)

    return c1, c2


def remove_wall_in_direction(cell: Cell, direction: tuple[int, int]) -> list[tuple[int, int]]:
    return [
        wall_d for wall_d in cell.wall_directions if wall_d != direction
    ]


def get_not_visited_neighbours(cells: list[list[Cell]], cell: Cell, visited: list[Cell]) -> list[Cell]:
    return [
        neighbour for neighbour in get_cell_neighbour(cells, cell) if neighbour not in visited
    ] 


def get_empty_maze(r: int, c: int) -> list[list[Cell]]:
    return [[Cell(j, i) for j in range(c)] for i in range(r)]


def get_cell_neighbour(cells: list[list[Cell]], cell: Cell) -> list[Cell]:
    neighbours = []
    x, y = cell.tile_x, cell.tile_y

    for direction in directions:
        dx, dy =  direction
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
