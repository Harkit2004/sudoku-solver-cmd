from project import getEmptyIndex, checker, solver

board1 = [
          [6, 0, 0],
          [0, 1, 0],
          [0, 0, 9]]

board2 = [
          [6, 0, 0, 0, 2, 0],
          [0, 1, 0, 5, 0, 9],
          [0, 0, 9, 0, 0, 0],
          [0, 5, 0, 9, 0, 8],
          [4, 0, 0, 0, 7, 0],
          [0, 6, 0, 4, 0, 3]]

board3 = [
          [6, 0, 0, 0, 2, 0, 0, 0, 1],
          [0, 1, 0, 5, 0, 9, 0, 7, 0],
          [0, 0, 9, 0, 0, 0, 4, 0, 0],
          [0, 5, 0, 9, 0, 8, 0, 4, 0],
          [4, 0, 0, 0, 7, 0, 0, 0, 3],
          [0, 6, 0, 4, 0, 3, 0, 2, 0],
          [0, 0, 3, 0, 0, 0, 6, 0, 0],
          [0, 8, 0, 6, 0, 2, 0, 9, 0],
          [5, 0, 0, 0, 9, 0, 0, 0, 4]]

expected1 = [
            [6, 2, 3],
            [4, 1, 5],
            [7, 8, 9]]

expected2 = [
            [6, 3, 4, 1, 2, 7],
            [2, 1, 7, 5, 8, 9],
            [5, 8, 9, 3, 4, 6],
            [1, 5, 2, 9, 6, 8],
            [4, 9, 3, 2, 7, 1],
            [7, 6, 8, 4, 5, 3]]

expected3 = [
            [6, 4, 5, 3, 2, 7, 9, 8, 1],
            [2, 1, 8, 5, 4, 9, 3, 7, 6],
            [7, 3, 9, 1, 8, 6, 4, 5, 2],
            [3, 5, 2, 9, 6, 8, 1, 4, 7],
            [4, 9, 1, 2, 7, 5, 8, 6, 3],
            [8, 6, 7, 4, 1, 3, 5, 2, 9],
            [9, 2, 3, 7, 5, 4, 6, 1, 8],
            [1, 8, 4, 6, 3, 2, 7, 9, 5],
            [5, 7, 6, 8, 9, 1, 2, 3, 4]]

def test_getEmptyIndex():
    assert getEmptyIndex(board1) == [{'row': 0, 'col': 1}, {'row': 0, 'col': 2}, {'row': 1, 'col': 0}, 
                                     {'row': 1, 'col': 2}, {'row': 2, 'col': 0}, {'row': 2, 'col': 1}]
    assert getEmptyIndex(board2) == [{'row': 0, 'col': 1}, {'row': 0, 'col': 2}, {'row': 0, 'col': 3}, 
                                     {'row': 0, 'col': 5}, {'row': 1, 'col': 0}, {'row': 1, 'col': 2}, 
                                     {'row': 1, 'col': 4}, {'row': 2, 'col': 0}, {'row': 2, 'col': 1}, 
                                     {'row': 2, 'col': 3}, {'row': 2, 'col': 4}, {'row': 2, 'col': 5}, 
                                     {'row': 3, 'col': 0}, {'row': 3, 'col': 2}, {'row': 3, 'col': 4}, 
                                     {'row': 4, 'col': 1}, {'row': 4, 'col': 2}, {'row': 4, 'col': 3}, 
                                     {'row': 4, 'col': 5}, {'row': 5, 'col': 0}, {'row': 5, 'col': 2}, {'row': 5, 'col': 4}]
    assert getEmptyIndex(board3) == [{'row': 0, 'col': 1}, {'row': 0, 'col': 2}, {'row': 0, 'col': 3}, 
                                     {'row': 0, 'col': 5}, {'row': 0, 'col': 6}, {'row': 0, 'col': 7}, 
                                     {'row': 1, 'col': 0}, {'row': 1, 'col': 2}, {'row': 1, 'col': 4}, 
                                     {'row': 1, 'col': 6}, {'row': 1, 'col': 8}, {'row': 2, 'col': 0}, 
                                     {'row': 2, 'col': 1}, {'row': 2, 'col': 3}, {'row': 2, 'col': 4}, 
                                     {'row': 2, 'col': 5}, {'row': 2, 'col': 7}, {'row': 2, 'col': 8}, 
                                     {'row': 3, 'col': 0}, {'row': 3, 'col': 2}, {'row': 3, 'col': 4}, 
                                     {'row': 3, 'col': 6}, {'row': 3, 'col': 8}, {'row': 4, 'col': 1}, 
                                     {'row': 4, 'col': 2}, {'row': 4, 'col': 3}, {'row': 4, 'col': 5}, 
                                     {'row': 4, 'col': 6}, {'row': 4, 'col': 7}, {'row': 5, 'col': 0}, 
                                     {'row': 5, 'col': 2}, {'row': 5, 'col': 4}, {'row': 5, 'col': 6}, 
                                     {'row': 5, 'col': 8}, {'row': 6, 'col': 0}, {'row': 6, 'col': 1}, 
                                     {'row': 6, 'col': 3}, {'row': 6, 'col': 4}, {'row': 6, 'col': 5}, 
                                     {'row': 6, 'col': 7}, {'row': 6, 'col': 8}, {'row': 7, 'col': 0}, 
                                     {'row': 7, 'col': 2}, {'row': 7, 'col': 4}, {'row': 7, 'col': 6}, 
                                     {'row': 7, 'col': 8}, {'row': 8, 'col': 1}, {'row': 8, 'col': 2}, 
                                     {'row': 8, 'col': 3}, {'row': 8, 'col': 5}, {'row': 8, 'col': 6}, {'row': 8, 'col': 7}]
    
def test_checker():
    assert checker(board1, {"row": 0, "col": 1}, 1) == False
    assert checker(board2, {"row": 3, "col": 4}, 1) == True
    assert checker(board3, {"row": 6, "col": 3}, 1) == True 

def test_solver():
    assert solver(board1) == expected1
    assert solver(board2) == expected2
    assert solver(board3) == expected3
    

