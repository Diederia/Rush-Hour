'''
    File description:
    This file contains the implementation of an A* algorithm,
    based on the Rush Hour puzzle. The goal of this algorithm is
    to find the shortest path to the solution possible.

    Part of the implementation is cited from:
    http://www.redblobstarts.com/pathfinding/a-star/implementation.html
'''
import grid
import heapq
import time as clock

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def a_star_search(start, heuristic):
    """
    This function starts an A* alogrithm finding the optimal
    solution for the rush hour board given to it.

    start: the initial rush hour board

    Returns: a list representing the path to the solution and the end time
    in seconds it took the algorithm to find the solution.
    If there is no solution found, it will alert the user this board has no solution.
    """
    queue = PriorityQueue()
    queue.put(start, 0)
    came_from = dict()
    cost = dict()
    path = list()
    came_from[start] = None
    cost[start] = 0
    start_time = clock.clock()
    visited_nodes = 0

    # Get board configuration out of the queue till non is left
    while not queue.empty():
        grid = queue.get()
        visited_nodes += 1

        # Checks if the board is solved
        if grid.solved():
            # If sovled calculate time to solve the game
            print visited_nodes
            end_time = clock.clock()
            time = end_time - start_time
            return came_from, grid, time

        # Get every move possible from a certain board configuration
        board_moves = grid.create_board(grid.vehicles)
        for move in grid.get_moves(board_moves):
            # Every step has a cost of 1
            new_cost = cost[grid] + 1

            # Calculate the costs (priority score) of a move through heuristics.
            if move not in cost or new_cost < cost[move]:
                board = move.create_board(move.vehicles)
                cost[move] = new_cost
                priority = new_cost + get_heuristic(heuristic, move, board)
                queue.put(move, priority)
                came_from[move] = grid


    time = 0
    return solution, time

def get_heuristic(heuristic, move, board):
    if heuristic == '1':
        return blocker_heuristic(move, board)
    elif heuristic == '2':
        return goal_heuristic(move, board)
    elif heuristic == '3':
        return advanced_heuristic(move, board)
    elif heuristic == '4':
        return blocker_heuristic(move, board) + goal_heuristic(move, board)
    elif heuristic == '5':
        return blocker_heuristic(move, board) + advanced_heuristic(move, board)
    elif heuristic == '6':
        return goal_heuristic(move, board) + advanced_heuristic(move, board)
    elif heuristic == '7':
        return blocker_heuristic(move, board) + goal_heuristic(move, board) + advanced_heuristic(move, board)
    else:
        print "Error with getting heuristic"

def blocker_heuristic(move, board):
    """ Checks how many vehicles are standing in front of the (red) target car

    move: Grid object of the current situation

    Returns: an integer that represents the amount of vehicles blocking the
    (red) target car
    """
    score = 0

    # Checks right to left at hight of exit y how many vehicles are blocking
    for i in range(move.n):
        current_place = board[move.exit_y][move.n - (i + 1)]
        if current_place != 'x':
            if current_place != ' ':
                score += 3
        else:
            return score


def goal_heuristic(move, board):
    """ Checks how many steps away the (red) target car is from the exit

    move: Grid object of the current situation

    Returns: an integer that represents the amount of moves the (red)
    target car needs to make before it is at the exit position
    """
    score = 0

    # Checks right to left at hight of exit y how far target car is from exit
    for i in range(move.n):
        current_place = board[move.exit_y][move.n - (i + 1)]
        if current_place == 'x':
            return score
        else:
            score += 1

def advanced_heuristic(move, board):
    """Checks if there is a vehcile standing in front of the (red) target car.
    If so, checks if the vehicle is blocked again and goes on until it finds
    a moveable vehicle.

    move: Grid object of the current situation

    Returns: an integer
    """
    visted_vehicles = set()
    score = 0
    # Checks right to left at hight of exit y if there is a vehicles is blocking
    for i in range(move.n):
        current_place = board[move.exit_y][move.n - (i + 1)]
        if current_place != ' ' and current_place != 'x':
            name = current_place
            # Go on until a moveable vehicle
            while move.is_vehicle_blocked(name, board, visted_vehicles) != None:
                score+= 1

                name, visted_vehicles = move.is_vehicle_blocked(name, board, visted_vehicles)
    return score
