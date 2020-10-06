class Human(object):
    def __init__(self):
        self.name = ""
        self.age = 0

    def get_name (self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age (self):
        return self.age

    def set_age(self, age):
        self.age = age

manA = Human()


# print("manA.name:", manA.name)
# pirnt("manA.age:", manA.age)

manA.set_name("Taro")
name = manA.get_name()
print(name)

manA.set_age(20)
age = manA.get_age()
print(age)