num = -5
# if num > 0:
#     if (num % 2) == 1:
#         print("plus, odd")



# if num > 0 and (num % 2) == 1:
#     print("plus, odd")

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)


person = {
    "member": False,
    "age": 18,
    "paid": False,
}

if (person ["member"] or 
    person["age"] >= 18 and person["paid"]):
    print("You can use a sports club.")
else:
    print("You can't use a sports club.")
