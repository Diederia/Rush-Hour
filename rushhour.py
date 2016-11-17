# Rush Hour
# Diederick, Valentijn en Jill

# - bij move hebben we nog niks gereturned, waarschijnlijk moeten we het met
# yield doen.
#
import sys
# import csv
from breadthsearch import *
n = 0
def setN(val):
    global n
    n = val

if __name__ == "__main__":
    # if len(sys.argv) != 4:
    #     print("Give four input argument; python rushhour.py algorithm file dimension")
    # else:
    csv = sys.argv[1]
    setN(sys.argv[2])
    algorithm(csv, 1000)
    print solution(solution)





# def main():
# #     """
# #     Return the input of the user, the dimension of the board and the file to
# #     load. The dimension is an integer.
# #     """
#     csv = sys.argv[1]
#     n = sys.argv[2]
#     return csv, n
# #
# csv, n = main()
# algorithm(csv, 1000)


#
# result = algorithm.algorithm(csv, 100)
#
# print breadthsearch.bfs
