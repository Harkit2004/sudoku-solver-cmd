
board = []
# list of indexes that are empty on the board
emptyIndex = []

# list to store solved values in board. solvedValue[i] is equal to the correct value of emptyIndex[i] 
solvedValue = []

# keep track of how many values are solved till now
noOfSolved = 0

# getting empty indexes from the board and storing them in the emptyIndex list
def getEmptyIndex(b):
  indices = []
  for i in range(len(b)):
    for j in range(len(b[i])):
      if (b[i][j] == 0):
        indices.append({"row": i, "col": j})
  # print(indices)
  return indices

# checking the 3 X 3 grid, the row and the column for any repeated values
def checker(b, index, value):
  row = index["row"] - index["row"] % 3
  # print(row)
  col = index["col"] - index["col"] % 3
  # print(col)
  for item in b[index["row"]]:
    if (item == value):
      return False
  # print("Row pass\n")
  for i in range(len(b)):
    if (b[i][index["col"]] == value):
      return False
  # print("Col pass\n")
  for i in range(row, row + 3):
    for j in range(col, col + 3):
      # print(board[i][j])
      if (b[i][j] == value):
        return False
  return True

# solving the actual board with the help of back tracking and recursion
def solve():
  global noOfSolved
  error = True
  # print(noOfSolved)
  for value in range(solvedValue[noOfSolved] + 1, 10):
    if (checker(board, emptyIndex[noOfSolved], value)):
      error = False
      board[emptyIndex[noOfSolved]["row"]][emptyIndex[noOfSolved]["col"]] = value
      solvedValue[noOfSolved] = value
      noOfSolved += 1
      break
  if (error):
    solvedValue[noOfSolved] = 0
    board[emptyIndex[noOfSolved]["row"]][emptyIndex[noOfSolved]["col"]] = 0
    noOfSolved -= 1
    solve()
    
def solver(b):
  global board, emptyIndex, solvedValue, noOfSolved
  board = b
  emptyIndex = getEmptyIndex(board)
  # print(emptyIndex)
  for i in range(len(emptyIndex)):
    solvedValue.append(0)
  while (noOfSolved < len(emptyIndex)):
    solve()
  # print(solvedValue)
  b = board
  board = []
  emptyIndex = []
  solvedValue = []
  noOfSolved = 0
  return b
  
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

if __name__ == "__main__":
  main()