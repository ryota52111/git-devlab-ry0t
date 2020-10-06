import shutil
from tkinter import filedialog

file_from = filedialog.askopenfilename()


split_path = file_from.split("\")
print(split_path)

basename = split_path[-1]
filename = basename.split(".")[0]
old_ver = filename.split("_")[-1]

ver_num = old_ver[1:]
increment = int(ver_num) + 1 # 2


new_ver = "v{:03}".format(increment) # v002
file_to = file_from.replace(old_ver, new_ver)


shutil.copyfile(file_from, file_to)
print("File From:", file_from)
print("File To:", file_to)

