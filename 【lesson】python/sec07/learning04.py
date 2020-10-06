class Test():
    y = 10

    def __init__(self):
        self.x = 5

    @staticmethod
    def get_y():
        return Test.y

    @staticmethod
    def set_y():
        Test.y = 555
    
    @staticmethod
    def get_x():
        t = Test()
        return t.x


Test.set_y()
print(Test.get_y())
print(Test.get_x())