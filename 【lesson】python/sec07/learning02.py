class Human(object):
    def __init__(self , name="", age=0):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def set_name(self, name):
        self.name = name
    
    def get_age(self):
        return self.age

    def set_age(self, age):
        return self.age

    def set_age(self, age):
        self.age = age

class Student(Human):
    def __init__(self, name="", age=0):
        super().__init__(name, age)
        self.academic_ability = {}

    def study(self, subject):
        self.academic_ability.setdefault(subject, 0)
        self.academic_ability[subject] += 5

    def get_academic_ability(self):
        return self.academic_ability



manA = Student("Taro", 20)

for num in range(5):
    manA.study("Japanese")

for num in range(10):
    manA.study("English")

for num in range(9):
    manA.study("Math")

print(manA.get_academic_ability())