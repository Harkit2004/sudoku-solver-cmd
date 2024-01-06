# Sudoku Solver
#### Video Demo:  https://youtu.be/rcIwMDguyjE
#### Description:
This Python script provides a simple Sudoku solver using a backtracking algorithm and recursion. The solver takes 3 X 3, 6 X 6 or 9 X 9 Sudoku board with empty cells represented by zeros and fills in the missing values to complete the puzzle.
### Usage
To use the Sudoku solver, simply replace the `b` in the `main` function and run the script as described below:
```
def main():
  # sudoku board to solve  
  b= [
      [6, 0, 0, 0, 2, 0, 0, 0, 1],
      [0, 1, 0, 5, 0, 9, 0, 7, 0],
      [0, 0, 9, 0, 0, 0, 4, 0, 0],
      [0, 5, 0, 9, 0, 8, 0, 4, 0],
      [4, 0, 0, 0, 7, 0, 0, 0, 3],
      [0, 6, 0, 4, 0, 3, 0, 2, 0],
      [0, 0, 3, 0, 0, 0, 6, 0, 0],
      [0, 8, 0, 6, 0, 2, 0, 9, 0],
      [5, 0, 0, 0, 9, 0, 0, 0, 4]]
  for i in solver(b):
    print(i)
```
### Code Overview
#### Variables
- **board:** Represents the Sudoku puzzle.
- **emptyIndex:** A list of dictionaries containing the row and column indices of empty cells on the board.
- **solvedValue:** A list to store the solved values in the board. `solvedValue[i]` is equal to the correct value of `emptyIndex[i]`.
- **noOfSolved:** Keeps track of how many values are solved till now.
### Functions
- **getEmptyIndex(b):**

    * **Input:** `b` - Sudoku board
    * **Output:** List of dictionaries containing the row and column indices of empty cells.

- **checker(b, index, value):**

    * **Input:**
        + `b` - Sudoku board
        + `index` - Dictionary containing row and column indices
        + `value` - Value to be checked
    * **Output:** True if the value is valid for the given cell, False otherwise.

- **solve():**

***Backtracking algorithm*** to solve the Sudoku puzzle. Uses recursion to fill in the empty cells.

- **solver(b):**

    * **Input:** `b` - Sudoku board
    * **Output:** Solved Sudoku board.

- **main():**

    * Entry point of the script.
    * Includes a default Sudoku puzzle.
    * Calls the solver function and prints the solved Sudoku board.

### Understanding the Backtracking Algorithm
The backtracking algorithm used in this script is a common approach for solving combinatorial problems like Sudoku. It explores potential solutions incrementally, backtracking when it determines that the current solution cannot be completed to a valid one.

In the context of Sudoku, the algorithm iterates through empty cells, attempting to fill them with valid values. If a conflict arises (e.g., the same value is present in the same row, column, or 3x3 grid), it backtracks to the previous cell and explores alternative values.

### Conclusion
This Sudoku solver script provides a clear example of a backtracking algorithm used to solve a well-known puzzle. It can be used as a tool to solve Sudoku puzzles efficiently and can serve as a learning resource for those interested in algorithms and problem-solving in Python. Feel free to experiment with different Sudoku puzzles and observe the script's performance and adaptability in solving them.