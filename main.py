from board import Board

game_active = True
board = Board()

# main game loop
while game_active:

    # take the users play and inputs it into play variable
    input_string = input(f"It is the {board.player}'s turn, please choose a row and column (i.e. 1,3): ")
    split_input = input_string.strip("()").split(',')
    play = tuple(map(int, split_input))

    # update board state and display
    if 0 < play[0] < 4  and  0 < play[0] < 4:
        board.update_board(play)
        board.display_board()
    else:
        print("Values must be between 1 and 3, try again.")
        continue
    # check to see if win condition has happened
    winner, game_end = board.check()
    if game_end:
        game_active = False
        if winner == 'draw':
            print("No one wins, it's a draw...")
        else:
            print(f"{winner} is the winner!")

    # switch players
    board.switch_player()