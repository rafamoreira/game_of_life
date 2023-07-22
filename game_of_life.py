# Conway's Game of Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Rules:
# 1. Any live cell with fewer than two live neighbours dies by the underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next
# generation.
# 3. Any live cell with more than three live neighbours dies, as if by
# overpopulation.

# A pure Python implementation of Conway's Game of Life.
# Not optimized for speed or memory usage.
# Meant as an example of how to use Python to implement a cellular automaton.
# It doesn't use any external libraries, and what you see is what you get.
# The grid is a 2D array of integers. 0 means dead, 1 means alive.
# The grid is initialized with a few live cells.
# The grid is printed on the console.
# The grid is updated according to the rules of Conway's Game of Life.
# The grid is printed to the console again.
# The grid is updated again.
# The grid is printed to the console again.
# The grid is updated again.
# The grid is printed to the console again.
# I think you get the idea.

import random
import time

GRID_SIZE_X: int = 120
GRID_SIZE_Y: int = 20
FPS: int = 5


def create_grid() -> list[list[int]]:
    x: int = GRID_SIZE_X
    y: int = GRID_SIZE_Y
    return [[0 for _ in range(0, x)] for _ in range(0, y)]


def check_neighbors(
    grid: list[list[int]],
    next_gen_grid: list[list[int]],
    row: int,
    column: int,
) -> None:
    offsets: list[tuple[int, int]] = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    # count living neighbors
    count = 0

    for o_x, o_y in offsets:
        if 0 <= row+o_x < len(grid) and 0 <= column+o_y < len(grid[row]):
            count += grid[row+o_x][column+o_y]

    if count < 2 or count > 3:
        next_gen_grid[row][column] = 0
    elif count == 3:
        next_gen_grid[row][column] = 1
    else:
        next_gen_grid[row][column] = grid[row][column]


def populate_grid(grid: list[list[int]]) -> None:
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            grid[i][j] = random.randint(0, 1)


def print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        print(' '.join(map(str, row)).replace('0', '.').replace('1', '#'))


def wait_for_next_frame(previous_frame_time: float) -> float:
    next_frame_time = previous_frame_time + 1.0 / FPS
    while time.time() < next_frame_time:
        time.sleep(next_frame_time - time.time())

    return next_frame_time


def main() -> None:
    grid1 = create_grid()
    grid2: list[list[int]] = create_grid()

    populate_grid(grid1)
    current_grid: list[list[int]] = grid1
    next_grid: list[list[int]] = grid2

    print_grid(current_grid)
    frame_time = time.time()

    while True:
        for i in range(0, len(current_grid)):
            for j in range(0, len(current_grid[i])):
                check_neighbors(current_grid, next_grid, i, j)

        print_grid(next_grid)
        current_grid, next_grid = next_grid, current_grid
        print('\n\n')
        frame_time = wait_for_next_frame(frame_time)


main()
