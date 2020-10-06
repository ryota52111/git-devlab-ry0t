class Test():
    y = 10

    def __init__(self):
        self.x = 5

    def get_y(self):
        return Test.y
        # return self.__class__.y
        # return self.y

    def set_y(self):
        Test.y = 555
        self.__class__.y = 555
        self.y = 555



y = Test.y
print("Test.y:", y)

Test.y = 500

t1 = Test()
print("t1.y:", t1.y)
# t1.y = 5

t2 = Test()
Test.y = 1000
print("t1.y:", t1.y)
print("get_y:", t1.get_y())
print("t2.y:", t2.y)