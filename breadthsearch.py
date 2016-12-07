# Rush Hour Breadth search algorithm
# Diederick, Valentijn en Jill
import time
from collections import deque
import grid

def bfs(game, max_depth = 1000):
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
    archive = set()
    solution = list()
    queue = deque()
    queue.appendleft((game, tuple()))
    start = time.clock()

    # comment
    while len(queue) != 0:
        board, path = queue.pop()
        new_path = path + tuple([board])

        # comment
        if len(new_path) >= max_depth:
            break

        # comment
        if board in archive:
            continue
        else:
            archive.add(board)

        # comment
        if board.solved():
            print new_path
            solution.append(new_path)
            end = time.clock()
            end_time = end - start
            return solution, end_time

        # comment
        else:
            queue.extendleft((move, new_path) for move in board.getMoves())
    return 'No solution found!'
