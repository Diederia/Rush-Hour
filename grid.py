'''
    File description:
    This file contains Grid object used represent all the board configurations possible.
'''

from vehicle import Vehicle

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

    def get_moves(self):
        """Checks and returns all the possible moves from a current Grid object.

        Returns: a list of moves.
        """
        # Clear the move list
        moves[:] = []
        board = self.create_board(self.vehicles)

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

    def not_in_archive(self, new_vehicles):
        """Checks if the vehicle is not in archive."""

        # Create board because list is not hashable
        board = ''
        for row in self.create_board(new_vehicles):
            board += ''.join(row)

        if board in archive:
            return False
        else:
            archive.add(board)
            return True

    def is_vehicle_blocked(self, name, board, visted_vehicles):
        """Checks if a vehicle is blocked. If so, the function return the
        vehicle name of the blocking car, else it returns None.

        Returns: the name of the blocking car and a list of visted vehicles.
         """
        # Iterates over all the vehicles on the board
        for vehicle in self.vehicles:
            # Get the right vehicle
            if name == vehicle.name:
                # Checks if the orientation of the vehicle is horizontal
                if vehicle.orientation == 'h':
                    # Check if vehicle is next to border and is blocked
                    if vehicle.x + vehicle.length == self.n and board[vehicle.y][vehicle.x - 1] != ' ':
                        # Get the name of the blocking car
                        current_name = board[vehicle.y][vehicle.x - 1]
                        # Return the name and the list of visted vehicles
                        return self.return_blocked(name, visted_vehicles, current_name)
                    # Check if vehicle is next to border and is blocked
                    if vehicle.x - 1 < 0 and board[vehicle.y][vehicle.x + vehicle.length] != ' ':
                        # Get the name of the blocking car
                        current_name = board[vehicle.y][vehicle.x + vehicle.length]
                        # Return the name and the list of visted vehicles
                        return self.return_blocked(name, visted_vehicles, current_name)
                    # Check if vehicle is blocked by two other vehicles
                    if board[vehicle.y][vehicle.x - 1] != ' ' and board[vehicle.y][vehicle.x + vehicle.length] != ' ':
                        # Get the name of the right blocking car
                        current_name = board[vehicle.y][vehicle.x + vehicle.length]
                        # Only return the if it's not in the visted list
                        if self.return_blocked(name, visted_vehicles, current_name) != None:
                            return self.return_blocked(name, visted_vehicles, current_name)
                        # Get the name of the left blocking car
                        current_name = board[vehicle.y][vehicle.x - 1]
                        # Return the name and the list of visted vehicles
                        return self.return_blocked(name, visted_vehicles, current_name)
                else:
                    # Check if vehicle is next to border and is blocked
                    if vehicle.y + vehicle.length == self.n and board[vehicle.y - 1][vehicle.x] != ' ':
                        # Get the name of the blocking car
                        current_name = board[vehicle.y - 1][vehicle.x]
                        # Return the name and the list of visted vehicles
                        return self.return_blocked(name, visted_vehicles, current_name)
                    # Check if vehicle is next to border and is blocked
                    if vehicle.y - 1 < 0 and board[vehicle.y + vehicle.length][vehicle.x] != ' ':
                        # Get the name of the blocking car
                        current_name = board[vehicle.y + vehicle.length][vehicle.x]
                        return self.return_blocked(name, visted_vehicles, current_name)
                    # Check if vehicle is blocked by two other vehicles
                    if board[vehicle.y - 1][vehicle.x] != ' ' and board[vehicle.y + vehicle.length][vehicle.x] != ' ':
                        # Get the name of the down blocking car
                        current_name = board[vehicle.y + vehicle.length][vehicle.x]
                        # Only return the if it's not in the visted list
                        if self.return_blocked(name, visted_vehicles, current_name) != None:
                            return self.return_blocked(name, visted_vehicles, current_name)
                        # Get the name of the up blocking car
                        current_name = board[vehicle.y - 1][vehicle.x]
                        # Return the name and the list of visted vehicles
                        return self.return_blocked(name, visted_vehicles, current_name)

                # Vehicle is not blocked
                return None

    def return_blocked(self, name, visted_vehicles, current_name):
        """Checks if a vehicle is allready visted. if not the function returns
        the name and the visted list, else it returns None.

        Returns: Name of the current vehicle and the list of visted vehicles.
         """
        visted_vehicles.add(name)
        if current_name not in visted_vehicles:
            return current_name, visted_vehicles
        return None
