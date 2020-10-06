# d1 = {
#     "key1": 1,
#     "key2": 2,
# }

# d2 = d1.copy()
# d2["key2"] = 10
# d2["key3"] = 30

# print("d1", d1, id(d1))
# print("d2", d2, id(d2))

# d1 = {
#     "key": {"subkey": 1}
# }

# import copy
# d2 = copy.deepcopy(d1)
# d2["key"]["subkey"] = 100

# print("d1", d1, id(d1))
# print("d2", d2, id(d2))


set()

# s = {1, 2, 3, 3, 1}
# print(s, type(s))

# s = set([1, 2, 3, 1, 3])
# print(s, type(s))

# s = set("ABCABBBC")
# print(s, type(s))

# l = list({"A", "B", "C"})
# print(l)

l = [1, 4, 2, 3, 3, 2, 4]
# s = set(l)
# l = list(set(l))
l = sorted(set(l), key=l.index)
print(l)