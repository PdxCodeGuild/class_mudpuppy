#Tic Tac Toe Lab, April 21st, 2020

class Player:
    def __init__(self, token):
        self.token = token


class Board:
    def __init__(self):
        self.board = [[' ', '|', ' ', '|', ' '], 
        [' ', '|', ' ', '|', ' '],
        [' ', '|', ' ', '|', ' ']]

        return None
    
    def print_board(self):
        ls2 = '\n'.join([''.join(inner_list) for inner_list in self])
        print(ls2)
        return ls2
    
#     def print_board(self, ls):
#         ls2 = '\n'.join([''.join(inner_list) for inner_list in ls2])
        

# class Game:
#     def __init__(self)
#     self.board = []

#     def __repr__(self):

test = Board()
test.print_board()
p1 = Player('X')
p2 = Player('O')


