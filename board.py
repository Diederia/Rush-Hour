vehicles = []

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

    def getVehicles(self):
        """
        Retrun a board filled with all vehicles.
        """
        self.board = [ [0] * n for _ in range(n)]

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
        # ga door alle vehicles en kijk welke isMovable
        # if Vehicle.name = "input user or algoritme"
        board = self.getVehicles()
        for Vehicle in vehicles:
            if Vehicle.orientation == 'h':
                if direction == 'left':
                    # check if coordiantes are within the board and if it doesn't bump into another car.
                    if Vehicle.x - 1 >= 0 and board[Vehicle.x - 1, Vehicle.y] == 0:
                        # Nu gaat die goed bij deze!
                        new_Vehicle = Vehicle(Vehicle.name, Vehicle.x - 1, Vehicle.y, Vehicle.orientation, Vehicle.length)
                        new_Vehicle = Vehicle(Vehicle.name, Vehicle.x, Vehicle.y - 1, Vehicle.orientation, Vehicle.length)
                        new_vehicles = self.vehicles.Copy()
                        new_vehicles.Remove(Vehicle)
                        new_vehicles.Add(new_Vehicle)
                        yield Board(new_vehicles)
                    else:
                        raise ValueError('move is not valid')
                    elif direction == 'right':
                        # Check next position is within the board and is still free(0).
                        if (Vehicle.x + Vehicle.length <= n and board[Vehicle.x + Vehicle.length, Vehicle.y ] == 0:)
                        # count moves, update the vehicle next position and clears the old position.
                        new_Vehicle = Vehicle(Vehicle.name, Vehicle.x + 1, Vehicle.y, Vehicle.orientation, Vehicle.length)
                        new_vehicles = self.vehicles.Copy()
                        new_vehicles.Remove(Vehicle)
                        new_vehicles.Add(new_Vehicle)
                        yield Board(new_vehicles)
                    else:
                        raise ValueError ('move is not valid')
                else:
                    raise ValueError('please give a left or right as direction')
            else:
                if direction == 'up':
                    # Check next position is within the board and is still free(0).
                    if Vehicle.y - 1 >= 0 and board[Vehicle.x, Vehicle.y - 1] == 0:
                        # Update the vehicle next position and clears the old position.
                        new_Vehicle = Vehicle(Vehicle.name, Vehicle.x, Vehicle.y - 1, Vehicle.orientation, Vehicle.length)
                        new_vehicles = self.vehicles.Copy()
                        new_vehicles.Remove(Vehicle)
                        new_vehicles.Add(new_Vehicle)
                        yield Board(new_vehicles)                    else:
                        raise ValueError ('move is not valid')
                elif direction == 'down':
                    # Check next position is within the board and is still free(0).
                    if (Vehicle.y + Vehicle.length <= n and board[Vehicle.x, Vehicle.y + Vehicle.length] == 0:)
                        # Update the vehicle next position and clears the old position.
                        new_Vehicle = Vehicle(Vehicle.name, Vehicle.x, Vehicle.y + 1, Vehicle.orientation, Vehicle.length)
                        new_vehicles = self.vehicles.Copy()
                        new_vehicles.Remove(Vehicle)
                        new_vehicles.Add(new_Vehicle)
                        yield Board(new_vehicles)
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
        Save the vehicles by the value of the hash.
        """
        return hash(self.vehicles)
