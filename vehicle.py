

class Vehicle(object):
    """A configuration of a single vehicle. hallooo """

    def __init__(self, name, x, y, orientation, length):
        """Create a new vehicle.

        Arguments:
        name: character(s)
        x:  (0 till n)
        y:  (0 till n)
        orientation:  vertical (v) or horizontal (h)
        length: length of the vehicle (2-3)

        """
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.orientation = orientation
        self.length = int(length)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Vehicle({0}, {1}, {2}, {3}, {4})".format(self.name, int(self.x),
        int(self.y), self.orientation, int(self.length))
