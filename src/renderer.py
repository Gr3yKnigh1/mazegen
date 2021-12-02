from __future__ import annotations
import dataclasses
import pygame

from generator import Cell, Direction


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
    for direction in Direction:
        if direction not in cell.wall_directions:
            continue
        render_wall(cell, direction, ctx)


def render_wall(cell: Cell, direction: Direction, ctx: MazeRendererContext) -> None:
    rect = get_cell_rect(cell, ctx)

    match direction:
        case Direction.UP:
            x1, y1 = rect.topleft
            x2, y2 = rect.topright
        case Direction.DOWN:
            x1, y1 = rect.bottomleft
            x2, y2 = rect.bottomright
        case Direction.RIGHT:
            x1, y1 = rect.topright
            x2, y2 = rect.bottomright
        case Direction.LEFT:
            x1, y1 = rect.topleft
            x2, y2 = rect.bottomleft

    pygame.draw.line(
        ctx.surface, (190, 50, 90), (x1, y1), (x2, y2), ctx.wall_width
    )
