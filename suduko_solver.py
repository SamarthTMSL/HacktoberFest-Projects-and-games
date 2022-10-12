board=[
    [0,0,0,0,2,0,0,0,0],
    [0,0,0,0,0,8,2,4,9],
    [9,7,0,0,0,0,8,0,3],
    [0,9,0,2,0,0,1,0,0],
    [1,0,0,0,0,0,0,0,4],
    [0,0,3,0,0,7,0,6,0],
    [4,0,5,0,0,0,0,9,8],
    [7,3,1,4,0,0,0,0,0],
    [0,0,0,0,3,0,0,0,0]
    ]


def solve(board):
    find = empty_space(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

#func suduko_grid prints the suduko board
def suduko_grid(board):
    print("---Suduko solver---")
    print("")
    for i in range(len(board)):
        if i%3 ==0 and i!=0:
            print("--------------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j!=0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end=" ")

#func empty_space finds empty spaces represented by zero
def empty_space(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i,j)
            
    return None


        
suduko_grid(board)
print("solving ......")
solve(board)
print("---- Solved ----")
suduko_grid(board)
