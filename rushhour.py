# Rush Hour
# Diederick, Valentijn en Jill

# - bij move hebben we nog niks gereturned, waarschijnlijk moeten we het met
# yield doen.
#
import sys
import csv
from board import *
from vehicle import *
from breadthsearch import *

def main():
    """
    Return the input of the user, the dimension of the board and the file to
    load. The dimension is an integer.
    """
    n = sys.argv[1]
    csv = sys.argv[2]
    return n, csv

n, csv = main()
result = bfs(rushhour, max_depth=100)
