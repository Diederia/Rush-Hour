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
    archive = set()
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
                priority = new_cost + board.advancedHeuristic(move) + board.fromGoal(move)
                queue.put(move, priority)
                came_from[move] = board

    return 'No solution found!'

"""
http://www.redblobgames.com/pathfinding/a-star/implementation.html
"""
