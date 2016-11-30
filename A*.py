import queue

def blockerEstimate(board):
    vehiclesBocking = 0
    for i in range(n):
        currentPlace = board[y_exit][n - (i + 1)]
        while currentPlace != 'x':
            if currentPlace != ' ':
                vehiclesBocking += 1
    return vehiclesBocking


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
    queue = queue.PriorityQueue()
    queue.put(game, 0)
    archive = set()
    path = dict()
    cost = dict()
    path[game] = None
    cost[game] = 0
    start = time.clock()

    while len(queue) != 0:
        # board, cost, depth = queue.get()
        board = queue.get()

        if board in archive:
            continue
        else:
            archive.add(board)

        if board.solved():
            solution.append(PATH)
            end = time.clock()
            end_time = end - start
            return reconstruct_path(path, game, solution), end_time

        for move in board.getMoves():
            new_cost = cost[board] + 1
            if move not in cost or new_cost < cost[move]:
                cost[move] = new_cost
                priority = new_cost + blockerEstimate(move)
                queue.add(move, priority)
    return 'No solution found!'
"""
http://www.redblobgames.com/pathfinding/a-star/implementation.html

Wat te doen, archief maken voor de astar
"""
