# Python implementation of Conway's game of life

## Conway's Game of Life
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

### Rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#### A pure Python implementation of Conway's Game of Life.
Not optimized for speed or memory usage.
###############################################################
# NO USE OF NUMPY OR ANY OTHER EXTERNAL LIBRARIES ON THE BASE # 
###############################################################
Meant as an example of how to use Python to implement a cellular automaton.
What you see is what you get.

The grid is a 2D array of integers. 0 means dead, 1 means alive.
The grid is initialized with a few live cells.
The grid is printed on the console.
The grid is updated according to the rules of Conway's Game of Life.
The grid is printed to the console again.
The grid is updated again.
The grid is printed to the console again.
The grid is updated again.
The grid is printed to the console again.
I think you get the idea.
