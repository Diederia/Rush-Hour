# Rush Hour
# Diederick, Valentijn en Jill

# - bij move hebben we nog niks gereturned, waarschijnlijk moeten we het met
# yield doen.
#

import csv
for board import *
for vehicle import *

def main():
    """
    Return the input of the user, the dimension of the board and the file to
    load. The dimension is an integer.
    """
    n = input("Enter the dimension of the board: ")
    csv = raw_input("Enter the file to load: ")
    return n, csv

n, csv = main()

def load_file():
    """
    Load the file of the user, each row is a vehicle. Read out all the vehicles
    and store them in vehicles.
    """
    with open('csv', 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name, x, y, orientation, length = row
            vehicles.append(Vehicle(name, int(x), int(y), orientation, int(length)))


load_file()
board = Board(n, vehicles)


for i in board.getVehicles():
    print i, "\n"
