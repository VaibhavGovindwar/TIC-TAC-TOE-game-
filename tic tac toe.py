from random import randrange

def display_board(board):
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|    " + str(board[row][col]) + "  ", end="")
        print("|")
        print("|       " * 3,"|", sep="")
        print("+-------" * 3,"+", sep="")


def enter_move(board):
    ok = False
    while not ok:
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= "1" and move <= "9"
        if not ok:
            print("Not a correct move - repeat your move")
            continue
        move = int(move) - 1 # cells number from 0 to 8
        row = move // 3      # cells row
        column = move % 3    # cells column
        sign = board[row][column]  # check the selected square
        ok = sign not in ['O', 'X']
        if not ok:  # its occupied to the input again
            print("field already occupied")
            continue
        board[row][column] = 'O'   # set 'O' at the selected square


def make_list_of_free_fields(board):
    free = []
    for row in range(3):        # rows
        for column in range(3): # columns
            if board[row][column] not in ['O', 'X']:
                free.append((row, column))
        return free


def victory_for(board, sign):
    if sign == 'X':   # looking for 'X'
        who = 'me'    # its computer side
    elif sign == 'O': # for O
        who = 'you'   # its user side
    else:
        who = None

    cross1 = cross2 = True # for diagonals
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign: # row rc
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign: # column rc
            return who
        if board[rc][rc] != sign: #check 1st diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sign:  # 2nd diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    free = make_list_of_free_fields(board)
    cmt = len(free)
    if cmt > 0:
        this = randrange(cmt)
        row, column = free[this]
        board[row][column] = 'X'


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'  # set first 'X' in the middle
free = make_list_of_free_fields(board)
human_turn = True  # which turn is it now?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won")
else:
    print("Tie!")
