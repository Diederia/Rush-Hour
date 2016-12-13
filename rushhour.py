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

def load_file(csv_file):
    """
    Loads in a csv file and places the vehicles on a grid

    rushhour_file: one of the seven possible board configurations
    n: int representing the size (length and width) of the chosen board

    Returns: a Grid object representing the chosen board
    """

    vehicles = []
    with open(csv_file, 'rb') as csv_open_file:
        reader = csv.reader(csv_open_file)
        for row in reader:
            if len(row) != 1:
                name, x, y, orientation, length = row
                vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))
            else:
                n = int(row[0])
    return Grid(set(vehicles), n)

def solution_steps(solution):
    """
    Generate list of steps to the solution

    results: ??

    Returns: an array of moves that lead to the solution
    """

    steps = []
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

def visualize(solution):
    """
    Simulation of the different steps on the board that lead to
    the solution from a breadth search algorithm.

    results: ??

    Returns: ??
    """
    # os.system('clear')
    # print solution[0][0]
    # time.sleep(5)
    os.system('clear')
    for i in range (len(solution[0]) - 1):
        print (solution[0][i])
        time.sleep(.1)
        os.system('clear')
    print solution[0][i + 1]
    return 'Rush hour board is Completed! The solution steps are displayed below:'

def main():
    global exit_x
    global exit_y
    global n

    if len(sys.argv) != 3:
        print "Usage example: python Boards/board.csv algorithm filename.py"

    csv_file = sys.argv[1]
    algorithm = sys.argv[2]

    game = load_file(csv_file)

    if algorithm == 'astar':
        path, end_time = a_star_search(game)

        solution = [path[1:]]
        print visualize(solution)
        print 'Solution steps: {0}'.format(', '.join(solution_steps(solution)))
    elif algorithm == 'bfs':
        solution, end_time = bfs(game, 10000)
        print visualize(solution)
        print 'Solution steps: {0}'.format(', '.join(solution_steps(solution)))
    elif algorithm == 'beamsearch':
        solution, end_time = beamSearch(game, 1000)
    else:
        print 'Please enter astar or bfs'

    print 'Time to find solution of the board: {0}'.format(end_time) + '.'

if __name__ == '__main__':
    # main()
    cProfile.run('main()')
#
