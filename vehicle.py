class Vehicle:
    def __init__(self, count, size, initials):
        self.count = count
        self.size = size
        self.initials = initials
    
    def __str__(self):
        return self.initials


class MilitaryTruck(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(2, 4, 'Mt')


class Tank(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(3, 4, 'Tk')


class Howitzer(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(4, 2, 'Hr')


class Jeep(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(5, 1, 'Jp')


vehicles = [MilitaryTruck, Tank, Howitzer, Jeep]
