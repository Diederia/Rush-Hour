'''
    File description: This file contains the implementation of an breadth first
    search algorithm, based on the Rush Hour puzzle. The goal of this algorithm
    is to find the shortest path to the solution possible.
'''

import grid
import time as clock
from collections import deque

def bfs(start):
    """This function starts an breadth first search algorithm finding the optimal
    solution for the rush hour board given to it.

    start: the initial rush hour board.

    Returns: a list representing the solution and the end time in seconds it
    took the algorithm to find the solution. If there is no solution found,
    it will alert the user this board has no solution.
    """
    came_from = dict()
    queue = deque()
    queue.appendleft(start)
    start_time = clock.clock()
    visited_nodes = 0
    cost = 0

    # Dequeue element from queue if there are elements left
    while len(queue) != 0:
        grid = queue.pop()
        visited_nodes += 1

        if grid.solved():
            # If sovled calculate time to solve the game
            end_time = clock.clock()
            time = end_time - start_time
            return came_from, grid, time, visited_nodes

        # If board is not solved, get every possible move from current board
        for move in grid.get_moves():
            came_from[move] = grid, cost
            queue.extendleft([move])

    time = 0
    return came_from, grid, time, visited_nodes
