# Rush Hour solver #
This is a rush hour solver written in python. It is tested using seven different begin configurations of the game with three different board sizes (6x6, 9x9 and 12x12).

## Set up and running the code ##
1. Download Github Project
2. Install python 2.7
3. Open project directory in terminal
4. Running the code with command line in the terminal: python rushhour.py Boards/board.csv algorithm
    * Possible boards: board1 till board7
    * Possible algorithms: astar or bfs
    * Posibble heuristics for astar:
        * 1: Blocking heuristic
        * 2: From goal heuristic
        * 3: Advanced heuristic
        * 4: Blocking heuristic + from goal heuristic
        * 5: Blocking heuristic + advanced heuristic
        * 6: Advanced heuristic + from goal heuristic
        * 7: Blocking heuristic + from goal heuristic + advanced heuristic

    Example if you would like to run the 5th board with an astar algorithm with the blocking and the from goal heuristic:

    ```
    python rushhour.py Boards/board5.csv astar 4
    ```
    Example if you would like to run the 5th board with the bfs algorithm:
    ```
    python rushhour.py Boards/board5.csv bfs
    ```

## Files ##

File          | Description
------------- | -------------
Boards        | File with representations of board 1 till 7
astar         | A* algorithm with differen heuristics
beamsearch    | Beamsearch alogrithm
breadthsearch | Breadth search first algorithm
grid          | Class Grid representing a rushhour board
vehicle       | The he main file in order to run the program
rushhour      | Class Vehicle representing a vehicle on the board

## Packages used (all built in) ##
* time
* queue
* heapq
* collections
* sys
* csv
* os
* cProfile

## Built With ##

* [Python Version 2.7](https://www.python.org/download/releases/2.7/)
* [Atom](https://atom.io) - text editor


## Authors ##

* **Diederick Calkoen**
* **Valentijn Frinking**
* **Jill de Ron**
