import numpy
from copy import deepcopy
from rushhour import *

# Global archive
archive = set()

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

        self.exit_x = self.n - 2
        if n != 9:
            self.exit_y = self.n / 2 - 1
        else:
            self.exit_y = self.n / 2


    # repr eruit wanneer we gaan runnen, bij visualize wel.
    def __repr__(self):
        "Returns a matrix that represents a board with borders around it."
        # counter = 0
        # matrix = '*' * (self.n * 2 + 3) + '\n'
        # for row in self.createBoard(self.vehicles):
        #     if counter == self.exit_y:
        #         matrix += '* {0} \n'.format(' '.join(row))
        #     else:
        #         matrix += '* {0} *\n'.format(' '.join(row))
        #     counter +=1
        # matrix += '*' * (self.n * 2 + 3) + '\n'
        #
        # #
        # # matrix = ''
        # # for row in self.createBoard(self.vehicles):
        # #     matrix += '' .join(row)

        return matrix


        # return str(self.createBoard()):

    def createBoard(self, vehicles):
        """Representation of the Rush Hour board as a 2D list of strings"""
        board = [ [' '] * self.n for _ in range(self.n)]
        for vehicle in vehicles:
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
        for vehicle in self.vehicles:
            if vehicle.name == 'x':
                if vehicle.x == self.exit_x:
                    print"test4"
                    return True
                else:
                    return False

    def getMoves(self):
        """
        Checks and returns all the possible moves from a current situation.

        Returns: iterator of next possible moves.
        """
        moves = []
        board = self.createBoard(self.vehicles)
        # iterates over all the vehicles on the board
        for vehicle in self.vehicles:
            # checks if the orientation of the vehicle is horizontal
            if vehicle.orientation == 'h':
                # LEFT
                if vehicle.x - 1 >= 0 and board[vehicle.y][vehicle.x - 1] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    if self.notInArchive(new_vehicles):
                        moves.append(Grid(new_vehicles, self.n))
                # RIGHT
                if vehicle.x + vehicle.length < self.n and board[vehicle.y][vehicle.x + vehicle.length] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    if self.notInArchive(new_vehicles):
                        moves.append(Grid(new_vehicles, self.n))
            # checks if the orientation of the vehicle is vertical
            else:
                # UP
                if vehicle.y - 1 >= 0 and board[vehicle.y - 1][vehicle.x] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    if self.notInArchive(new_vehicles):
                        moves.append(Grid(new_vehicles, self.n))
                # DOWN
                if vehicle.y + vehicle.length < self.n and board[vehicle.y + vehicle.length][vehicle.x] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    if self.notInArchive(new_vehicles):
                        moves.append(Grid(new_vehicles, self.n))
        return moves

    def notInArchive(self, new_vehicles):
        print len(archive)
        matrix = ''
        for row in self.createBoard(new_vehicles):
            matrix += ''.join(row)

        if matrix in archive:
            return False
        else:
            archive.add(matrix)
            return True


    def blockerEstimate(self, move):
        """
        Checks how many vehicles are standing in front of the (red) target car

        move: Grid object of the current situation

        Returns: an integer that represents the amount of vehicles blocking the
        (red) target car
        """
        new_vehicles = move.vehicles
        board = self.createBoard(new_vehicles)
        score = 0
        for i in range(self.n):
            currentPlace = board[self.exit_y][self.n - (i + 1)]
            if currentPlace != 'x':
                if currentPlace != ' ':
                    score += 2
            else:
                return score


    def fromGoal(self, move):
        """
        Checks how many steps away the (red) target car is from the exit

        move: Grid object of the current situation

        Returns: an integer that represents the amount of moves the (red)
        target car needs to make before it is at the exit position
        """
        new_vehicles = move.vehicles
        board = self.createBoard(new_vehicles)
        score = 0
        for i in range(self.n):
            currentPlace = board[self.exit_y][self.n - (i + 1)]
            if currentPlace == 'x':
                return score
            else:
                score += 1

    def advancedHeuristic(self, move):
        """
        Twee soorten, 1 voor de boards van 6x6 en 1 voor de grotere boards.
        Dit komt doordat je anders niet meer in de range van het board ben met checken.

        move: Grid object of the current situation

        Returns: an integer
        """
        new_vehicles = move.vehicles
        board = self.createBoard(new_vehicles)
        score = 0
        for i in range(self.n):
            currentPlace = board[self.exit_y][self.n - (i + 1)]
            if currentPlace != ' ' and currentPlace != 'x':
                if board[self.exit_y - 1][self.n - (i + 1)] == currentPlace:
                    if board[self.exit_y - 2][self.n - (i + 1)] == currentPlace:
                        if board[self.exit_y - 3][self.n - (i + 1)] != ' ':
                            # print 'test1'
                            score += 1
                    elif board[self.exit_y - 2][self.n - (i + 1)] != ' ':
                        # print 'test2'
                        score += 1
                elif board[self.exit_y - 1][self.n - (i + 1)] != ' ':
                    # print 'test3'
                    score += 1
                if board[self.exit_y + 1][self.n - (i + 1)] == currentPlace:
                    if board[self.exit_y + 2][self.n - (i + 1)] == currentPlace:
                        if board[self.exit_y + 3][self.n - (i + 1)] != ' ':
                            # print 'test4'
                            score += 1
                    elif board[self.exit_y + 2][self.n - (i + 1)] != ' ':
                        # print 'test5'
                        score += 1
                elif board[self.exit_y + 1][self.n - (i + 1)] != ' ':
                    # print 'test6'
                    score += 1
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
