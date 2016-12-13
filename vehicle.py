

class Vehicle(object):
    """
    A configuration of a single vehicle
    """

    def __init__(self, name, x, y, orientation, length):
        """
        Create a new vehicle.

        name: character(s)
        x:  0 till n
        y:  0 till n
        orientation:  vertical (v) or horizontal (h)
        length: length of the vehicle (2-3)
        """
        self.name = name
        self.x = x
        self.y = y
        self.orientation = orientation
        self.length = length

    def __repr__(self):
        "Representation of one vehicle"
        return "Vehicle({0}, {1}, {2}, {3}, {4})".format(self.name, self.x,
        self.y, self.orientation, self.length)
        return self.name, self.x, self.y, self.orientation, self.length
