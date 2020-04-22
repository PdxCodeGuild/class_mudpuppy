#Tic Tac Toe Lab1, April 21st, 2020

board = [[' ', '|', ' ', '|', ' '], #indexes[0][0,2,4]
        [' ', '|', ' ', '|', ' '],  #indexes[1][0,2,4]
        [' ', '|', ' ', '|', ' ']]  #indexes[2][0,2,4]

    
def print_board(ls1):
    ls2 = []
    ls2 = '\n'.join([''.join(inner_list) for inner_list in board])
    print(ls2)
    return ls2

def your_move(inp1, inp2, inp3):
    if input_row == 0:
        board[0][input_col // 2] = input_token
    elif input_row == 1:
        board[1][input_col + 1] = input_token
    elif input_row == 2:
        board[2][input_col + 1] = input_token
    print_board(board)
    return None

while True:
    input_token = input("What is your token? : ")
    input_row = int(input("What is the index of your row? : "))
    input_col = int(input("What is the index of your column? : "))

    your_move(input_row, input_col, input_token)

    for inner_list in board:
        for item in inner_list:
            if item != ' ':
                print("That's the game!")
                break
            else:
                print("Next turn...")
                