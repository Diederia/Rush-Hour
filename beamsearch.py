# Rush Hour Breadth search algorithm
# Diederick, Valentijn en Jill
import time as clock
from collections import deque
import grid

def beamSearch(game, max_depth):
    """

    Arguments:
        Game : A RushHour board.

    """
    solution = list()
    queue = deque()
    queue.appendleft((game, tuple()))
    start = time.clock()
    while len(queue) != 0:
        board, path = queue.pop()
        new_path = path + tuple([board])


        if len(new_path)%5 == 0:
            for moves in board.get_moves():
                cost = 10000
                new_cost = board.advancedHeuristic(moves) + board.fromGoal(moves)
                if new_cost <= cost:
                    new_board = moves
                    cost = new_cost
            board = new_board

        if board.solved():
            solution.append(new_path)
            end = clock.clock()
            end_time = end - start
            return solution, end_time
        else:
            queue.extendleft((move, new_path) for move in board.get_moves())

    end_time = 0
    return solution, end_time
