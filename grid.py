import numpy
from copy import deepcopy
from rushhour import *


class Grid(object):
    """
    A configuration of a single Rush Hour board.
    """

    def __init__(self, vehicles, begin_board, n):
        """
        Create a new Rush Hour board.

        vehicles: a set of Vehicle objects.
        begin_board: the board to start with.
        n: the size of the board
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
        "What does this do?"
        return hash(self.__repr__())

    def __eq__(self, other):
        "What does this do?"
        return self.board == other.board

    def __ne__(self, other):
        "What does this do?"
        return not self.__eq__(other)

    # repr eruit wanneer we gaan runnen, bij visualize wel.
    def __repr__(self):
        "Returns a matrix that represents a board with borders around it."
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
        # return str(self.board)

    def solved(self):
        """
        Returns True if the board is in a solved state, returns False otherwise.
        """
        if self.board[self.exit_y][self.exit_x] == 'x':
            return True
        else:
            return False

    def getMoves(self):
        """
        Checks and returns all the possible moves from a current situation.

        Returns: iterator of next possible moves.
        """
        # iterates over all the vehicles on the board
        for vehicle in self.vehicles:
            # checks if the orientation of the vehicle is horizontal
            if vehicle.orientation == 'h':
                # LEFT
                if (vehicle.x - 1 >= 0 and
                    self.board[vehicle.y][vehicle.x - 1] == ' '):
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y][vehicle.x - 1] = vehicle.name
                    new_board[vehicle.y][vehicle.x + vehicle.length - 1] = ' '
                    yield Grid(new_vehicles, new_board, self.n)
                # RIGHT
                if (vehicle.x + vehicle.length < self.n and
                self.board[vehicle.y][vehicle.x + vehicle.length] == ' '):
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y][vehicle.x + vehicle.length] = vehicle.name
                    new_board[vehicle.y][vehicle.x] = ' '
                    yield Grid(new_vehicles, new_board, self.n)
            # checks if the orientation of the vehicle is vertical
            else:
                # UP
                if (vehicle.y - 1 >= 0 and
                    self.board[vehicle.y - 1][vehicle.x] == ' '):
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y - 1][vehicle.x] = vehicle.name
                    new_board[vehicle.y + vehicle.length - 1][vehicle.x] = ' '
                    new_board
                    yield Grid(new_vehicles, new_board, self.n)
                # DOWN
                if (vehicle.y + vehicle.length < self.n and
                    self.board[vehicle.y + vehicle.length][vehicle.x] == ' '):
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    new_board = deepcopy(self.board)
                    new_board[vehicle.y + vehicle.length][vehicle.x] = vehicle.name
                    new_board[vehicle.y][vehicle.x] = ' '
                    yield Grid(new_vehicles, new_board, self.n)

    def blockerEstimate(self, move):
<<<<<<< HEAD
        """
        Checks how many vehicles are standing in front of the (red) target car

        move: ??

        Returns: an integer that represents the amount of vehicles blocking the
        (red) target car
        """
        vehiclesBocking = 0
=======
        score = 0
>>>>>>> origin/master
        for i in range(self.n):
            currentPlace = self.board[self.exit_y][self.n - (i + 1)]
            if currentPlace == 'x':
                return score
            else:
                if currentPlace != ' ':
                    score += 3

    def fromGoal(self, move):
        """
        Checks how many steps away the (red) target car is from the exit

        move: ??

        Returns: an integer that represents the amount of moves the (red)
        target car needs to make before it is at the exit position
        """
        score = 0
        for i in range(self.n):
            currentPlace = self.board[self.exit_y][self.n - (i + 1)]
            if currentPlace == 'x':
                return score
            else:
                score += 2

    def advancedHeuristic(self, move):
        """
        Twee soorten, 1 voor de boards van 6x6 en 1 voor de grotere boards. Dit komt doordat je anders niet meer in de range van het board ben met checken.
        """

        score = 0
        for i in range(self.n):
            currentPlace = self.board[self.exit_y][self.n - (i + 1)]
            if currentPlace != ' ' and currentPlace != 'x':
                if self.board[self.exit_y - 1][self.n - (i + 1)] == currentPlace:
                    if self.board[self.exit_y - 2][self.n - (i + 1)] == currentPlace:
                        if self.board[self.exit_y - 3][self.n - (i + 1)] != ' ':
                            # print 'test1'
                            score += 3
                    elif self.board[self.exit_y - 2][self.n - (i + 1)] != ' ':
                        # print 'test2'
                        score += 3
                elif self.board[self.exit_y - 1][self.n - (i + 1)] != ' ':
                    # print 'test3'
                    score += 3
                if self.board[self.exit_y + 1][self.n - (i + 1)] == currentPlace:
                    if self.board[self.exit_y + 2][self.n - (i + 1)] == currentPlace:
                        if self.board[self.exit_y + 3][self.n - (i + 1)] != ' ':
                            # print 'test4'
                            score += 3
                    elif self.board[self.exit_y + 2][self.n - (i + 1)] != ' ':
                        # print 'test5'
                        score += 3
                elif self.board[self.exit_y + 1][self.n - (i + 1)] != ' ':
                    # print 'test6'
                    score += 3
        return score
        # for i in range(self.n):
        #     currentPlace = self.board[self.exit_y][self.n - (i + 1)]
        #     if currentPlace != ' ' and currentPlace != 'x':
        #         if self.board[self.exit_y - 1][self.n - (i + 1)] == currentPlace:
        #             if self.board[self.exit_y - 2][self.n - (i + 1)] != currentPlace and self.board[self.exit_y - 2][self.n - (i + 1)] != ' ':
        #                 score += 100
        #         elif self.board[self.exit_y - 1][self.n - (i + 1)] != ' ':
        #             score += 100
        #         if self.board[self.exit_y + 1][self.n - (i + 1)] == currentPlace:
        #             if self.board[self.exit_y - 2][self.n - (i + 1)] != currentPlace and self.board[self.exit_y - 2][self.n - (i + 1)] != ' ':
        #                 score += 100
        #         elif self.board[self.exit_y + 1][self.n - (i + 1)] != ' ':
        #             score += 100
        #
        # return score
