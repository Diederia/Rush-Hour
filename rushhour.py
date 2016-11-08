# Rush Hour
# Diederick, Valentijn en Jill

import numpy as np
import csv

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
        self.x = x
        self.y = y
        self.orientation = orientation
        self.length = length

    def __repr__(self):
        return "Vehicle({0}, {1}, {2}, {3}, {4})".format(self.name, self.x,
        self.y, self.orientation, self.length)

class board(object):
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

    def load_file(file):
        vehicles = []
        f = open(file)
        csv_file = csv.reader(f)

        for row in csv_file:
            name, x, y, orientation, length = row
            vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))
        f.close()

    def getvehicles(self):
        for Vehicle in self.vehicles:
            x, y = Vehicle.x, Vehicle.y

        if Vehicle.orientation == 'h':
            for i in range(Vehicle.length):
                board[y][x + i] = Vehicle.name
        else:
            for i in range(Vehicle.length):
                board[y + i][x] = Vehicle.name

        return board

    def solved(self):
        if n % 2 == 0:
            exit.y = n / 2
        else:
            exit.y = (n + 1) / 2

        exit.x = n - 2

        if (target.x, target.y) == (exit.x, exit.y):
            return true
        else:
            return false


#
# class truck(Vehicle):
#
# class car(Vehicle):
#
# class target(Vehicle):
