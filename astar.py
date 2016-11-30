import time
import Queue
import grid

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)
    path.reverse()
    return path

# path is came from
def a_star_search(game):
    queue = Queue.PriorityQueue()
    queue.put(game, 0)
    # archive = set()
    came_from = dict()
    cost = dict()
    path = list()
    came_from[game] = None
    cost[game] = 0
    start = time.clock()

    while not queue.empty():
        # board, cost, depth = queue.get()
        board = queue.get()

        if board.solved():
            print 'done!'
            path = reconstruct_path(came_from, game, board)
            solution = 0
            # solution.append(PATH)
            end = time.clock()
            end_time = end - start
            return path, end_time
            # return reconstruct_path(path, game, solution), end_time

        for move in board.getMoves():
            new_cost = cost[board] + 1
            if move not in cost or new_cost < cost[move]:
                cost[move] = new_cost
                priority = new_cost + board.blockerEstimate(move) + board.fromGoal(move)
                queue.put(move, priority)
                came_from[move] = board

    return 'No solution found!'
"""
http://www.redblobgames.com/pathfinding/a-star/implementation.html

Wat te doen, archief maken voor de astar
"""
