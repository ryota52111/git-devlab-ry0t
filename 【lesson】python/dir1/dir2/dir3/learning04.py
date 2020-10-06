# import os

# path = r"C:\Users\r_sas\Desktop\hello_sublime\dir1\dir2\dir3"
# list_dir = os.listdir(path)
# print(list_dir)


# import  glob
# path = r":\Users\r_sas\Desktop\*"
# glob_list = glob.glob(path, recursive = True)

# import pprint
# pprint.pprint(glob_list) 

# import os

# path = r"C:\Users\r_sas\Desktop\hello_sublime\dir1\dir2\dir3\learning04.py"

# size = os.path.getsize(path)
# print(size)


# import datetime
# import os
# path = r"C:\Users\r_sas\Desktop\hello_sublime\dir1\dir2\dir3\learning04.py"
# c_timestamp = os.path.getctime(path)
# m_timestamp = os.path.getmtime(path)
# a_timestamp = os.path.getatime(path)

# c_time = datetime.datetime.fromtimestamp(c_timestamp)
# m_time = datetime.datetime.fromtimestamp(m_timestamp)
# a_time = datetime.datetime.fromtimestamp(a_timestamp)

# print(c_time)
# print(m_time)
# print(a_time)

# import subprocess

# path = r"C:\Users\r_sas"

# subprocess.run('explorer {}'.format(path))