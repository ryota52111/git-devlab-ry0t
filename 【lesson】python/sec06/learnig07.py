# d = {
#     "key4": 3,
#     "key2": 1,
#     "key1": 2,
#     "key3": 4
# }

# # for key in sorted(d, reverse=True):
# #     print(key)

# # for item in d.values():
# #     print(item)

# # print("****************************************")

# # for item in sorted(d.values(), reverse=True):
# #     print(item)

# # for key, item in d.items():
# #     print(key)
# #     print(item)

# for key, item in sorted(d.items(), reverse=True):
#     print(key, item)

# print("****************************************")

# for key, item in sorted(d.items(), key=lambda t:t[1], reverse=True):
#     print(key, item)