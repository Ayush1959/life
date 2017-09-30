def display(board):
    ret = []
    for row in board:
        t_row = []
        for col in row:
            if col:
                t_row.append("X")
            else:
                t_row.append(".")
        ret.append("".join(t_row))
    return "\n".join(ret)
        

def alive(board, row, col):
    return board[row][col]

def kill(board, row, col):
    board[row][col] = False

def birth(board, row, col):
    board[row][col] = True

def num_live_neighbours(board, row, col):
    size = len(board)-1

    if row == 0 and col == 0:
        return int(board[0][1]) + int(board[1][1]) + int(board[1][0])

    if row == 0 and col == size:
        return int(board[0][size-1]) + int(board[1][size-1]) + int(board[1][size])
    
    if row == size and col == 0:
        return int(board[size-1][0]) + int(board[size-1][1]) + int(board[size][1])
        
    if row == size and col == size:
        return  int(board[size-1][size]) + int(board[size-1][size-1]) + int(board[size][size-1])

    # Top edge
    if row == 0:
        return int(board[0][col-1]) + int(board[1][col-1]) + int(board[1][col]) + int(board[1][col+1]) + int(board[0][col+1])

    if col == 0:
        return int(board[row-1][0])+int(board[row-1][1])+int(board[row][1])+int(board[row+1][1])+int(board[row+1][0])

    if row == size:
        return int(board[size][col-1])+int(board[size-1][col-1])+int(board[size-1][col])+int(board[size-1][col+1])+int(board[size][col+1])

    if col == size:
        return int(board[row-1][col]) + int(board[row-1][col-1]) + int(board[row][col-1]) + int(board[row+1][col-1]) + int(board[row+1][col])

    return  int(board[row-1][col-1])+ int(board[row-1][col])+ int(board[row-1][col+1])+ int(board[row][col+1])+ int(board[row+1][col+1])+ int(board[row+1][col])+ int(board[row+1][col-1])+ int(board[row][col-1])
    


def create_new_board(size):
    ret = []
    for i in range(size):
        cols = []
        for j in range(size):
            cols.append(False)
        ret.append(cols)
    return ret

        
def apply_rules(board):
    ret_board = create_new_board(len(board))
    # Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    
    for row in range(len(board)):
        for col in range(len(board)):
            if alive(board, row, col) and num_live_neighbours(board, row, col) < 2:
                kill(ret_board, row, col)

    return ret_board
                
        
