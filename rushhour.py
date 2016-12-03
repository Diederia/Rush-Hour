import cProfile

import sys
import csv
import os
import time
from vehicle import Vehicle
from breadthsearch import *
from grid import *
from astar import *

def load_file(csv_file, n):
    vehicles = []
    with open(csv_file, 'rb') as csv_open_file:
        reader = csv.reader(csv_open_file)
        for row in reader:
            name, x, y, orientation, length = row
            vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))

    begin_board = [ [' '] * n for _ in range(n)]
    for vehicle in vehicles:
        x, y = vehicle.x, vehicle.y
        if vehicle.orientation == 'h':
            for i in range(vehicle.length):
                begin_board[y][x + i] = vehicle.name
        else:
            for i in range(vehicle.length):
                begin_board[y + i][x] = vehicle.name
    return Grid(set(vehicles), begin_board, n)


def solution_steps_bfs(solution):
    """Generate list of steps to the solution ."""
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

def solution_steps_astar(solution):
    """Generate list of steps to the solution ."""
    steps = []
    # print solution
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
        solution, end_time = bfs(game, 10000)
        # print visualize_bfs(solution)
        print 'Solution steps: {0}'.format(', '.join(solution_steps_bfs(solution)))
    else:
        print 'Please enter A* or bfs'

    print 'Time to find solution of the board: {0}'.format(end_time) + '.'

if __name__ == '__main__':
    # main()
    cProfile.run('main()')
# 
