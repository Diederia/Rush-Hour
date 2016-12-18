'''
    File description:

'''

import grid
import time as clock
from collections import deque

def bfs(start):
    """
    This function starts an breadth first search algorithm finding the optimal
    solution for the rush hour board given to it.

    start: the initial rush hour board
    max_depth: an integer representing the maximum amount of moves can be made
    before the solution is found. If you fill in nothing this will be 1000.

    Returns: a list representing the solution and the end time in seconds it
    took the algorithm to find the solution. If there is no solution found,
    it will alert the user this board has no solution.
    """
    solution = list()
    came_from = dict()
    queue = deque()
    queue.appendleft(start)
    start_time = clock.clock()

    # Dequeue element from queue if there are elements left
    while len(queue) != 0:
        grid = queue.pop()

        if grid.solved():
            # If sovled calculate time to solve the game
            end_time = clock.clock()
            time = end_time - start_time
            return came_from, grid, time
        # If board is not solved, get every possible move from current board
        board = grid.create_board(grid.vehicles)
        for move in grid.get_moves(board):
            came_from[move] = grid
            queue.extendleft([move])

    end_time = 0
    return solution, end_time
