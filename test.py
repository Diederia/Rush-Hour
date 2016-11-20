import sys
import csv
from collections import deque

vehicles = []

def load_file(csv_file):
    """
    Load the file of the user, each row is a vehicle. Read out all the vehicles
    and store them in vehicles.
    """
    with open(csv_file, 'rb') as csv_open_file:
        reader = csv.reader(csv_open_file)
        for row in reader:
            name, x, y, orientation, length = row
            vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))


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
        self.board = []
        self.vehicles = vehicles

    def createBoard(self):
        """
        Retrun a board filled with all vehicles.
        """
        self.board = [ [0] * int(n) for _ in range(int(n))]

        for Vehicle in self.vehicles:
            x, y = Vehicle.x, Vehicle.y

            if Vehicle.orientation == 'h':
                for i in range(Vehicle.length):
                    self.board[y][x + i] = Vehicle.name
            else:
                for i in range(Vehicle.length):
                    self.board[y + i][x] = Vehicle.name
        return self.board

    def getMoves(self):

        """
        Move the vehicle if the next position of the car is within the board
        and it doesn't bump into another car. The function also counts all the
        moves.
        """
        # ga door alle vehicles en kijk welke isMovable
        # if Vehicle.name = "input user or algoritme"
        board = self.board
        for vehicle in vehicles:
            if vehicle.orientation == 'h':
                # check if coordiantes are within the board and if it doesn't bump into another car.
                print vehicle.x
                if vehicle.x - 1 >= 0 and board[vehicle.x - 1, vehicle.y] == 0:
                    # Nu gaat die goed bij deze!
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    self.board[vehicle.x + vehicle.length, vehicle.y] = 0
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    yield Board(new_vehicles)
                # Check next position is within the board and is still free(0).
                if (vehicle.x + vehicle.length) <= n and board[vehicle.x + vehicle.length, vehicle.y] == 0:
                    # count moves, update the vehicle next position and clears the old position.
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    self.board[vehicle.x - vehicle.length, vehicle.y] = 0
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    yield Board(new_vehicles)
            else:
                # Check next position is within the board and is still free(0).
                if vehicle.y - 1 >= 0 and board[vehicle.x, vehicle.y - 1] == 0:
                    # Update the vehicle next position and clears the old position.
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    self.board[vehicle.x, vehicle.y + vehicle.length] = 0
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    yield Board(new_vehicles)
                # Check next position is within the board and is still free(0).
                if (vehicle.y + vehicle.length) <= n and board[vehicle.x, vehicle.y + vehicle.length] == 0:
                    # Update the vehicle next position and clears the old position.
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    self.board[vehicle.x, vehicle.y - vehicle.length] = 0
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    yield Board(new_vehicles)

    def solved(self):
        """
        Return True if vehicle x is at the exit of the board, False otherwise.
        """
        exitX = n - 2

        for vehicle in vehicles:
            if vehicle.name == 'x':
                if vehicle.x == exitX:
                    return True
                else:
                    return False
            else:
                return False


def bfs(board, max_depth=100):
    """
    Use breadth first search algorithm to find a solution for Rush Hour.

    Arguments:
    begin_board: The begin position of the board wanting to solve
    max_depth: Least amount of steps to solve the rush hour puzzle
    """
    begin_board = Board(n, vehicles).createBoard()
    archive = set()
    solution = list()
    queue = deque()
    queue.appendleft((begin_board, tuple()))
    while len(queue) != 0:

        # add begin board on the queue
        board, path = queue.pop()
            # make all children from current board state
        new_path = path + tuple([board])

            # stop if amount of moves is to much
        if len(new_path) >= max_depth:
            break

        # if board in archive:
        #     continue
        # else:
        #     archive.add(board)

        # check if board is already solved (yes? Stop and return)
        if Board(vehicles, n).solved():
            solution.append(new_path)
            return solution
        else:
            # add all children to the queue
            queue.extendleft((move, new_path) for move in Board(n, vehicles).getMoves())

    print solution

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

    def __repr__(self):
        return "Vehicle({0}, {1}, {2}, {3}, {4})".format(self.name, int(self.x),
        int(self.y), self.orientation, int(self.length))

if __name__ == "__main__":
    csv_file = sys.argv[1]
    n = int(sys.argv[2])
    game = load_file(csv_file)
    bfs(game, 1000)
