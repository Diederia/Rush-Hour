import cProfile
import sys
import csv
import os
import time
from vehicle import Vehicle
from breadthsearch import *
from grid import *
from astar import *
from beamsearch import *

def load_file(csv_file, n):
    """
    Loads in a csv file and places the vehicles on a grid

    rushhour_file: one of the seven possible board configurations
    n: int representing the size (length and width) of the chosen board

    Returns: a Grid object representing the chosen board
    """
    vehicles = []

    # open the csv file
    with open(csv_file, 'rb') as csv_open_file:
        reader = csv.reader(csv_open_file)
        # read csv file row for row and save every row in the array vehicles
        for row in reader:
            name, x, y, orientation, length = row
            vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))

    # make an empty begin board with all spaces, size of n
    begin_board = [ [' '] * n for _ in range(n)]

    # place every vehicle on the board by looping through the vehicles array
    for vehicle in vehicles:
        x, y = vehicle.x, vehicle.y
        # if orientation is horizontal change the x coordinate
        if vehicle.orientation == 'h':
            for i in range(vehicle.length):
                begin_board[y][x + i] = vehicle.name
        # if orientation is vertical change the y coordinate
        else:
            for i in range(vehicle.length):
                begin_board[y + i][x] = vehicle.name
    # place result in a Grid object
    return Grid(set(vehicles), begin_board, n)

def solution_steps_bfs(solution):
    """
    Generate list of steps to the solution

    solution: ??

    Returns: an array of moves that lead to the solution
    """
    steps = []

    # comment
    for i in range(len(solution[0]) - 1):
        board1, board2 = solution[0][i], solution[0][i + 1]
        vehicle1 = list(board1.vehicles - board2.vehicles)[0]
        vehicle2 = list(board2.vehicles - board1.vehicles)[0]
        if vehicle1.x < vehicle2.x:
            steps.append('step %d: {0} right'.format(vehicle1.name) %i)
        elif vehicle1.x > vehicle2.x:
            steps.append('step %d: {0} left'.format(vehicle1.name) %i)
        elif vehicle1.y < vehicle2.y:
            steps.append('step %d: {0} down'.format(vehicle1.name) %i)
        elif vehicle1.y > vehicle2.y:
            steps.append('step %d: {0} up'.format(vehicle1.name) %i)
    return steps

def solution_steps_astar(solution):
    """
    Generate list of steps to the solution

    results: ??

    Returns: an array of moves that lead to the solution
    """    steps = []
    solution1 = solution[1:]
    for i in range(len(solution1) - 1):
        board1, board2 = solution1[i], solution1[i + 1]
        vehicle1 = list(board1.vehicles - board2.vehicles)[0]
        vehicle2 = list(board2.vehicles - board1.vehicles)[0]
        if vehicle1.x < vehicle2.x:
            steps.append('step %d: {0} right'.format(vehicle1.name) %i)
        elif vehicle1.x > vehicle2.x:
            steps.append('step %d: {0} left'.format(vehicle1.name) %i)
        elif vehicle1.y < vehicle2.y:
            steps.append('step %d: {0} down'.format(vehicle1.name) %i)
        elif vehicle1.y > vehicle2.y:
            steps.append('step %d: {0} up'.format(vehicle1.name) %i)
    return steps

def visualize_bfs(solution):
    """
    Simulation of the different steps on the board that lead to
    the solution from a breadth search algorithm.

    solution: ??

    Returns: ??
    """
    os.system('clear')
    print solution[0][0]
    time.sleep(5)
    os.system('clear')

    for i in range (len(solution[0]) - 1):
        print (solution[0][i])
        time.sleep(.1)
        os.system('clear')
    print solution[0][i + 1]
    return 'Rush hour board is Completed! The solution steps are displayed below:'


def visualize_astar(solution):
    """
    Simulation of the different steps on the board that lead to
    the solution from an A* algorithm.

    solution: ??

    Returns: ??
    """
    os.system('clear')
    for i in range (len(solution) - 1):
        print (solution[i])
        time.sleep(.1)
        os.system('clear')
    print solution[i + 1]
    print len(solution)
    return 'Rush hour board is Completed! The solution steps are displayed below:'

def main():
    global exit_x
    global exit_y
    global n

    if len(sys.argv) != 3:
        print "Usage example: python Boards/board.csv algorithm filename.py"

    csv_file = sys.argv[1]
    algorithm = sys.argv[2]

    if (csv_file == 'Boards/board1.csv' or csv_file == 'Boards/board2.csv'
        or csv_file == 'Boards/board3.csv'):
        n = 6
    elif (csv_file == 'Boards/board4.csv' or csv_file == 'Boards/board5.csv'
        or csv_file == 'Boards/board6.csv'):
        n = 9
    else:
        n = 12

    game = load_file(csv_file, n)

    if algorithm == 'astar':
        solution, end_time = a_star_search(game)
        # print visualize_astar(solution)
        print 'Solution steps: {0}'.format(', '.join(solution_steps_astar(solution)))
    elif algorithm == 'bfs':
        solution, end_time = bfs(game)
        print visualize_bfs(solution)
        solution, end_time = bfs(game, 10000)
        # print visualize_bfs(solution)
        print 'Solution steps: {0}'.format(', '.join(solution_steps_bfs(solution)))
    elif algorithm == 'beamsearch':
        solution, end_time = beamSearch(game, 1000)
    else:
        print 'Please enter astar or bfs'

    print 'Time to find solution of the board: {0}'.format(end_time) + '.'

if __name__ == '__main__':
    # main()
    cProfile.run('main()')
