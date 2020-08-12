#Devin Salter

#Sudoku solver that takes a given board and produces the first solution found by searching from top left to bottom right
#Board values are found through board[y][x]

import copy

#Determines if the current value for a specific position is a valid candidate at the moment
def valid_position(board, x, y, value):
    #Skips checking 0, as it is a placeholder for empty positions
    if value == 0:
        return True
    
    #New board that removes the current value being examined to prevent false failures
    tempBoard = copy.deepcopy(board)
    tempBoard[y][x] = ''

    #Checks current row for value
    if value in tempBoard[y]:            
        return False
    #Checks currnet column for value
    for row in tempBoard:
        if row[x] == value:
            return False
    #3x3 board taken from 9x9 board
    section = get_section(tempBoard, x, y)
    if any(value in sublist for sublist in section):
        return False
    return True

#Helper method to find sections of values (3x3 grid from 9x9 grid)
def get_section(board, x, y):
    section_y = [[],[],[]]
    mod = 0
    if y < 3:
        mod = 0
    elif y < 6:
        mod = 3
    else:
        mod = 6
    for rows in range(0, 3, 1):
        section_y[rows] = board[rows + mod]

    section = [[],[],[]]
    if x < 3:
        mod = 0
    elif x < 6:
        mod = 3
    else:
        mod = 6
    for row in range(0, 3 , 1):
        temp = [0,0,0]
        for col in range(0, 3, 1):
            temp[col] = section_y[row][col + mod]
        section[row] = temp

    return section


def valid_candidate(board):
    for row in range(0, 9, 1):
        for col in range(0, 9, 1):
            if not valid_position(board, col, row, board[row][col]):
                return False
    return True

def solved_board(board):
    #Checks if the board is a valid candidate and has no 0s on the board
    if not any(0 in sublist for sublist in board) and valid_candidate(board):
        return True
    return False

def next_candidate(board, value):
    newBoard = copy.deepcopy(board)
    found = False
    for row in range(0, 9, 1):
        for col in range(0, 9, 1):
            if newBoard[row][col] == 0:
                newBoard[row][col] = value
                found = True
                break
        if found:
            break
    return newBoard

#Starts the entire solving process and shows each step
def solve(board):
    if not valid_candidate(board):
        return None    
    if solved_board(board):
        return board
    current_value = 1
    while current_value < 10:
        newBoard = next_candidate(board, current_value)
        sol = solve(newBoard)
        if sol != None:
            return sol
        current_value += 1       
    return None

#Prints board
def print_board(board):
    for rows in board:
        current_line = ""
        for col in rows:
            current_line = current_line + str(col) + " "
        print(current_line)
    print()
    
test = [[0,1,2,3,4,5,6,7,8],
    [9,10,11,12,13,14,15,16,17],
    [18,19,20,21,22,23,24,25,26],
    [27,28,29,30,31,32,33,34,35],
    [36,37,38,39,40,41,42,43,44],
    [45,46,47,48,49,50,51,52,53],
    [54,55,56,57,58,59,60,61,62],
    [63,64,65,66,67,68,69,70,71],
    [72,73,74,75,76,77,78,79,80]]
zeroes = [[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]
board = [[5,3,0,0,7,0,0,0,0],
     [6,0,0,1,9,5,0,0,0],
     [0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],
     [4,0,0,8,0,3,0,0,1],
     [7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],
     [0,0,0,4,1,9,0,0,5],
     [0,0,0,0,8,0,0,7,9]]
print_board(solve(board))

