class Vehicle(object):
    def __init__(self):
        pass

    def __str__(self):
        return self.initials


class MilitaryTruck(Vehicle):
    count = 2
    size = 4
    initials = 'Mt'

    def __init__(self):
        super(Vehicle, self).__init__()


class Tank(Vehicle):
    count = 3
    size = 4
    initials = 'Tk'

    def __init__(self):
        super(Vehicle, self).__init__()


class Howitzer(Vehicle):
    count = 4
    size = 2
    initials = 'Hr'

    def __init__(self):
        super(Vehicle, self).__init__()


class Jeep(Vehicle):
    count = 4
    size = 2
    initials = 'Jp'

    def __init__(self):
        super(Vehicle, self).__init__()


vehicles = [MilitaryTruck, Tank, Howitzer, Jeep]
