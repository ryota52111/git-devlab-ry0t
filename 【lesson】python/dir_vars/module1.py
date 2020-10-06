CONSTANT = "ABC"


def add(a, b):
    return a + b


class Human(object):
    y = 100

    def __init__(self):
        self.x = 5
    
    def get_x(self):
        return self.x


class Student(Human):
    z = 1000

    def __init__(self):
        super().__init__()
        self.xyz = 50
    
    def get_xyz(self):
        return self.xyz