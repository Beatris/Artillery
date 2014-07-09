from vehicle import vehicles
from random import randint

class Board:
    rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    occupated_cells = {}
    shoots = []
    hits = []


    def place_vehicle(self, vehicle):
        taken = False
        placed = False

        while not placed:
            ori = randint(0, 1)
            if not ori:
                col = randint(0, len(self.columns) - 1)
                row = randint(0, len(self.rows) - vehicle.size - 1)
                for i in range(vehicle.size):
                    if self.occupated_cells.get("{}{}".format(self.columns[col], self.rows[row+i])) is not None:
                        taken = True
                        break
                if not taken:
                    for i in range(vehicle.size):
                        self.occupated_cells["{}{}".format(self.columns[col], self.rows[row+i])] = vehicle
                    placed = True
            else:
                col = randint(0, len(self.columns) - vehicle.size - 1)
                row = randint(0, len(self.rows) - 1)

                for i in range(vehicle.size):
                    if self.occupated_cells.get("{}{}".format(self.columns[col], self.rows[row])) is not None:
                        taken = True
                        break

                if not taken:
                    for i in range(vehicle.size):
                        self.occupated_cells["{}{}".format(self.columns[col+i], self.rows[row])] = vehicle
                    placed = True
            taken = False

    def populate_vehicles(self):
        for vehicle_cls in vehicles:
            vehicle_instance = vehicle_cls()
            for _ in range(vehicle_instance.count):
                vehicle = vehicle_cls()
                self.place_vehicle(vehicle)

    def draw(self, reveal=False):
        print("      " + '    '.join(self.columns))
        for row in self.rows:
            line = ""
            for column in self.columns:
                cell = "{}{}".format(column, row)
                if reveal:
                    sign = self.occupated_cells.get(cell, '  ')
                elif cell in self.hits:
                    sign = "X "
                elif cell in self.shoots:
                    sign = "0 "
                else:
                    sign = "  "
                line += " {}  ".format(sign)
            print("{:>2}   {}".format(row, line))

    def shoot(self, cell):
        if cell in self.shoots:
            print("You have already shoot at {}".format(cell))
        else:
            print("Shooting at {}".format(cell))
            self.shoots.append(cell)
            possible_vehicle = self.occupated_cells.get(cell)
            if possible_vehicle is not None:
                self.hits.append(cell)
                print("Hit!")
            else:
                print ("You miss")
