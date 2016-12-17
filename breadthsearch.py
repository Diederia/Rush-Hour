'''
    File description:
    This file contains the implementation of the breadth first search algorithm. 
    The breadth first search algorithm is an exhaustive search algorithm. 
    It finds the shortest path towards the goal (if there is one). 
    Implementation is based on Rush Hour puzzles.  
'''

import time
from collections import deque
import grid

def bfs(game, max_depth):
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
    moves = []
    solution = list()
    queue = deque()
    queue.appendleft((game, tuple()))
    start = time.clock()

    # Dequeue element from queue if there are elements left
    while len(queue) != 0:
        board, path = queue.pop()
        new_path = path + tuple([board])

        # Checks if maximum depht isn't exceeded 
        depth = len(new_path)
        # print"Depth:"
        # print depth
        if depth >= max_depth:
            break

        # Checks if the board is solved
        if board.solved():
            solution.append(new_path)
            end = time.clock()
            end_time = end - start
            return solution, end_time
        # Get every possible move from current board configuration
        else:
            moves = board.getMoves()
            queue.extendleft((move, new_path) for move in moves)

    end_time = 0
    return solution, end_time
