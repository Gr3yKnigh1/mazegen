from __future__ import annotations
import pygame
from generator import Cell
from generator import generate_maze



def render_cells(
        surface: pygame.Surface,
        cells: list[list[Cell]],
        render_position: tuple[int, int],
        cell_size: tuple(int, int), interval: tuple[int, int]) -> None:

    for cr in cells:
        for cc in cr:
            pygame.draw.rect(
                surface, (120, 50, 50), pygame.Rect(
                    render_position[0] + cc.tile_x * (cell_size[0] + interval[0]),
                    render_position[1] + cc.tile_y * (cell_size[1] + interval[1]),
                    cell_size[0],
                    cell_size[1]
                )
            )


def main() -> int:
    pygame.init()

    screen_surface = pygame.display.set_mode((900, 600))
    is_running = True

    clean_color = (50, 50, 50)

    cells = generate_maze(10, 10, (0, 0))

    while is_running:

        keys = pygame.key.get_pressed()
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and keys[pygame.K_LCTRL]:
                pygame.event.post(
                    pygame.event.Event(pygame.QUIT)
                )

        screen_surface.fill(clean_color)
        render_cells(
            screen_surface, cells, (4, 4), (50, 50), (4, 4)
        )
        pygame.display.flip()

    pygame.quit()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("KeyboardInterrupt...")
        raise SystemExit(0)
