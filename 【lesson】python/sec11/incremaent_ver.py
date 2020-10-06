#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
import shutil
import sys

def increment_file_ver(old_path):
    split_path = old_path.split("/")

    basename = split_path[-1]
    filename = basename.split(".")[0]
    old_ver = filename.split("_")[-1]

    ver_num = old_ver[1:]
    increment = int(ver_num) + 1
    new_ver = "v{:03}".format(increment)
    new_path = old_path.replace(old_ver, new_ver)
    return new_path

def main():
    print("sys.argv:", sys.argv, end="\n\n")

    if len(sys.argv) >= 2:
        file_from = sys.argv[1]

        file_to = increment_file_ver(file_from)

        while os.path.exists(file_to):
            print("Skip:", file_to)
            file_to = increment_file_ver(file_to)        
        


        shutil.copyfile(file_from, file_to)
        print()
        print("File From:", file_from)
        print("File To:", file_to)

    
    print()
    input("Please enter any key to exit.")


if __name__ == '__main__':
    main()
