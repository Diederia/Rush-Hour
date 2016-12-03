import time
import Queue
import grid
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


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
    archive = set()
    came_from = dict()
    cost = dict()
    path = list()
    came_from[game] = None
    cost[game] = 0
    start = time.clock()
    counter = 0
    while not queue.empty():
        # board, cost, depth = queue.get()
        board = queue.get()
        # print board
        # print queue

        if board.solved():
            path = reconstruct_path(came_from, game, board)
            end = time.clock()
            end_time = end - start
            return path, end_time

        for move in board.getMoves():
            new_cost = cost[board] + 1
            if move not in cost or new_cost < cost[move]:
                # counter +=1
                # print counter
                cost[move] = new_cost
                priority = new_cost + board.advancedHeuristic(move) + board.fromGoal(move)
                print priority
                queue.put(move, priority)
                came_from[move] = board

    return 'No solution found!'
"""
http://www.redblobgames.com/pathfinding/a-star/implementation.html

Wat te doen, archief maken voor de astar
"""
