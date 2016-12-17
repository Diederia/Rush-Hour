'''
    File description:
    This file contains the implementation of an A* algorithm, 
    based on the Rush Hour puzzle. The goal of this algorithm is 
    to find the shortest path to the solution possible. 
    
    Part of the implementation is cited from: 
    http://www.redblobgames.com/pathfinding/a-star/implementation.html
'''

import time
import Queue
import grid
import heapq

def reconstruct_path(came_from, start, goal):
    """
    Starting from the goal situation, it finds it parent till the start situation is
    reached.

    came_from: ?? 
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
    return path

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

    # Get board configuration out of the queue till non is left
    while not queue.empty():
        board = queue.get()

        # Checks if the board is solved
        if board.solved():
            # If sovled it reconstructs the path and time to calculate the solution
            path = reconstruct_path(came_from, game, board)
            end = time.clock()
            end_time = end - start
            return path, end_time

        # Get every move possible from a certain board configuration
        for move in board.getMoves():
            # Every step has a cost of 1 
            new_cost = cost[board] + 1
            
            # Calculate the costs of a move through heuristics. The costs define the priority of a board. 
            if move not in cost or new_cost < cost[move]:
                cost[move] = new_cost
                boardFromMove = move.createBoard(move.vehicles)
                priority = new_cost + fromGoal(move, boardFromMove) + advancedHeuristic2(move, boardFromMove)
                print priority
                queue.put(move, priority)
                came_from[move] = board

    end_time = 0
    return solution, end_time

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
    EXPLANATION. 

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
