# Rush Hour
# Diederick, Valentijn en Jill

import csv

def main():
    """
    Return the input of the user, the dimension of the board and the file to
    load. The dimension is an integer.
    """
    n = input("Enter the dimension of the board: ")
    csv = raw_input("Enter the file to load: ")
    return n, csv

n, csv = main()
vehicles = []
counter = 0

def load_file():
    """
    Load the file of the user, each row is a vehicle. Read out all the vehicles
    and store them in vehicles.
    """
    with open('csv', 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name, x, y, orientation, length = row
            vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))

# class Position(object):
#
#     def __init__(self, x, y):
#
#         """
#         Initializes a position with coordiantes (x,y).
#         """
#         self.x = x
#         self.y = y
#
#     def getX(self):
#         return x
#     def getY(self):
#         return y
#     def getNewposition(self, direction, length):
#
#         old_x, old_y = self.getX(), self.getY()
#         if direction == 'left':
#             new_x = old_x - 1
#             new_y = old_y
#         elif direction == 'right':
#             new_x = old_x + 1
#             new_y = old_y
#         elif direction 'up':
#             new_y = old_y - 1
#             new_x = old_x
#         else direction == 'down':
#             new_y = old_y + 1
#             new_x = old_x
#         self.board[old_x][old_y] = 0
#         return Position(new_x, new_y)


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
        self.board = [ [0] * n for _ in range(n)]
        self.vehicles = vehicles

    def getVehicles(self):
        """
        Retrun a board filled with all vehicles.
        """
        for Vehicle in self.vehicles:
            x, y = Vehicle.x, Vehicle.y

            if Vehicle.orientation == 'h':
                for i in range(Vehicle.length):
                    self.board[y][x + i] = Vehicle.name
            else:
                for i in range(Vehicle.length):
                    self.board[y + i][x] = Vehicle.name
        return self.board

    def isMoveable(self, Vehicle, direction):

        """
        Move the vehicle if the next position of the car is within the board
        and it doesn't bump into another car. The function also counts all the
        moves.
        """
        # if Vehicle.name = "input user or algoritme"
        if Vehicle.orientation == 'h':
            if direction == 'left':
                # check if coordiantes are within the board and if it doesn't bump into another car.
                if Vehicle.x - 1 >= 0 and board[Vehicle.x - 1, Vehicle.y] == 0:
                    # count moves, update the vehicle next position and clears the old position.
                    counter += 1
                    newX = Vehicle.x - 1
                    self.board = [newX + Vehicle.length][Vehicle.y] = 0
                    Vehicle.x = newX
                    getVehicles()
                else:
                    raise ValueError('move is not valid')
            elif direction == 'right':
                # Check next position is within the board and is still free(0).
                if (Vehicle.x + Vehicle.length <= n and board[Vehicle.x +
                    Vehicle.length, Vehicle.y ] == 0:)
                    # count moves, update the vehicle next position and clears the old position.
                    counter += 1
                    newX = x + 1
                    self.board = [Vehicle.x][Vehicle.y] = 0
                    Vehicle.x = newX
                    getVehicles()
                else:
                    raise ValueError ('move is not valid')
            else:
                raise ValueError('please give a left or right as direction')
        else:
            if direction == 'up':
                # Check next position is within the board and is still free(0).
                if Vehicle.y - 1 >= 0 and board[Vehicle.x, Vehicle.y - 1] == 0:
                    # count moves, update the vehicle next position and clears the old position.
                    counter += 1
                    newY = Vehicle.y - 1
                    self.board = [Vehicle.x][newY + Vehicle.length] = 0
                    Vehicle.y = newY
                    getVehicles()
                else:
                    raise ValueError ('move is not valid')
            elif direction == 'down':
                # Check next position is within the board and is still free(0).
                if (Vehicle.y + Vehicle.length <= n and board[Vehicle.x,
                    Vehicle.y + Vehicle.length] == 0:)
                    # count moves, update the vehicle next position and clears the old position.
                    counter += 1
                    newY = y + 1
                    self.board = [Vehicle.x][Vehicle.y] = 0
                    Vehicle.y = newY
                    getVehicles()
                else:
                    raise ValueError('move is not valid')
            else:
                raise ValueError('please give a up or down direction')

    def solved(self):
        """
        Return True if vehicle x is at the exit of the board, False otherwise.
        """

        exitX = n - 2

        if Vehicle.name == x:
            if Vehicle.x == exitX:
                return True
            else:
                return False
        else:
            return False

    def __hash__(self):
        """
        Save the nodes by the value of the hash.
        """
        return self.vehicles

load_file()
board = Board(n, vehicles)

for i in board.getVehicles():
    print i, "\n"
