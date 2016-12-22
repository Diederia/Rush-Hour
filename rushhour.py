'''
    File description:
    This file contains the main file in order to run the program.
'''

import cProfile
import sys
import csv
import os
import time
from vehicle import *
from breadthsearch import *
from grid import *
from astar import *

def main():
    # Error handling wrong command line from user
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print "Usage example: python rushhour.py Boards/board.csv algorithm"
        # exit()

    # Initializing variables matching correct csv file and algorithm
    csv_file = sys.argv[1]
    algorithm = sys.argv[2]
    if len(sys.argv) == 4:
        heuristic = sys.argv[3]

    # Unload csv file
    start = load_file(csv_file)

    # Running program on the right algorithm and showing results
    if algorithm == 'astar':
        came_from, goal, time, visited_nodes = a_star_search(start, heuristic)
        display_results(start, came_from, goal, time, visited_nodes)
    elif algorithm == 'bfs':
        came_from, goal, time, visited_nodes = bfs(start)
        display_results(start, came_from, goal, time, visited_nodes)
    else:
        print 'Please enter astar or bfs'

def load_file(csv_file):
    """Loads in a csv file with places of the vehicles on a grid and the dimension
    of the board (n).

    csv_file: One of the seven possible board configurations.
    The first line gives the size of the grid.
    The next lines give a description of the vehicles. First chararchter
    represents the name of the vehicle. The target car is alway named 'x'.
    The first two numbers are the coordinates of the upper left corner
    of the vehicle. The 'h' or 'v' represent the orientation and the last number
    is the size of the vehicle.

    Returns: a Grid object representing the chosen board.
    """
    vehicles = []
    # Opens the file and reads it row for row
    with open(csv_file, 'rb') as csv_open_file:
        reader = csv.reader(csv_open_file)
        for row in reader:
            # Reads in vehicles
            if len(row) != 1:
                name, x, y, orientation, length = row
                vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))
            # Read size of the grid
            else:
                n = int(row[0])
    return Grid(set(vehicles), n)

def display_results(start, came_from, goal, time, visited_nodes):
    """Visualizing the solution steps and prints the solution steps, time and
    the visited nodes.

    start: the initial rush hour board.
    came_from: a dictionary with the child as key and parent as value.
    goal: the board where the red car stands next to the exit.
    time: the time to find the solution.
    visited_nodes: the amount of visited nodes.
    """
    if time == 0:
        print "No solution found!"
    solution = reconstruct_path(came_from, start, goal)
    visualize(solution)
    print 'Solution steps: {0}'.format(', '.join(solution_steps(solution))) + '.'
    print 'Time to find solution of the board: {0}'.format(time) + '.'
    print 'Visited nodes: {0}'.format(visited_nodes) + '.'

def reconstruct_path(came_from, start, goal):
    """Starting from the goal situation, it finds it parent till the start
    situation is reached.

    came_from: a dictionary with the child as key and parent as value.
    start: the initial rush hour board.
    goal: the board where the red car stands next to the exit.

    Returns: The steps it took from the start situation to the goal situation.
    """
    current = goal
    path = [current]

    # Append configuartion to board as a step until the begin situation is reached
    while current != start:
        current = came_from[current][0]
        path.append(current)
    path.append(start)
    path.reverse()
    return [path[1:]]

def visualize(solution):
    """Simulation of the different steps on the board that lead to
    the solution from a breadth search algorithm. On OS X the visialization is
    working smooth, on windows it lags a bit.

    solution: a list of Grid objects leading to the solution.

    Returns: prints one Grid object in solution at a time.
    """
    # Check operating system and give the right clear command
    if os.name == 'nt':
        clear = 'cls'
    else:
        clear = 'clear'

    os.system(clear)
    # Loops through the list of Grid objects
    for i in range (len(solution[0]) - 1):
        # prints the solution, waits and than clears the displayed solution
        print (solution[0][i])
        time.sleep(.2)
        os.system(clear)

    # prints the final grid
    print solution[0][i + 1]
    return

def solution_steps(solution):
    """Generate list of steps to the solution.

    solution: a list of Grid objects leading to the solution.

    Returns: a list of the descriptions of the steps that lead to the solution.
    """
    steps = []
    # Loops through the list of Grid objects
    for i in range(len(solution[0]) - 1):
        # Calculating the difference between the vehicles in two Grid objects
        grid1, grid2 = solution[0][i], solution[0][i + 1]
        vehicle1 = list(grid1.vehicles - grid2.vehicles)[0]
        vehicle2 = list(grid2.vehicles - grid1.vehicles)[0]

        # Get direction of the step
        if vehicle1.x < vehicle2.x:
            steps.append('step %d: {0} right'.format(vehicle1.name) %i)
        elif vehicle1.x > vehicle2.x:
            steps.append('step %d: {0} left'.format(vehicle1.name) %i)
        elif vehicle1.y < vehicle2.y:
            steps.append('step %d: {0} down'.format(vehicle1.name) %i)
        elif vehicle1.y > vehicle2.y:
            steps.append('step %d: {0} up'.format(vehicle1.name) %i)
    return steps

if __name__ == '__main__':
    main()
    # cProfile.run('main()')
