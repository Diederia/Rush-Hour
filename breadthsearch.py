# Rush Hour Breadth search algorithm
# Diederick, Valentijn en Jill
import time
from collections import deque
import grid

def bfs(game, max_depth):
    """

    Arguments:
        Game : A RushHour board.

    Keyword Arguments:
        max_depth: 1000
    """
    archive = set()
    solution = list()
    queue = deque()
    queue.appendleft((game, tuple()))
    start = time.clock()
    while len(queue) != 0:
        board, path = queue.pop()
        new_path = path + tuple([board])

        if len(new_path) >= max_depth:
            break

        if board in archive:
            continue
        else:
            archive.add(board)

        if board.solved():
            solution.append(new_path)
            end = time.clock()
            end_time = end - start
            return solution, end_time
        else:
            queue.extendleft((move, new_path) for move in board.getMoves())
    return 'No solution found!'
