class Board():

    def __init__(self):
        self.row1 = ["⬜️", "⬜️", "⬜️"]
        self.row2 = ["⬜️", "⬜️", "⬜️"]
        self.row3 = ["⬜️", "⬜️", "⬜️"]
        self.player = "X"
        self.display_board()
        self.moves = []

    def display_board(self):
        print(f"{self.row1}\n{self.row2}\n{self.row3}")

    def switch_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def update_board(self, row_column):
        if row_column not in self.moves:
            self.moves.append(row_column)
            row = row_column[0]
            column = row_column[1]
            if row == 1:
                self.row1[column - 1] = self.player
            elif row == 2:
                self.row2[column - 1] = self.player
            else:
                self.row3[column - 1] = self.player
        else:
            self.switch_player()
            print('That location is already taken, choose an empty ("⬜️") location')

    def check(self):
        if self.row1[0] == self.player and self.row1[1] == self.player and self.row1[2] == self.player:
            winner = self.player
            game_end = True
            return winner, game_end
        elif self.row2[0] == self.player and self.row2[1] == self.player and self.row2[2] == self.player:
            winner = self.player
            game_end = True
            return winner, game_end
        elif self.row3[0] == self.player and self.row3[1] == self.player and self.row3[2] == self.player:
            winner = self.player
            game_end = True
            return winner, game_end
        elif self.row1[0] == self.player and self.row2[0] == self.player and self.row3[0] == self.player:
            winner = self.player
            game_end = True
            return winner, game_end
        elif self.row1[1] == self.player and self.row2[1] == self.player and self.row3[1] == self.player:
            winner = self.player
            game_end = True
            return winner, game_end
        elif self.row1[2] == self.player and self.row2[2] == self.player and self.row3[2] == self.player:
            winner = self.player
            game_end = True
            return winner, game_end
        elif self.row1[0] == self.player and self.row2[1] == self.player and self.row3[2] == self.player:
            winner = self.player
            game_end = True
            return winner, game_end
        elif self.row1[2] == self.player and self.row2[1] == self.player and self.row3[0] == self.player:
            winner = self.player
            game_end = True
            return winner, game_end
        elif "⬜️" not in self.row1 and "⬜️" not in self.row2 and "⬜️" not in self.row3:
            winner = 'draw'
            game_end = True
            return winner, game_end
        else:
            winner = None
            game_end = False
            return winner, game_end
