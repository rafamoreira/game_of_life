import pygame
import time
from game_of_life import (
    check_neighbors,
    FPS,
    setup,
)

pygame.init()
WINDOW_SIZE = (1000, 1000)
screen = pygame.display.set_mode(WINDOW_SIZE)

SQUARE_SIZE = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_grid(grid: list[list[int]]) -> None:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = BLACK if cell == 0 else WHITE
            pygame.draw.rect(
                screen,
                color,
                [j*SQUARE_SIZE, i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE],
            )


def main() -> None:
    current_grid, next_grid = setup()

    while True:
        for i in range(0, len(current_grid)):
            for j in range(0, len(current_grid[i])):
                check_neighbors(current_grid, next_grid, i, j)

        draw_grid(current_grid)

        pygame.display.flip()

        current_grid, next_grid = next_grid, current_grid

        time.sleep(1.0 / FPS)


if __name__ == '__main__':
    main()
