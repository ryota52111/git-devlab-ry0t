
# list_D2 = [
#     ["A" , "B" , "C"],
#     list(range(3))
# ]
# print(list_D2)

# import glob
# import pprint
# dir_list = glob.glob("c:/*")
# pprint.pprint(dir_list)

# tuple

# # t = (1, 2, 3)
# # t = (1, 2, 3)
# # t = tuple("ABC")
# # t = tuple(range(5))
# # t = tuple([1, 2, 3])
# # t = (1,)
# # l = []
# # 
# tuple_2D = (
#     (1, 2, 3),
#     [4, 5, 6]
# )
# print(tuple_2D[0][0])
# print(tuple_2D[1][1])

# num_tuple = (1,2,3,4,5,6,7,8,9,10)

# num_tuple[0]
# num_tuple[1]
# num_tuple[100]
# num_tuple[-1]
# num_tuple[-3]

# num_tuple[0:2]
# num_tuple[0:-1]
# num_tuple[:-1]
# num_tuple[:-1]
# num_tuple[:-3]
# num_tuple[3:]
# num_tuple[:]
# num_tuple[::2]

# year, month, day = 2019, 7, 24
# print(year)
# print(month)
# print(day)


# al_tuple = ("A", "B" ,"C")
# al_str = "_".join(al_tuple)
# print(al_str)

# num_tuple1 = (1, 2, 3)
# num_tuple2 = num_tuple1

# num_tuple3 = ([1, 2, 3], [4, 5, 6])
# num_tuple4 = num_tuple3

# import copy
# # num_tuple5 = ([1, 2, 3],[4, 5, 6])
# # # num_tuple6 = num_tuple5
# # num_tuple6 = copy.deepcopy(num_tuple5)
# # num_tuple6[0][1] = 200
# # print(num_tuple5)
# # print(num_tuple6)
# dict
# d = {"key": "value"}

# my_profile = {
#               "first_name": "Tatsuya",
#               "last_name": "Nakamori",
#               "age" :"32",
#               "phone": "090-1234-5678",
# }

# my_profile["city"] = "Tokyo"
# my_profile["age"] = 33
# my_profile["friends"] = ["Taro", "Hanako"]



# import pprint
# pprint.pprint(my_profile)
# print(my_profile)

# print(my_profile["first_name"])
# print(my_profile["age"])
# print(my_profile["WWW"])

# my_friends = {
#     "Tom":{"age": 32,"phone":"090-1234-5678"},
#     "Hanako":{"age": 26,"phone":"080-1234-5678"}
# }

# my_friends["Tom"]["hobby"] = "Reading"

# import pprint
# pprint.pprint(my_friends)
# # print(my_friends["Hanako"]["age"])

# # my_profile = {
# #               "first_name": "Tatsuya",
# #               "last_name": "Nakamori",
# #               "age" :"32",
# #               "phone": "090-1234-5678",
# # }

# # keys = my_profile.keys()
# # # print(keys[0])
# # print(type(keys))
# # print(list(keys))

# # values = my_profile.values()
# # print(values)
# # # print(values)
# # print(list(values))

# # import pprint
# # items = my_profile.items()
# # print(items)
# # print(type(items))
# # pprint.pprint(list(items))

# my_profile = {
#               "first_name": "Tatsuya",
#               "last_name": "Nakamori",
#               "age" :"32",
#               "phone": "090-1234-5678",
#               "friends":["Taro"]
# }

# # additional_date = {
# #     "friends":["Taro","Hanako"],
# #     "phone":"080-9876-5432"
# # }

# # my_profile.update(additional_date)
# # import pprint
# # pprint.pprint(my_profile)

# # value = my_profile["friends"]
# value = my_profile.get("friends", [])


# print(value)
# print(type(value))

my_profile = {"friends": ["Hanako"]}
print("1:", my_profile)

# my_profile.setdefault("friends", [])
my_profile["friends"] = []
print("2:", my_profile)

my_profile["friends"].append("Tom")
print("3:",my_profile)






