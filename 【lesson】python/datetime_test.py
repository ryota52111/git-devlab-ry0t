# import datetime

# dt = datetime.datetime.now()
# print(dt, type(dt))

# # print(dt.year)
# # print(dt.month)
# # print(dt.day)
# # print(dt.hour)
# # print(dt.minute)
# # print(dt.second)
# # print(dt.microsecond)

# iso = dt.isoformat()
# print("iso format:", iso)

# str_format = dt.strftime("%Y/%m/%d  %H:%M:%S")
# print("str format:", str_format)

# import datetime


# dt1 = datetime.datetime(2019, 1, 1, 12, 30, 00)
# dt2 = datetime.datetime(2019, 8, 21, 15, 30, 00)

# result = (dt1 < dt2)
# print(result)

# import datetime

# start = datetime.datetime(2020, 4, 3, 18)
# end = datetime.datetime.now()


# delta = end - start
# print(delta, type(delta))

# print("*****")
# print(delta.days)
# print(delta.seconds)
# print(delta.microseconds)
# print("*****")

# h = int(delta.seconds / 3600)
# m = int((delta.seconds - (h * 3600)) / 60)
# s = delta.seconds - (h * 3600) - (m * 60)
# print("{}:{}:{}".format(h, m, s))

import datetime

now = datetime.datetime.now()
delta = datetime.timedelta(days=-10, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=1)

dt = now + delta
print(dt)