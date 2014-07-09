import re
from board import Board


board = Board()
board.populate_vehicles()

while True:
    board.draw()
    cmd = raw_input("Give a shoot: ").lower()
    coordinate_match = re.match(r"([A-La-l])(\d+)", cmd.upper())
    if cmd == "reveal":
        board.draw(reveal=True)
    elif coordinate_match is not None:
        column = coordinate_match.groups()[0]
        row = coordinate_match.groups()[1]
        if column not in Board.columns or row not in Board.rows:
            print("Error: bad coordinate")
            continue
        board.shoot(cmd.upper())
