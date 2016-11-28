# http://www.redblobgames.com/pathfinding/a-star/implementation.html
from grid import *

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, game):
    frontier = PriorityQueue()
    frontier.add(game, 0)
    came_from = {}
    cost_so_far = {}
    came_from[game] = None
    cost_so_far[game] = 0

    while not frontier.empty():
        current = frontier.get()

        # how do you use solved?
        if current == board.solved():
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, game, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start) # optional
    path.reverse() # optional
    return path
