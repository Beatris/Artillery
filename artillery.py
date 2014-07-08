from board import Board

board = Board()
board.draw()

reveal = raw_input()
if reveal == "Reveal":
    board.reveal()
