'''
    File description:
    This file contains the implementation of an A* algorithm,
    based on the Rush Hour puzzle. The goal of this algorithm is
    to find the shortest path to the solution possible.

    Part of the implementation is cited from:
    http://www.redblobgames.com/pathfinding/a-star/implementation.html
'''
import grid
import Queue
import heapq
import time as clock


def reconstruct_path(came_from, start, goal):
    """Starting from the goal situation, it finds it parent till the start situation is
    reached.

    came_from: a dictionary with the move as key and grid as value.
    start: begin configuration of the board
    goal: situation where the red car stands next to the exit

    Returns: The steps it took from the start situation to the goal situation.
    """
    current = goal
    path = [current]

    # Append configuartion to board as a step until the begin situation is reached
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)
    path.reverse()
    return [path[1:]]

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
    start_time = clock.clock()
    counter = 0

    # Get board configuration out of the queue till non is left
    while not queue.empty():
        grid = queue.get()

        # Checks if the board is solved
        if grid.solved():
            # If sovled it reconstructs the path and time to calculate the solution
            solution = reconstruct_path(came_from, game, grid)
            end_time = clock.clock()
            time = end_time - start_time
            return solution, time

        # Get every move possible from a certain board configuration
        board_moves = grid.create_board(grid.vehicles)
        for move in grid.get_moves(board_moves):
            # Every step has a cost of 1
            new_cost = cost[grid] + 1

            # Calculate the costs (priority score) of a move through heuristics.
            if move not in cost or new_cost < cost[move]:
                board = move.create_board(move.vehicles)
                cost[move] = new_cost
                priority = new_cost + from_goal(move, board) + advanced_heuristic(move, board)
                queue.put(move, priority)
                came_from[move] = grid


    time = 0
    return solution, time

def blocker_estimate(move, board):
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
                score += 2
        else:
            return score


def from_goal(move, board):
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
