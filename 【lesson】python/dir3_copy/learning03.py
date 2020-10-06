
learning01 = r"C:\Users\r_sas\Desktop\hello_sublime\dir1\dir2\dir3\learning01.py"
learning02 = r"C:\Users\r_sas\Desktop\hello_sublime\dir1\dir2\dir3\learning02.py"

# import pathlib
# pathlib.Path(learning02).touch()

# import os
# # os.remove(learning02)

# os.rename(learning01, learning02)

# import shutil
# shutil.copy(learning02, learning01)

# learning02 = r"C:\Users\r_sas\Desktop\hello_sublime\dir1\dir2\learning02.py"
# move_to = r"C:\Users\r_sas\Desktop\hello_sublime\dir1\dir2\dir3\xxx.py"

# import shutil
# shutil.move(learning02, move_to)

dir3 = r"C:\Users\r_sas\Desktop\hello_sublime\dir1\dir2\dir3"
copy_to = r"C:\Users\r_sas\Desktop\hello_sublime\dir3_copy"

import shutil
shutil.copytree(dir3, copy_to)