# s = "{language} {version} {greetin}!".format(
#     greetin="hello", language="python" , version=3)
# print(s)



# "W:/sec03/learning08.py"

# template = "W:/sec{sec:04}/learning{filenum:02}.py"
# path = template.format(sec=3, filenum=8)
# print(path)

# s = "{:04}".format(5)
# s = "{:>5}".format("AAA")
# s = "{:<5}".format("AAA")
# s = "{:^5}".format("AAA")
# s = "{:#^5}".format("AAA")
# s = "{:,}".format(1000000)

# s = "{:.3f}".format(0.12345)
# s = "{:,.3f}".format(100000000.12345)

# s = "{:,.3f}".format(100000000.12345)

# print(s)

# num_list1 = list(range(1, 6))
# num_list1 = [list(range(1, 6))]
# num_list2 = num_list1[:]

# num_list2[0][0] = 100

# print(num_list1)
# print(num_list2) 


import copy
num_list1 = [list(range(1, 6))] #[1, 2, 3, 4, 5]
# num_list2 = num_list1[:]
num_list2 = copy.deepcopy(num_list1)
num_list2[0][0] = 100

print("list1:", num_list1, type(num_list1), id(num_list1))
print("list2:", num_list2, type(num_list2), id(num_list2))
print("list1[0]:", num_list1[0], type(num_list1[0]), id(num_list1[0]))
print("list2[0]:", num_list2[0], type(num_list2[0]), id(num_list2[0]))