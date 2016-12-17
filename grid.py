'''
    File description:
    This file contains Grid object used represent all the board configurations possible. 
'''

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


    def __repr__(self):
        """ 
        Returns a matrix that represents a board with borders around it.
        """
        counter = 0
        matrix = '*' * (self.n * 2 + 3) + '\n'
        for row in self.createBoard(self.vehicles):
            if counter == self.exit_y:
                matrix += '* {0} \n'.format(' '.join(row))
            else:
                matrix += '* {0} *\n'.format(' '.join(row))
            counter +=1
        matrix += '*' * (self.n * 2 + 3) + '\n'


        # matrix = ''
        # for row in self.createBoard(self.vehicles):
        #     matrix += '' .join(row)

        return matrix

    def createBoard(self, vehicles):
        """
        Representation of the Rush Hour board as a 2D list of strings
        """
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
        """
        Returns true if the board is in a solved state.
        """
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
                # Can the vehicle move to the LEFT?
                if vehicle.x - 1 >= 0 and board[vehicle.y][vehicle.x - 1] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    if self.notInArchive(new_vehicles):
                        moves.append(Grid(new_vehicles, self.n))
                # Can the vehicle move to the RIGHT?
                if vehicle.x + vehicle.length < self.n and board[vehicle.y][vehicle.x + vehicle.length] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    if self.notInArchive(new_vehicles):
                        moves.append(Grid(new_vehicles, self.n))
            # checks if the orientation of the vehicle is vertical
            else:
                # Can the vehicle move UP?
                if vehicle.y - 1 >= 0 and board[vehicle.y - 1][vehicle.x] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    if self.notInArchive(new_vehicles):
                        moves.append(Grid(new_vehicles, self.n))
                # Can the vehicle move DOWN?
                if vehicle.y + vehicle.length < self.n and board[vehicle.y + vehicle.length][vehicle.x] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    if self.notInArchive(new_vehicles):
                        moves.append(Grid(new_vehicles, self.n))
        return moves

    def notInArchive(self, new_vehicles):
        """
        EXPLANATION. 
        """
        print len(archive)
        matrix = ''
        for row in self.createBoard(new_vehicles):
            matrix += ''.join(row)

        if matrix in archive:
            return False
        else:
            archive.add(matrix)
            return True

    def isVehicleBlocked(self, name, boardFromMove, vistedVehicles):
        """
        This heuristic check how many vehicles block a car. 
        """
        board = boardFromMove
        for vehicle in self.vehicles:
            if name == vehicle.name:
                print vehicle
                if vehicle.orientation == 'h':
                    if vehicle.x + vehicle.length < self.n and board[vehicle.y][vehicle.x + vehicle.length] != ' ':
                        vistedVehicles.add(name)
                        currentName = board[vehicle.y][vehicle.x + vehicle.length]
                        if currentName not in vistedVehicles:
                            return currentName, vistedVehicles
                    if vehicle.x - 1 >= 0 and board[vehicle.y][vehicle.x - 1] != ' ':
                        vistedVehicles.add(name)
                        currentName = board[vehicle.y][vehicle.x - 1]
                        if currentName not in vistedVehicles:
                            return currentName, vistedVehicles
                else:
                    if vehicle.y + vehicle.length < self.n and board[vehicle.y + vehicle.length][vehicle.x] != ' ':
                        vistedVehicles.add(name)
                        currentName = board[vehicle.y + vehicle.length][vehicle.x]
                        if currentName not in vistedVehicles:
                            return currentName, vistedVehicles
                    if vehicle.y - 1 >= 0 and board[vehicle.y  - 1][vehicle.x] != ' ':
                        vistedVehicles.add(name)
                        currentName = board[vehicle.y - 1][vehicle.x]
                        if currentName not in vistedVehicles:
                            return currentName, vistedVehicles
                return False
