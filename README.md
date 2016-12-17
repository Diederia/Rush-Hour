# Rush Hour solver #
This is a rush hour solver written in python. It is tested using seven different begin configurations of the game with three different board sizes (6x6, 9x9 and 12x12). 

## Running the program ##
1. Download Github Project
2. Install python 2.7
3. Open project directory in terminal
4. Running the code with command line in the terminal: python Boards/board.csv algorithm rushhour.py
    * Possible algorithms: astar or bfs
    * Possible boards: board1 till board7

    Example if you would like to run the 5th board with an astar algorithm

    ```
    python rushhour.py Boards/board5.csv astar
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

## Built With ##

* [Atom Version 1.12.7](https://atom.io) - text editor
* [Python Version 2.7](https://www.python.org/download/releases/2.7/)

## Authors ##

* **Diederick Calkoen**
* **Valentijn Frinking**
* **Jill de Ron**
