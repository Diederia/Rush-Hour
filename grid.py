from copy import deepcopy
from rushhour import *

n = 6

class Grid(object):
    """A configuration of a single Rush Hour board."""

    def __init__(self, vehicles, begin_board):
        """Create a new Rush Hour board.

        Arguments:
            vehicles: a set of Vehicle objects.
            begin_board: the board to start with.
        """
        self.vehicles = vehicles
        self.board = begin_board

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        matrix = '*' * 15 + '\n'
        for row in self.board:
            matrix += '* {0} *\n'.format(' '.join(row))
        matrix += '*' * 15 + '\n'
        return matrix

    def solved(self):
        """Returns true if the board is in a solved state."""
        exit_x = n - 2
        for vehicle in self.vehicles:
            if vehicle.name == 'x':
                if vehicle.x == exit_x:
                    return True
                else:
                    return False
        #
        # if self.board[exit_y][exit_x] == 'x':
        #     return True
        # else:
        #     return False

    def getMoves(self):
        """Return iterator of next possible moves."""
        for vehicle in self.vehicles:
            if vehicle.orientation == 'h':
                # LEFT
                if vehicle.x - 1 >= 0 and self.board[vehicle.y][vehicle.x - 1] == ' ':
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
                    # print Grid(new_vehicles, new_board)
                    yield Grid(new_vehicles, new_board)
                # RIGHT
                if vehicle.x + vehicle.length < n and self.board[vehicle.y][vehicle.x + vehicle.length] == ' ':
                    # print self.vehicles
                    # print Grid(self.vehicles, self.board)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y][vehicle.x + vehicle.length] = vehicle.name
                    new_board[vehicle.y][vehicle.x] = ' '
                    # print 'test2'
                    # print Grid(new_vehicles, new_board)
                    yield Grid(new_vehicles, new_board)
            else:
                # UPP
                if vehicle.y - 1 >= 0 and self.board[vehicle.y - 1][vehicle.x] == ' ':
                    # print self.vehicles
                    # print Grid(self.vehicles, self.board)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y - 1][vehicle.x] = vehicle.name
                    new_board[vehicle.y + vehicle.length - 1][vehicle.x] = ' '
                    # print 'test3'
                    # print Grid(new_vehicles, new_board)
                    yield Grid(new_vehicles, new_board)
                # DOWN
                if vehicle.y + vehicle.length < n and self.board[vehicle.y + vehicle.length][vehicle.x] == ' ':
                    # print self.vehicles
                    # print Grid(self.vehicles, self.board)
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y + vehicle.length][vehicle.x] = vehicle.name
                    new_board[vehicle.y][vehicle.x] = ' '
                    # print 'test4'
                    # print Grid(new_vehicles, new_board)
                    yield Grid(new_vehicles, new_board)
