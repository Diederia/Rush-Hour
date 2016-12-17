import time
import Queue
import grid
import heapq

def reconstruct_path(came_from, start, goal):
    """
    EXPLANATION

    came_from:
    start:
    goal:

    Returns: ??
    """
    current = goal
    path = [current]
    # comment
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)
    path.reverse()
    return path

# path is came from
def a_star_search(game):
    """
    This function starts an A* alogrithm finding the optimal
    solution for the rush hour board given to it.

    game: the initial rush hour board

    Returns: a list representing the path to the solution and the end time
    in seconds it took the algorithm to find the solution.
    If there is no solution found, it will alert the user this board has no solution.
    """
    queue = Queue.PriorityQueue()
    queue.put(game, 0)
    came_from = dict()
    cost = dict()
    path = list()
    came_from[game] = None
    cost[game] = 0
    start = time.clock()
    counter = 0

    #comment
    while not queue.empty():
        board = queue.get()

        # comment
        if board.solved():
            path = reconstruct_path(came_from, game, board)
            end = time.clock()
            end_time = end - start
            return path, end_time

        # comment
        for move in board.getMoves():
            #comment
            new_cost = cost[board] + 1

            if move not in cost or new_cost < cost[move]:
                cost[move] = new_cost
                boardFromMove = move.createBoard(move.vehicles)
                priority = new_cost + fromGoal(move, boardFromMove) + advancedHeuristic2(move, boardFromMove)
                print priority
                queue.put(move, priority)
                came_from[move] = board

    end_time = 0
    return solution, end_time

"""
http://www.redblobgames.com/pathfinding/a-star/implementation.html
"""

def blockerEstimate(move, boardFromMove):
    """
    Checks how many vehicles are standing in front of the (red) target car

    move: Grid object of the current situation

    Returns: an integer that represents the amount of vehicles blocking the
    (red) target car
    """
    board = boardFromMove
    score = 0
    for i in range(move.n):
        currentPlace = board[move.exit_y][move.n - (i + 1)]
        if currentPlace != 'x':
            if currentPlace != ' ':
                score += 2
        else:
            return score


def fromGoal(move, boardFromMove):
    """
    Checks how many steps away the (red) target car is from the exit

    move: Grid object of the current situation

    Returns: an integer that represents the amount of moves the (red)
    target car needs to make before it is at the exit position
    """
    board = boardFromMove
    score = 0
    for i in range(move.n):
        currentPlace = board[move.exit_y][move.n - (i + 1)]
        if currentPlace == 'x':
            return score
        else:
            score += 1

def advancedHeuristic2(move, boardFromMove):
    """
    Twee soorten, 1 voor de boards van 6x6 en 1 voor de grotere boards.
    Dit komt doordat je anders niet meer in de range van het board ben met checken.

    move: Grid object of the current situation

    Returns: an integer
    """
    print move
    vistedVehicles = set()
    board = boardFromMove
    score = 0
    for i in range(move.n):
        currentPlace = board[move.exit_y][move.n - (i + 1)]
        if currentPlace != ' ' and currentPlace != 'x':
            name = currentPlace
            while move.isVehicleBlocked(name, boardFromMove, vistedVehicles) != False:
                name, vistedVehicles = move.isVehicleBlocked(name, boardFromMove, vistedVehicles)
                score+= 1
    print"score!"
    print score
    return score
