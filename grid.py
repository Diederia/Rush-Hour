'''
    File description:
    This file contains Grid object used represent all the board configurations possible.
'''

from vehicle import Vehicle
from random import randint


# Global moves and archive
moves = []
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

        # Define coordinates exit, for odd number of size y coordinate - 1
        if n != 9:
            self.exit_y = self.n / 2 - 1
        else:
            self.exit_y = self.n / 2

    def __repr__(self):
        """
        Returns a board that represents a grid with borders around it.
        """
        counter = 0

        # Makes the upper border of the board
        board = '*' * (self.n * 2 + 3) + '\n'

        # Makes the side borders and row, skips the border at the exit
        for row in self.create_board(self.vehicles):
            if counter == self.exit_y:
                board += '* {0} \n'.format(' '.join(row))
            else:
                board += '* {0} *\n'.format(' '.join(row))
            counter +=1

        # Makes the lower border of the board
        board += '*' * (self.n * 2 + 3) + '\n'
        return board

    def create_board(self, vehicles):
        """Representation of the Rush Hour board as a 2D list of strings

        vehicles: list of information about the vehicles

        Returns: multiple arrays in an array representing a board filled with
        vehicles.
        """
        # Makes multiple empty arrays, representing an empty board
        board = [ [' '] * self.n for _ in range(self.n)]

        # Loops through all the vehicles and places it on the board
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
        """Checks if the board is solves, by checking if the target car (always
        named x) is on the coordinates of the exit.

        Returns: a boolian, true if the board is in a solved state and
        false otherwise.
        """
        for vehicle in self.vehicles:
            if vehicle.name == 'x':
                if vehicle.x == self.exit_x:
                    return True
                else:
                    return False

    def get_moves(self, board):
        """Checks and returns all the possible moves from a current Grid object.

        Returns: a list of moves.
        """
        # Clear the move list
        moves[:] = []

        # Iterates over all the vehicles on the board
        for vehicle in self.vehicles:
            # Checks if the orientation of the vehicle is horizontal
            if vehicle.orientation == 'h':
                # Can the vehicle move to the LEFT
                if vehicle.x - 1 >= 0 and board[vehicle.y][vehicle.x - 1] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    self.add_move(vehicle, new_vehicle)
                # Can the vehicle move to the RIGHT
                if vehicle.x + vehicle.length < self.n and board[vehicle.y][vehicle.x + vehicle.length] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    self.add_move(vehicle, new_vehicle)
            # Checks if the orientation of the vehicle is vertical
            else:
                # Can the vehicle move to the UP
                if vehicle.y - 1 >= 0 and board[vehicle.y - 1][vehicle.x] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    self.add_move(vehicle, new_vehicle)
                # Can the vehicle move to the DOWN
                if vehicle.y + vehicle.length < self.n and board[vehicle.y + vehicle.length][vehicle.x] == ' ':
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
                    self.add_move(vehicle, new_vehicle)
        return moves


    def add_move(self, vehicle, new_vehicle):
        """Creates a new list of vehicles, checks if it's in the archive and
        append the new grid object to moves list.
        """
        new_vehicles = self.vehicles.copy()
        new_vehicles.remove(vehicle)
        new_vehicles.add(new_vehicle)
        if self.not_in_archive(new_vehicles):
            moves.append(Grid(new_vehicles, self.n))

    def nodes_counter(self):
        return

    def not_in_archive(self, new_vehicles):
        """Checks if the vehicle is not in archive."""

        # Create board because list is not hashable
        board = ''
        for row in self.create_board(new_vehicles):
            board += ''.join(row)

        if board in archive:
            return False
        else:
            self.nodes_counter()
            archive.add(board)
            return True

    def is_vehicle_blocked(self, name, board, visted_vehicles):
        """Loops through vehicles """


        for vehicle in self.vehicles:
            if name == vehicle.name:
                if vehicle.orientation == 'h':
                    if vehicle.x + vehicle.length == self.n and board[vehicle.y][vehicle.x - 1] != ' ':
                        current_name = board[vehicle.y][vehicle.x - 1]
                        return self.return_blocked(name, visted_vehicles, current_name)
                    if vehicle.x - 1 < 0 and board[vehicle.y][vehicle.x + vehicle.length] != ' ':
                        current_name = board[vehicle.y][vehicle.x + vehicle.length]
                        return self.return_blocked(name, visted_vehicles, current_name)
                    if board[vehicle.y][vehicle.x - 1] != ' ' and board[vehicle.y][vehicle.x + vehicle.length] != ' ':
                        current_name = board[vehicle.y][vehicle.x + vehicle.length]
                        if self.return_blocked(name, visted_vehicles, current_name) != None:
                            return self.return_blocked(name, visted_vehicles, current_name)
                        current_name = board[vehicle.y][vehicle.x - 1]
                        if self.return_blocked(name, visted_vehicles, current_name) != None:
                            return self.return_blocked(name, visted_vehicles, current_name)
                else:
                    if vehicle.y + vehicle.length == self.n and board[vehicle.y - 1][vehicle.x] != ' ':
                        current_name = board[vehicle.y - 1][vehicle.x]
                        # print "1000"
                        return self.return_blocked(name, visted_vehicles, current_name)
                    if vehicle.y - 1 < 0 and board[vehicle.y + vehicle.length][vehicle.x] != ' ':
                        current_name = board[vehicle.y + vehicle.length][vehicle.x]
                        # print "2000"
                        return self.return_blocked(name, visted_vehicles, current_name)
                    if board[vehicle.y - 1][vehicle.x] != ' ' and board[vehicle.y + vehicle.length][vehicle.x] != ' ':
                        current_name = board[vehicle.y + vehicle.length][vehicle.x]
                        if self.return_blocked(name, visted_vehicles, current_name) != None:
                            return self.return_blocked(name, visted_vehicles, current_name)
                        current_name = board[vehicle.y - 1][vehicle.x]
                        if self.return_blocked(name, visted_vehicles, current_name) != None:
                            return self.return_blocked(name, visted_vehicles, current_name)

                return None

    def return_blocked(self, name, visted_vehicles, current_name):
        visted_vehicles.add(name)
        if current_name not in visted_vehicles:
            return current_name, visted_vehicles
        return None
