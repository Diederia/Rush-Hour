import cProfile

import sys
from collections import deque
import csv
import time
import os

class RushHour(object):
    """A configuration of a single Rush Hour board."""

    def __init__(self, vehicles):
        """Create a new Rush Hour board.

        Arguments:
            vehicles: a set of Vehicle objects.
        """
        self.vehicles = vehicles

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.vehicles == set(other.vehicles)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        # s = '-' * 15 + '\n'
        # for line in self.createBoard():
        #     s += '| {0} |\n'.format(' '.join(line))
        # s += '-' * 15 + '\n'

        return str(self.createBoard())

    def createBoard(self):
        """Representation of the Rush Hour board as a 2D list of strings"""
        board = [ [' '] * n for _ in range(n)]
        for vehicle in self.vehicles:
            x, y = vehicle.x, vehicle.y
            if vehicle.orientation == 'h':
                for i in range(vehicle.length):
                    board[y][x + i] = vehicle.name
            else:
                for i in range(vehicle.length):
                    board[y + i][x] = vehicle.name
        return board

    def solved(self):
        """Returns true if the board is in a solved state."""
        exitX = n - 2
        for vehicle in self.vehicles:
            if vehicle.name == 'x':
                if vehicle.x == exitX:
                    return True
                else:
                    return False

    def getMoves(self):
        """Return iterator of next possible moves."""
        board = self.createBoard()

        for vehicle in self.vehicles:
            if vehicle.orientation == 'h':
                if vehicle.x - 1 >= 0 and board[vehicle.y][vehicle.x - 1] == ' ':
                    # print self.vehicles
                    # print RushHour(self.vehicles)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    # print 'test1'
                    # print RushHour(new_vehicles)
                    yield RushHour(new_vehicles)
                if vehicle.x + vehicle.length < n and board[vehicle.y][vehicle.x + vehicle.length] == ' ':
                    # print self.vehicles
                    # print RushHour(self.vehicles)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    # print 'test2'
                    # print RushHour(new_vehicles)
                    yield RushHour(new_vehicles)
            else:
                if vehicle.y - 1 >= 0 and board[vehicle.y - 1][vehicle.x] == ' ':
                    # print self.vehicles
                    # print RushHour(self.vehicles)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    # print 'test3'
                    # print RushHour(new_vehicles)
                    yield RushHour(new_vehicles)
                if vehicle.y + vehicle.length < n and board[vehicle.y + vehicle.length][vehicle.x] == ' ':
                    # print self.vehicles
                    # print RushHour(self.vehicles)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    # print 'test4'
                    # print RushHour(new_vehicles)
                    yield RushHour(new_vehicles)

def load_file(csv_file):
    vehicles = []
    with open(csv_file, 'rb') as csv_open_file:
        reader = csv.reader(csv_open_file)
        for row in reader:
            name, x, y, orientation, length = row
            vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))
    return RushHour(set(vehicles))

def bfs(game, max_depth):
    """
    Find solutions to given RushHour board using breadth first search.
    Returns a dictionary with named fields:
        visited: the number of configurations visited in the search
        solutions: paths to the goal state
        depth_states: the number of states visited at each depth

    Arguments:
        r: A RushHour board.

    Keyword Arguments:
        max_depth: Maximum depth to traverse in search (default=25)
    """
    archive = set()
    solution = list()
    queue = deque()
    queue.appendleft((game, tuple()))
    start = time.clock()
    while len(queue) != 0:
        board, path = queue.pop()
        new_path = path + tuple([board])

        if len(new_path) >= max_depth:
            # print 'test3'
            break

        if board in archive:
            # print 'test4'
            continue
        else:
            # print 'test5'
            archive.add(board)

        if board.solved():
            return

            # print 'test2'
            solution.append(new_path)
            end = time.clock()
            end_time = end - start
            print end_time
            return {'solution': solution, 'end_time': end_time}
        else:
            queue.extendleft((move, new_path) for move in board.getMoves())
            # print len(queue)
def solution_steps(results):
    """Generate list of steps from a solution path."""
    steps = []
    for i in range(len(solution) - 1):
        r1, r2 = solution[i], solution[i+1]
        v1 = list(r1.vehicles - r2.vehicles)[0]
        v2 = list(r2.vehicles - r1.vehicles)[0]
        if v1.x < v2.x:
            steps.append('step %d: {0} right'.format(v1.name) %i)
        elif v1.x > v2.x:
            steps.append('step %d: {0} left'.format(v1.name) %i)
        elif v1.y < v2.y:
            steps.append('step %d: {0} down'.format(v1.name) %i)
        elif v1.y > v2.y:
            steps.append('step %d: {0} upp'.format(v1.name) %i)
    return steps

def vesualize(results):
    counter = 0
    os.system('clear')
    for i in range(len(solution) - 1):
        counter += 1
        print (solution[i])
        time.sleep(.1)
        os.system('clear')
    print solution[counter]
    return 'Rush hour board is Completed! The solution steps are displayed below:'


class Vehicle(object):
    """A configuration of a single vehicle."""

    def __init__(self, name, x, y, orientation, length):
        """Create a new vehicle.

        Arguments:
        name: a valid car or truck name character(s)
        x: the x coordinate of the top left corner of the vehicle (0-5)
        y: the y coordinate of the top left corner of the vehicle (0-5)
        orientation: either the vehicle is vertical (v) or horizontal (h)
        length: length of the vehicle (2-3)
        """
        self.name = name

        if 0 <= x <= n and 0 <= y <= n:
            self.x = int(x)
            self.y = int(y)
        else:
            raise ValueError('Invalid value(s) of coordinate(s)')

        if orientation == 'h' or 'v':
            self.orientation = orientation
        else:
            raise ValueError('Invalid value for orientation')

        if 2 <= length <= 3:
            self.length = int(length)
        else:
            raise ValueError('Invalid value for length')

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.name, self.x, self.y, self.orientation, self.length

def main():
    global n
    csv_file = sys.argv[1]
    n = int(sys.argv[2])
    game = load_file(csv_file)
    result = bfs(game, 10000)
    # print 'test1'
    for solution in result['solution']:
        print vesualize(solution)
    for solution in result['solution']:
        print 'Solution steps: {0}'.format(', '.join(solution_steps(solution)))

    print 'Time to find solution of the board: {0}'.format(result['end_time']) + '.'

if __name__ == '__main__':
    cProfile.run('main()')
