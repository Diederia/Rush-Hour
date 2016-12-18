'''
    File description:

'''

import grid
import time as clock
from collections import deque

def bfs(game):
    """
    This function starts an breadth first search algorithm finding the optimal
    solution for the rush hour board given to it.

    game: the initial rush hour board
    max_depth: an integer representing the maximum amount of moves can be made
    before the solution is found. If you fill in nothing this will be 1000.

    Returns: a list representing the solution and the end time in seconds it
    took the algorithm to find the solution. If there is no solution found,
    it will alert the user this board has no solution.
    """
    solution = list()
    queue = deque()
    queue.appendleft((game, tuple()))
    start_time = clock.clock()

    # Dequeue element from queue if there are elements left
    while len(queue) != 0:
        grid, path = queue.pop()
        new_path = path + tuple([grid])

        # Checks if the board is solved
        if grid.solved():
            solution.append(new_path)
            end_time = clock.clock()
            time = end_time - start_time
            return solution, time
        # If board is not solved, get every possible move from current board
        else:
            board = grid.create_board(grid.vehicles)
            queue.extendleft((move, new_path) for move in grid.get_moves(board))

    end_time = 0
    return solution, end_time
