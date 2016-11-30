import queue

def blockerEstimate(board):
    vehiclesBocking = 0
    for i in range(n):
        currentPlace = board[y_exit][n - (i + 1)]
        while currentPlace != 'x':
            if currentPlace != ' ':
                vehiclesBocking += 1
    return vehiclesBocking

def a_star_search(game):
    queue = queue.PriorityQueue()
    queue.put(game, 0)
    archive = set()
    path = dict()
    cost = dict()
    path[game] = None
    cost[game] = 0

    while len(queue) != 0:
        board, cost, depth = queue.get()

        if board in archive:
            continue
        else:
            archive.add(board)

        if board.solved():
            solution.append(PATH)
            end = time.clock()
            end_time = end - start
            return solution, end_time

        for move in board.getMoves():
            new_cost = cost[board] + 1
            if move not in cost or new_cost < cost[move]:
                cost[move] = new_cost
                priority = new_cost + blockerEstimate(move)
                queue.add(move, priority)

"""
http://www.redblobgames.com/pathfinding/a-star/implementation.html

Wat te doen, archief maken voor de astar
"""
