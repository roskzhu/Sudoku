
# constants

board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(brd):
    for i in range (len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else: 
                print(str(brd[i][j]) + " ", end="")


#
# sudoku solver code
#

# solve the board with recursive application
def solve(brd):
    # base case: board is full
    find = find_empty(brd)
    if not find:
        return True # returns true or false depending on whether we found the solution or not
    else:
        row, col = find
    # i represents each possible move (1 to 9)
    for i in range(1, 10): 
        # check if by adding i into our board, if it's a valid solution
        if valid(brd, i, (row, col)):
            # if valid, add that into our board
            brd[row][col] = i
            # recursive call: call solve with new board
            if solve(brd):
                return True
            # backtrack: if solve does not return true, we reset the last element we just added,
            #            then repeat the process again recursively
            brd[row][col] = 0

    return False


# find an empty spot in the board, denoted by 0 
def find_empty(brd):
    for i in range(len(brd)):
        # check for the length of each row
        for j in range(len(brd[0])):
            # check if that position is 0 
            if brd[i][j] == 0:
                # return (row, column); (y, x) 
                return (i, j) 
    # if  there are no blank spots, return None for the solve function
    return None


# find if the current board is valid; if it meets the conditions of sudoku
def valid(brd, num, posn):
    # check occurences in each row
    for i in range(len(brd[0])):
        # (y, x)
        # check each element in each row and see if it's equal to the number we just added
        # and if the element is not the position we just inserted something into
        if brd[posn[0]][i] == num and posn[1] != i:
            return False

    # check occurences in each column
    for i in range(len(brd)):
        # (y, x)
        # check each element in each column and see if it's equal to the number we just added
        # and if the element is not the position we just inserted something into
        if brd[i][posn[1]] == num and posn[0] != i:
            return False

    # check occurences in each subsquare
    sbsqr_x = posn[1] // 3
    sbsqr_y = posn[0] // 3
    
    for i in range(sbsqr_y*3, sbsqr_x*3 + 3): 
        for j in range (sbsqr_x*3, sbsqr_y*3 + 3):
            if brd[i][j] == num and (i,j) != posn:
                return False

    return True


# test cases

print_board(board1)
print("\n________________SOLVED GAME:_________________\n")
solve(board1)
print_board(board1)
