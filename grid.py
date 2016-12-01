from copy import deepcopy
from rushhour import *
import numpy


class Grid(object):
    """A configuration of a single Rush Hour board."""

    def __init__(self, vehicles, begin_board, n):
        """Create a new Rush Hour board.

        Arguments:
            vehicles: a set of Vehicle objects.
            begin_board: the board to start with.
        """
        self.n = n
        self.vehicles = vehicles
        self.board = begin_board

        self.exit_x = self.n - 1
        if n != 9:
            self.exit_y = self.n / 2 - 1
        else:
            self.exit_y = self.n / 2

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        counter = 0
        matrix = '*' * (self.n * 2 + 3) + '\n'
        for row in self.board:
            if counter == self.exit_y:
                matrix += '* {0} \n'.format(' '.join(row))
            else:
                matrix += '* {0} *\n'.format(' '.join(row))
            counter +=1
        matrix += '*' * (self.n * 2 + 3) + '\n'
        return matrix

    def solved(self):
        """Returns true if the board is in a solved state."""
        # exit_x = self.n - 2
        # for vehicle in self.vehicles:
        #     if vehicle.name == 'x':
        #         if vehicle.x == exit_x:
        #             return True
        #         else:
        #             return False

        if self.board[self.exit_y][self.exit_x] == 'x':
            return True
        else:
            return False

    def getMoves(self):
        """Return iterator of next possible moves."""
        for vehicle in self.vehicles:
            if vehicle.orientation == 'h':
                # LEFT
                if (vehicle.x - 1 >= 0 and
                    self.board[vehicle.y][vehicle.x - 1] == ' '):
                    # print self.vehicles
                    # print Grid(self.vehicles, self.board)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y][vehicle.x - 1] = vehicle.name
                    new_board[vehicle.y][vehicle.x + vehicle.length - 1] = ' '
                    # print new_board
                    # print test_board
                    # print 'test1'
                    # print Grid(new_vehicles, new_board, self.n)
                    yield Grid(new_vehicles, new_board, self.n)
                # RIGHT
                if (vehicle.x + vehicle.length < self.n and
                self.board[vehicle.y][vehicle.x + vehicle.length] == ' '):
                    # print self.vehicles
                    # print Grid(self.vehicles, self.board)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y][vehicle.x + vehicle.length] = vehicle.name
                    new_board[vehicle.y][vehicle.x] = ' '
                    # print new_board
                    # print 'test2'
                    # print Grid(new_vehicles, new_board, self.n)
                    yield Grid(new_vehicles, new_board, self.n)
            else:
                # UPP
                if (vehicle.y - 1 >= 0 and
                    self.board[vehicle.y - 1][vehicle.x] == ' '):
                    # print self.vehicles
                    # print Grid(self.vehicles, self.board)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y - 1][vehicle.x] = vehicle.name
                    new_board[vehicle.y + vehicle.length - 1][vehicle.x] = ' '
                    new_board
                    # print 'test3'
                    # print Grid(new_vehicles, new_board, self.n)
                    yield Grid(new_vehicles, new_board, self.n)
                # DOWN
                if (vehicle.y + vehicle.length < self.n and
                    self.board[vehicle.y + vehicle.length][vehicle.x] == ' '):
                    # print self.vehicles
                    # print Grid(self.vehicles, self.board)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y + vehicle.length][vehicle.x] = vehicle.name
                    new_board[vehicle.y][vehicle.x] = ' '
                    # print new_board
                    # print 'test4'
                    # print Grid(new_vehicles, new_board, self.n)
                    yield Grid(new_vehicles, new_board, self.n)

    def blockerEstimate(self, move):
        vehiclesBocking = 0
        for i in range(self.n):
            currentPlace = self.board[self.exit_y][self.n - (i + 1)]
            if currentPlace == 'x':
                return vehiclesBocking
            else:
                if currentPlace != ' ':
                    vehiclesBocking += 10

    def fromGoal(self, move):
        score = 0
        for i in range(self.n):
            currentPlace = self.board[self.exit_y][self.n - (i + 1)]
            if currentPlace == 'x':
                return score
            else:
                score += 7

    def advancedHeuristic(self, move):
        score = 0
