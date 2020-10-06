# def to_even(num):
#     if num % 2 == 1:
#         return num + 1
#     else:
#         return num

    
#     print("xxx")


# result = to_even(99)
# print(result)

# def plus(num1, num2):
#     return num1 + num2


# result = plus(100)
# print(result)

# def plus_5(num1, num2, num3, num4, num5):
#     total = num1 + num2 + num3 + num4 + num5
#     return total


# result = plus_5(1, 2, 3, 0, 0)
# print(result)

# #****************************************************
# def plus_list(num_list):
#     total = 0
#     for num in num_list:
#         total += num
#     return total

# result = plus_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(result)


# def division(divisor, dividend):
#     print("{} / {}".format(divisor, dividend))
#     return divisor / dividend

# result = division(dividend=5, divisor=2)
# print(result)

# def print_greeting(greeting="Good Morning!"):
#     print(greeting)
#     return

# print_greeting(greeting="Good Evening")

# def func(a, b, c, d=0, e=0, f=0):
#     print(a, b, c, d, e, f)
#     return

# func(100, 200, 300)

# def func(l=None):
#     if l is None:
#         l = []
#     l.append(10)
#     return

# print(func())
# print(func())
# print(func())

# max1 = max(1, 2, 3, 4, 5, 11, 12, 13, 14, 15)
# max2 = max(5, 6)

# print(max1)
# print(max2)

# def function(*args):
#     print(args, type(args))
#     return

# function(1, 2, 3, 4, 5)
# function(*(1, 2, 3, 4, 5))

# def func(a, b, c, *args):
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#     print("args:", args)

# func(1, 2, 3, 4, 5, 6, 7, 8, 9)

# def func(**kwargs):
#     print(kwargs, type(kwargs))

# # func(a=1, b=2)

# d = {"a": 1,"b": 2}
# func(**d)

# "{drive}:/{sec}/{filename}.{extension}".format(drive="W",sec="sec06",filename="learning13",extension="py")

# d = {
#     "drive": "W",
#     "sec": "sec06",
#     "filename": "learning13",
#     "extension": "py"
# }
# s = "{drive}:/{sec}/{filename}.{extension}".format(**d)
# print(s)

def func(a, b, *args, c=0, d=0, **kwargs):
    print("a", a)
    print("b", b)
    print("args", args)
    print("c", c)
    print("d", d)
    print("kwargs", kwargs)


func(1, 2, 3, 4, c=100, d=200, e=300, f=400)






















