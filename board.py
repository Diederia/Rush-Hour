import vehicle

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
        for vehicle in vehicles:
            if vehicle.orientation == 'h':
                # check if coordiantes are within the board and if it doesn't bump into another car.
                if vehicle.x - 1 >= 0 and board[vehicle.x - 1, vehicle.y] == 0:
                    # Nu gaat die goed bij deze!
                    new_vehicle = Vehicle(vehicle.name, vehicle.x - 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    yield Board(new_vehicles)
                # Check next position is within the board and is still free(0).
                if (Vehicle.x + Vehicle.length <= n and board[Vehicle.x + Vehicle.length, Vehicle.y ] == 0:)
                    # count moves, update the vehicle next position and clears the old position.
                    new_vehicle = Vehicle(vehicle.name, vehicle.x + 1, vehicle.y, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    yield Board(new_vehicles)
            else:
                # Check next position is within the board and is still free(0).
                if Vehicle.y - 1 >= 0 and board[Vehicle.x, Vehicle.y - 1] == 0:
                    # Update the vehicle next position and clears the old position.
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y - 1, vehicle.orientation, vehicle.length)
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(vehicle)
                    new_vehicles.add(new_vehicle)
                    yield Board(new_vehicles)
                # Check next position is within the board and is still free(0).
                if (Vehicle.y + Vehicle.length <= n and board[Vehicle.x, Vehicle.y + Vehicle.length] == 0:)
                    # Update the vehicle next position and clears the old position.
                    new_vehicle = Vehicle(vehicle.name, vehicle.x, vehicle.y + 1, vehicle.orientation, vehicle.length)
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
            if vehicle.name == x:
                if vehicle.x == exitX:
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
