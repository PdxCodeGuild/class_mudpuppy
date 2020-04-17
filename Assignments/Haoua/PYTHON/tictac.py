 Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

# You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

# The Player class has the following properties:

# name = player name
# token = 'X' or 'O'
# The Game class has the following properties:

# board = your representation of the board
# You can represent the board however you like, such as a 2D list, tuples, or dictionary.

# The Game class has the following methods:

# __repr__() Returns a pretty string representation of the game board
# >>> print(board)
# X| | 
# O|X|O
#  | | 
# move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
# >>> board.move(2, 1, player_1)
#  | | 
#  | |X
#  | | 
# calc_winner() What token character string has won or None if no one has.
# X| | 
# O|X|O
#  | |X
# >>> board.calc_winner()
# X
# is_full() Returns true if the game board is full.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_full()
# True
# is_game_over() Returns true if the game board is full or a player has won.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_game_over()
# True

# X|O|
#  | |X
#  | |
# >>> board.is_game_over()
# False

# The Player class has the following properties:
# name = player name
# token = 'X' or 'O'
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    
    def token_name(self
    

# The Game class has the following properties:

# board = your representation of the board
class Game:
    def __init__(self,):
        self.board =  [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # __repr__() Returns a pretty string representation of the game board
    def __repr__(self):
        print('')
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print('')

        # 0 1 2
        # 3 4 5
        # 6 7 8


    # move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
    def move(self,i,player):
        # dict = {
        #     1: 1,
        #     2: [0, 1],
        # }    
        # dict[1]
        # self.board[4]
        # self.board[4] = player1.token
        # player_1 = Player('bob', 'X')
        player_pick = int(input(f'{player.name}, Make your move: '))
        
        if self.board[player_pick] != 'X' or self.board[player_pick] != 'O':
            self.board[player_pick] = player.token
            return player_pick
        else:
            pr

    # calc_winner() What token character string has won or None if no one has.
    def calc_winner(self):
        self.win_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0, 3, 6), (1, 4, 7), (2, 5, 8))


    # is_full() Returns true if the game board is full.
    def is_full(self):
        if int in self.board:
            return True
        


    # is_game_over() Returns true if the game board is full or a player has won.
    def is_game_over(self):
        # if self.is_full == True:
        #     return True
        # elif self.calc_winner
        


# player1 = Player('Toby', 'X')
# player2 = Player('Jon', 'O')
# namecheck = Game()

namecheck.__repr__()


# if player1.token = 


def main():
    placement1 = []
    placement2 = []

    while True:
        
        move(i, player1)
        if is_full():
            print("board is full tie-game")
            break
        move(i, player2)
        if is_full():
            print("board is full tie-game")
            break

        else:
            break


# player1 = Player('Toby', 'X')
# player2 = Player('Jon', 'O')





# main()






        


# player1 = Player()


# game = [[1,  2,  3],
#         [4,  5,  6],
#         [7,  8,  9]]
# for row in game:
#     print(row)

   