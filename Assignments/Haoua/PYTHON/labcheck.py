class Game:
    def __init__(self):
        self.board = [10, 1, 2, 3, 4, 5, 6, 7, 8]
        self.win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
        self.moves_count = 0
    def create_board(self):
        print()
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print()
    def p1(self):
            try:
                print("PLAYER X")
                question = int(input("Type where your X should be placed\n"))
                if self.board[question] != "X" and self.board[question] != "O":
                    self.board[question] = "X"
                    self.create_board()
                    self.moves_count += 1
                else:
                    print("someone already took that row")
                    self.p1()
                self.check_win()
            except ValueError:
                print("Write a NUMBER from 0 to 8")
                self.p1()
    def p2(self):
        try:
            print("PLAYER 0")
            question = int(input("Type where your 0 should be placed\n"))
            if self.board[question] != "X" and self.board[question] != "O":
                self.board[question] = "O"
                self.create_board()
                self.moves_count += 1
            else:
                print("someone already took that row")
                self.p2()
            self.check_win()
        except:
            print("Write a NUMBER from 0 to 8")
            self.p2()
    def check_win(self):
        for a in self.win_conditions:
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == "X":
                print("PLAYER X WINS")
                self.play_again()
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == "O":
                print("PLAYER O WINS")
                self.play_again()
            elif self.moves_count == 9:
                print("A DRAW!")
                exit()
    def play(self):
        while True:
            self.p1()
            self.p2()
    def run(self):
        self.create_board()
        self.play()
    def play_again(self):
        while True:
            question = input("Do you want to play again? Type y or n\n")
            if question == "y":
                print("GLHF")
                self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.run()
            elif question == "n":
                print("See you next time!")
                quit()
            else:
                print("Thats not a valid option")
cos = Game()
cos.run()