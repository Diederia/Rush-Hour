# Rush Hour
# Diederick, Valentijn en Jill

import numpy as np
import csv


def load_file(file):
    vehicles = []
    f = open(file)
    csv_file = csv.reader(f)

    for row in csv_file:
        name, x, y, orientation, length = row
        self.vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))
    f.close()

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
            self.x = x
            self.y = y
        else:
            raise ValueError('Invalid value(s) of coordinate(s)')

        if orientation == 'h' or 'v':
            self.orientation = orientation
        else:
            raise ValueError('Invalid value for orientation')

        if 2 <= length <= 3:
            self.length = length
        else:
            raise ValueError('Invalid value for length')

class Board(object):
    """
    A grid represents a rectangular region.
    The grid contains n x n positions, where there can be either a vehicle or not.
    """
    def __init__(self, n, vehicles):
        """
        Initializes a board with the specified height and width
        n = integer > 0
        """
        self.width = n
        self.height = n
        self.board = np.zeros((width, height))
        self.vehicles = vehicles


    def getVehicles(self):
        for Vehicle in self.vehicles:
            x, y = Vehicle.x, Vehicle.y

        if Vehicle.orientation == 'h':
            for i in range(Vehicle.length):
                self.board[y][x + i] = Vehicle.name
        else:
            for i in range(Vehicle.length):
                self.board[y + i][x] = Vehicle.name

        return self.board

    def isMoveable(self, Vehicle, direction, steps):

        if Vehicle.orientation == 'h':
            if direction == 'left':
                # check if coordiantes are within the board and if it doesn't bump into another car
                if Vehicle.x - steps >= 0 and board[Vehicle.y, Vehicle.x - steps] == 0:
                    # update the vehicle
                else:
                    raise ValueError('move is not valid')
            elif direction == 'right':
                if Vehicle.x + steps <= n and board[Vehicle.y, Vehicle.x + steps] == 0:
                    # update the vehicle
                    else:
                        raise ValueError ('move is not valid')
            else:
                raise ValueError('please give a left or right as direction')
        else:
            if direction == 'up':
                if Vehicle.y - steps >= 0 and board[Vehicle.y - steps, Vehicle.x] == 0:
                    #   update the vehicle
                else:
                    raise ValueError ('move is not valid')
            elif direction == 'down':
                if Vehicle.y + steps <= n and board[Vehicle.y + steps, Vehicle.x] == 0:
                    #update the vehicle
                else:
                    raise ValueError ('move is not valid')
            else:
                raise ValueError('please give a up or down direction')
    #
    # def solved(self):
    #     if n % 2 == 0:
    #         exitY = n / 2
    #     else:
    #         exitY = (n + 1) / 2
    #
    #     exitX = n - 2
    #
    #     if (target.x, target.y) == (exitX, exitY):
    #         return true
    #     else:
    #         return false

#
# class truck(Vehicle):
#
# class car(Vehicle):
#
# class target(Vehicle):
