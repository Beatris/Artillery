from vehicle import vehicles
from random import randint, choice

class Board:
    rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    #cells_list = [(col + row) for col in columns for row in rows]
    #cells = dict((cell, 'O') for cell in cells_list)
    occupated_cells = {}
    can_be_positioned = True

    def ships_position(self):
        for vehicle_cls in vehicles:
            vehicle_instance = vehicle_cls()
            for _ in range(vehicle_instance.count):
                vehicle = vehicle_cls()
                direction = choice(["horizontal", "vertical"])
                start_row = choice(self.rows)
                start_col = choice(self.columns)
                start_cell = "{0}{1}".format(start_col, start_row)
                while start_cell in self.occupated_cells.keys():
                    start_row = choice(self.rows)
                    start_col = choice(self.columns)

                if direction == "horizontal":
                    for index in range(vehicle.size - 1):
                        next_col = self.columns[self.columns.index(start_col) + 1]
                        next_cell = "{0}{1}".format(next_col, start_row)
                        if next_cell in self.occupated_cells.keys():
                            can_be_positioned = False
                            break
                        self.occupated_cells[next_cell] = vehicle
                
                elif direction == "vertical":
                    for index in range(vehicle.size - 1):
                        next_row = self.columns[self.rows.index(start_row) + 1]
                        next_cell = "{0}{1}".format(next_row, start_col)
                        if next_cell in self.occupated_cells.keys():
                            can_be_positioned = False
                            break
                        self.occupated_cells[next_cell] = vehicle

    def draw(self):
        print("      " + '    '.join(self.columns))
        for row in self.rows:
            line = ""
            for column in self.columns:
                line += "Tt   "
            print("{:>2}    {}".format(row, line))

    def shoot(self):
        pass

    def reveal(self):
        print("      " + '    '.join(self.columns))
        for row in self.rows:
            line = ""
            for column in self.columns:
                current_cell = "{0}{1}".format(row, column)
                if current_cell in self.occupated_cells.keys():
                    line += "{}   ".format(str(self.occupated_cells[current_cell]))
                else:
                    line += "0    "
            print("{:>2}    {}".format(row, line))
