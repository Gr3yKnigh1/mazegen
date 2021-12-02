import pygame


def main() -> int:
    pygame.init()

    screen_surface = pygame.display.set_mode((900, 600))
    is_running = True

    clean_color = (50, 50, 50)

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
        pygame.display.flip()

    pygame.quit()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("KeyboardInterrupt...")
        raise SystemExit(0)
