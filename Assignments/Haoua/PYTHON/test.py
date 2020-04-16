import random 

class Player:
    def __init__(self, player_name, player_token): #Creates class that defines the input for user name and choice of token.
        self.player_name = player_name
        self.player_token = player_token
    
    def name(self):  #Defines user input of name.
        name = input('Please enter your name: ')
        return name
    
    def token(self): #Defines user choice of X or O
        token = input('Would you like X\'s or O\'s? : ').lower()
        if token == 'o':
            return 'O'
        else:
            token == 'x'
            return 'X'

#[['x', 'o', 'o'], ['o', 'x', 'o'], ['o', 'x', 'o']] --> some visual representation with a normal tic-tac-to layout
class Game:
    board_layout = [['', '', ''], ['', '', ''], ['', '', '']] # working on board layout
    def __init__(self, board):
        self.board = board_layout
   
    def __repr__(self): #Returns a pretty string representation of the game board
        self.visual_board_layout = [ 
                             [" ","|"," ",'|'," "],  #referenced above in line 22
                             ["-","-","-","-","-"],
                             [" ","|"," ","|"," "],
                             ["-","-","-","-","-"],
                             [" ","|"," ","|"," "]
                            ]
        # CODE GOES HERE that will place a move into the visual representation of the board. 
# """
# if we want "x" in the middle: 

# user_input = "x"
# user_positon = 5
# in_play_board[2][2] = user_position

# reprint the board with the replacement. in_play_board = board

# # for i in board:
# #     print(i[0], i[1], i[2])
    
#     def move(self, playable_board, player_input): #Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
#         self.playable_board = 
#         self.player_input = input('Please enter the position to place your piece (1-9): ')
#         space = []        
#         coordinates = {
#                        "1" : playable_board[0][0]
#                        "2" : playable_board[0][2]
#                        "3" : playable_board[0][4] 
#                        "4" : playable_board[2][0] 
#                        "5" : playable_board[2][2] 
#                        "6" : playable_board[2][4]
#                        "7" : playable_board[4][0]
#                        "8" : playable_board[4][2]
#                        "9" : playable_board[4][4]
#                       }
        board = [['', '', ''], ['', '', ''], ['', '', '']]
                # user token is x and they input 0,0
        token = 'x'
        move = [0,0]
        board.update(token, move)
        [['x', '', ''], ['', '', ''], ['', '', '']]

        token = 'o'
        move = [2,1]
        board.update(token, move)
        [['x', '', ''], ['', '', ''], ['', 'o', '']]

# #         position = coordinates[player_input]
        
# #         space.append(player_input) #keeps track of what positions have been filled
        
# #         """
# #         if player_input not in space:
# #             position = coordinates[player_input] (?)
# #         else:
# #             loop back to input
# #         """
        
        
# #         return position
        
# #     def calc_winner(self): #What token character string has won or None if no one has.
        
# #         winning_combos = [
# #                           ['1','2','3']
# #                           ['4','5','6']
# #                           ['7','8','9']
# #                           ['1','4','7']
# #                           ['2','5','8']
# #                           ['3','6','9']
# #                           ['1','5','9']
# #                           ['3','5','7']
# #                          ]
        
# #             if:
# #                 pass
# #             #then winning result
        
# #             else:
# #                 pass
# #                 #continue playing
       
    
# #     def is_full(self): #Returns true if the game board is full.
# #         if count == 9:
# #             print("It's a tie!")
    
# #     def is_game_over(self): #Returns true if the game board is full or a player has won.
# #         if count == 9:
# #             print("Game over")
# #             print("It's a tie!")




    


# # def main():

# #     while True:
# #         play = input('Would you like to play a game of Tic-tac-toe?\n Type: yes OR no')
# #         if play == 'yes':
# #             continue
# #         elif play == 'no':
# #             break
            
# #     player1_name = Player.name(self)
# #     player1_token = Player.token(self)
# #     player1 = Player(player1_name, player1_token)
# #     player1_moves = []

# #     player2_name = Player.name(self)
# #     player2_token = Player.token(self)
# #     player2 = Player(player2_name, player2_token)
# #     player2_moves = []

    
# #     main function to start the game
# #     def play_game():
# #          board, winner,counter = creat_board (), 0,1
# #          print(board)
# #          sleep(2)  # the sleep(2) suspends the fuction a given amount of seconds

# #         while winner == 0:
# #             for player in [1,2]:
# #                 board = random_place(board,playeR)  #come back to this(because there is a player1_name and player2_name)
# #                 print('board after'+ str(counter) + "move")
# #                 print(board)
# #                 sleep(2) 
# #                 counter += 1
# #                 winner = evaluate(board)
# #                 if winner != 0:
# #                     break
# #         return(winner)
    
    

# # #checking for whether the player has three in a row
# # def col_win(board,player):
# #     for x in range (len(board)):
# #         win = True

# #         for y in range(len(board)):
# #             if board [y][x] != player:
# #                 win = False 
# #                 continue
        
# #         if win == True: 
# #             return(win)
    
# #     return(win)
    
# # #Determines who the winner is a.k.a. "Driver Code"
# # print("The winner is:"+ str(play_game()))

# main()