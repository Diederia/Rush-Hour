# Rush Hour Breadth search algorithm
# Diederick, Valentijn en Jill

from collections import deque
from board import *
from rushhour import *

def algorithm(board, max_depth=100):
    """
    Use breadth first search algorithm to find a solution for Rush Hour.

    Arguments:
    begin_board: The begin position of the board wanting to solve
    max_depth: Least amount of steps to solve the rush hour puzzle
    """
    begin_board = Board(n, vehicles)
    archive = set()
    solution = list()
    queue = deque()
    queue.appendleft((begin_board, tuple()))
    while len(queue) != 0:

        # add begin board on the queue
        board, path = queue.pop()

        # make all children from current board state
        new_path = path + tuple([board])

        # stop if amount of moves is to much
        if len(new_path) >= max_depth:
            break

        if board in archive:
            continue
        else:
            archive.add(board)

        # check if board is already solved (yes? Stop and return)
        if board.solved():
            solution.append(new_path)
            return solution
        else:
            # add all children to the queue
            queue.extendleft((move, new_path) for move in board.getMoves())


def solution(solution):
    moves = []
    moves = solution
    # for i in range(len(solution)):
        # Get info if step is up,down,left,right

    return moves



# 3. Remove bovenste item van de queue (Leeg? Stop, geen oplossing)

# 4. Maak alle kinderen van dat item

# 5. Controleer of een kind al in het archief zit (Yes? Delete kind)

# 6. Controleer of de oplossing tussen er tussen zit (yes? Stop en return)

# 7. Add alle kinderen op de queue

# 8. ga naar 3
