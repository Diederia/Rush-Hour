import numpy
import copy
from rushhour import *


class Grid(object):
    """
    A configuration of a single Rush Hour board.
    """

    def __init__(self, vehicles, n):
        """
        Create a new Rush Hour board.

        vehicles: a set of Vehicle objects.
        begin_board: the board to start with.
        n: the size of the board
        """
        self.n = n
        self.vehicles = vehicles
        begin_board = [ [' '] * n for _ in range(n)]
        self.board = begin_board

        self.exit_x = self.n - 1
        if n != 9:
            self.exit_y = self.n / 2 - 1
        else:
            self.exit_y = self.n / 2

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
                # cheks if the vehicle can move to the left
                if (vehicle.x - 1 >= 0 and
                    self.board[vehicle.y][vehicle.x - 1] == ' '):
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = copy.copy(self.vehicles)
                    new_vehicles.remove(vehicle)
                    new_vehicles.append(new_vehicle)
                    yield Grid(new_vehicles, self.n)
                # checks if the vehicle can move to the right
                if (vehicle.x + vehicle.length < self.n and
                self.board[vehicle.y][vehicle.x + vehicle.length] == ' '):
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = copy.copy(self.vehicles)
                    new_vehicles.remove(vehicle)
                    new_vehicles.append(new_vehicle)
                    yield Grid(new_vehicles, self.n)
            # if the vehicle isn't horizontal, it is vertical
            else:
                # checks if the vehicle can go up
                if (vehicle.y - 1 >= 0 and
                    self.board[vehicle.y - 1][vehicle.x] == ' '):
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    new_vehicles = copy.copy(self.vehicles)
                    new_vehicles.remove(vehicle)
                    new_vehicles.append(new_vehicle)
                    yield Grid(new_vehicles, self.n)
                # checks if the vehicle can go down
                if (vehicle.y + vehicle.length < self.n and
                    self.board[vehicle.y + vehicle.length][vehicle.x] == ' '):
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    new_vehicles = copy.copy(self.vehicles)
                    new_vehicles.remove(vehicle)
                    new_vehicles.append(new_vehicle)
                    yield Grid(new_vehicles, self.n)

    def blockerEstimate(self, move):

        """
        Checks how many vehicles are standing in front of the (red) target car

        move: ??

        Returns: an integer that represents the amount of vehicles blocking the
        (red) target car
        """
        vehiclesBocking = 0
        score = 0

        # comment
        for i in range(self.n):
            currentPlace = self.board[self.exit_y][self.n - (i + 1)]
            if currentPlace == 'x':
                return score
            else:
                if currentPlace != ' ':
                    score += 2

    def fromGoal(self, move):
        """
        Checks how many steps away the (red) target car is from the exit

        move: ??

        Returns: an integer that represents the amount of moves the (red)
        target car needs to make before it is at the exit position
        """
        score = 0

        # comment
        for i in range(self.n):
            currentPlace = self.board[self.exit_y][self.n - (i + 1)]
            # comment
            if currentPlace == 'x':
                return score
            else:
                score += 1

    # def advancedHeuristic(self, move):
    #     """
    #     Twee soorten, een voor de boards van 6x6 en een voor de grotere boards.
    #     Dit komt doordat je anders niet meer in de range van
    #     het board bent met checken.
    #     """
    #     score = 0
    #     for i in range(self.n):
    #         currentPlace = self.board[self.exit_y][self.n - (i + 1)]
    #         if currentPlace != ' ' and currentPlace != 'x':
    #             if self.board[self.exit_y - 1][self.n - (i + 1)] == currentPlace:
    #                 if self.board[self.exit_y - 2][self.n - (i + 1)] == currentPlace:
    #                     if self.board[self.exit_y - 3][self.n - (i + 1)] != ' ':
    #                         # print 'test1'
    #                         score += 1
    #                 elif self.board[self.exit_y - 2][self.n - (i + 1)] != ' ':
    #                     # print 'test2'
    #                     score += 1
    #             elif self.board[self.exit_y - 1][self.n - (i + 1)] != ' ':
    #                 # print 'test3'
    #                 score += 1
    #             if self.board[self.exit_y + 1][self.n - (i + 1)] == currentPlace:
    #                 if self.board[self.exit_y + 2][self.n - (i + 1)] == currentPlace:
    #                     if self.board[self.exit_y + 3][self.n - (i + 1)] != ' ':
    #                         # print 'test4'
    #                         score += 1
    #                 elif self.board[self.exit_y + 2][self.n - (i + 1)] != ' ':
    #                     # print 'test5'
    #                     score += 1
    #             elif self.board[self.exit_y + 1][self.n - (i + 1)] != ' ':
    #                 # print 'test6'
    #                 score += 1
    #     return score
    #     # for i in range(self.n):
    #     #     currentPlace = self.board[self.exit_y][self.n - (i + 1)]
    #     #     if currentPlace != ' ' and currentPlace != 'x':
    #     #         if self.board[self.exit_y - 1][self.n - (i + 1)] == currentPlace:
    #     #             if self.board[self.exit_y - 2][self.n - (i + 1)] != currentPlace and self.board[self.exit_y - 2][self.n - (i + 1)] != ' ':
    #     #                 score += 100
    #     #         elif self.board[self.exit_y - 1][self.n - (i + 1)] != ' ':
    #     #             score += 100
    #     #         if self.board[self.exit_y + 1][self.n - (i + 1)] == currentPlace:
    #     #             if self.board[self.exit_y - 2][self.n - (i + 1)] != currentPlace and self.board[self.exit_y - 2][self.n - (i + 1)] != ' ':
    #     #                 score += 100
    #     #         elif self.board[self.exit_y + 1][self.n - (i + 1)] != ' ':
    #     #             score += 100
    #     #
    #     # return score
