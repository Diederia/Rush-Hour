# Rush Hour
# Diederick, Valentijn en Jill

import numpy as np
import csv

class vehicle(object):
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
        return "vehicle({0}, {1}, {2}, {3}, {4})".format(self.name, self.x,
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
        f = open('board1.csv')
        csv_file = csv.reader(f)

        for row in csv_file:
            # vehicles.append(row[0])
            name, x, y, orientation, length = row
            vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))
        f.close()
        return board(set(vehicles))

    def getvehicles(self):
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
# class truck(vehicle):
#
# class car(vehicle):
#
# class target(vehicle):
