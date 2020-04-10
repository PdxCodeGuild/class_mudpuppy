# print_board.py
board = []
board.append(['1', '2', '3'])
board.append(['4', '5', '6'])
board.append(['7', '8', '9'])

for i in range(3):
    for j in range(3):
        print(board[i][j], end='')
    print()