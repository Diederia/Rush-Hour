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

    # while the queue is not empty, get a child from the queue
    while len(queue) != 0:
        board, path = queue.pop()
        new_path = path + tuple([board])

        #
        if len(new_path) >= max_depth:
            break

        # check if the board is in archive, to avoid infinite loops
        if board in archive:
            continue
        else:
            archive.add(board)

        # check if the child is a solved board
        if board.solved():
            print new_path
            solution.append(new_path)
            end = time.clock()
            end_time = end - start
            return solution, end_time

        # if it is not solved, extend the queue with all the childs of current board
        else:
            queue.extendleft((move, new_path) for move in board.getMoves())
    return 'No solution found!'
