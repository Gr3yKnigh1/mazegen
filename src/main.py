from __future__ import annotations
import pygame

from generator import generate_maze
from renderer import MazeRendererContext
from renderer import render_cells


def main() -> int:
    pygame.init()

    screen_surface = pygame.display.set_mode((900, 600))
    is_running = True

    clean_color = (50, 50, 50)

    maze_size = (10, 10)
    first_cell_pos = (0, 0)

    cells = generate_maze(*maze_size, first_cell_pos)
    ctx = MazeRendererContext(screen_surface, (4, 4), (50, 50), (0, 0), 1)

    while is_running:

        keys = pygame.key.get_pressed()
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and keys[pygame.K_LCTRL]:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif event.key == pygame.K_r and keys[pygame.K_LCTRL]:
                cells = generate_maze(*maze_size, first_cell_pos)

        screen_surface.fill(clean_color)
        render_cells(cells, ctx)
        pygame.display.flip()

    pygame.quit()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("KeyboardInterrupt...")
        raise SystemExit(0)
