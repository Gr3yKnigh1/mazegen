from __future__ import annotations
import dataclasses
import pygame

from cell import Cell
from common.direction import Direction


@dataclasses.dataclass
class MazeRendererContext:

    surface: pygame.Surface
    render_position: tuple[int, int]
    cell_size: tuple[int, int]
    cell_interval: tuple[int, int]
    wall_width: int


def get_cell_rect(cell: Cell, ctx: MazeRendererContext) -> pygame.Rect:
    return pygame.Rect(
        ctx.render_position[0] + cell.tile_x * (ctx.cell_size[0] + ctx.cell_interval[0]),
        ctx.render_position[1] + cell.tile_y * (ctx.cell_size[1] + ctx.cell_interval[1]),
        ctx.cell_size[0],
        ctx.cell_size[1]
    )


def render_cells(cells: list[list[Cell]], ctx: MazeRendererContext) -> None:
    for cell_row in cells:
        for cell in cell_row:
            pygame.draw.rect(
                ctx.surface, (120, 50, 50), get_cell_rect(cell, ctx)
            )
            render_walls(cell, ctx)  


def render_walls(cell: Cell, ctx: MazeRendererContext) -> None:
    for wall_direction in cell.wall_directions:
        render_wall(cell, wall_direction, ctx)


def render_wall(cell: Cell, direction: tuple[int, int], ctx: MazeRendererContext) -> None:
    rect = get_cell_rect(cell, ctx)

    if direction == Direction.UP:
        x1, y1 = rect.topleft
        x2, y2 = rect.topright
    elif direction == Direction.DOWN:
        x1, y1 = rect.bottomleft
        x2, y2 = rect.bottomright
    elif direction == Direction.RIGHT:
        x1, y1 = rect.topright
        x2, y2 = rect.bottomright
    elif direction == Direction.LEFT:
        x1, y1 = rect.topleft
        x2, y2 = rect.bottomleft

    pygame.draw.line(
        ctx.surface, (190, 50, 90), (x1, y1), (x2, y2), ctx.wall_width
    )


# def render_path(path: list[tuple[int, int]], ctx: MazeRendererContext, first_cell_pos: tuple[int, int]) -> None:
#     cell = Cell(
#         *first_cell_pos
#     )
#     for move in path:
#         rect1 = get_cell_rect(cell, ctx)
#         next_cell = Cell(
#             tile_x=cell.tile_x + move[0],
#             tile_y=cell.tile_y + move[1])
#         rect2 = get_cell_rect(next_cell, ctx)

#         pygame.draw.line(
#             ctx.surface, (255, 200, 190), rect1.center, rect2.center
#         )
#         cell = next_cell
