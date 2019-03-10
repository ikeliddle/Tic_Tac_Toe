
class Board():

    counter = 1
    player_turn = None
    three_in_a_row = 0
    over_9_turns = 0

    def __init__(self):
        self.board = [["Y"],
                      ["3 ", '-', '-', '-'],
                      ["2 ", '-', '-', '-'],
                      ["1 ", '-', '-', '-'],
                      ["  ", "1", "2", "3", "X"]]

    def board_edit(self):
        print()
        for i in self.board:
            print(i)
        while Board.three_in_a_row == 0 and Board.over_9_turns < 9:
            if Board.counter % 2 == 0:
                Board.player_turn = "x"
            else:
                Board.player_turn = "o"
            if Board.player_turn == "o":
                print()
                print("It is O's turn")
                print("Please put the position in the coordinate format -- x,y")
                b_position = input("Where do you want to place your piece? ")
                print()
                x_coord = int(b_position[0])
                y_coord = int(b_position[2])
                if y_coord == 1:
                    y_row = self.board[3]
                elif y_coord == 2:
                    y_row = self.board[2]
                elif y_coord == 3:
                    y_row = self.board[1]
                if y_row[x_coord] == "-":
                    y_row[x_coord] = "O"
                    Board.over_9_turns += 1
                    Board.counter += 1
                else:
                    print("This position has already been taken!")
                    print()
                if self.board[1][1] == "O" and self.board[1][2] == "O" and self.board[1][3] == "O":
                    print("O wins!")
                    Board.three_in_a_row += 1
                elif self.board[2][1] == "O" and self.board[2][2] == "O" and self.board[2][3] == "O":
                    print("O wins!")
                    Board.three_in_a_row += 1
                elif self.board[3][1] == "O" and self.board[3][2] == "O" and self.board[3][3] == "O":
                    print("O wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][1] == "O" and self.board[2][1] == "O" and self.board[3][1] == "O":
                    print("O wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][2] == "O" and self.board[2][2] == "O" and self.board[3][2] == "O":
                    print("O wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][3] == "O" and self.board[2][3] == "O" and self.board[3][3] == "O":
                    print("O wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][1] == "O" and self.board[2][2] == "O" and self.board[3][3] == "O":
                    print("O wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][3] == "O" and self.board[2][2] == "O" and self.board[3][1] == "O":
                    print("O wins!")
                    Board.three_in_a_row += 1
                else: pass
                
            elif Board.player_turn == "x":
                print()
                print("It is X's turn")
                print("Please put the position in the coordinate format -- x,y")
                b_position = input("Where do you want to place your piece? ")
                print()
                x_coord = int(b_position[0])
                y_coord = int(b_position[2])
                if y_coord == 1:
                    y_row = self.board[3]
                elif y_coord == 2:
                    y_row = self.board[2]
                elif y_coord == 3:
                    y_row = self.board[1]
                if y_row[x_coord] == "-":
                    y_row[x_coord] = "X"
                    Board.over_9_turns += 1
                    Board.counter += 1
                else:
                    print("This position has already been taken!")
                    print()
                if self.board[1][1] == "X" and self.board[1][2] == "X" and self.board[1][3] == "X":
                    print("X wins!")
                    Board.three_in_a_row += 1
                elif self.board[2][1] == "X" and self.board[2][2] == "X" and self.board[2][3] == "X":
                    print("X wins!")
                    Board.three_in_a_row += 1
                elif self.board[3][1] == "X" and self.board[3][2] == "X" and self.board[3][3] == "X":
                    print("X wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][1] == "X" and self.board[2][1] == "X" and self.board[3][1] == "X":
                    print("X wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][2] == "X" and self.board[2][2] == "X" and self.board[3][2] == "X":
                    print("X wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][3] == "X" and self.board[2][3] == "X" and self.board[3][3] == "X":
                    print("X wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][1] == "X" and self.board[2][2] == "X" and self.board[3][3] == "X":
                    print("X wins!")
                    Board.three_in_a_row += 1
                elif self.board[1][3] == "X" and self.board[2][2] == "X" and self.board[3][1] == "X":
                    print("X wins!")
                    Board.three_in_a_row += 1
                else: pass
            print()
            for i in self.board:
                print(i)


b1 = Board()
b1.board_edit()
