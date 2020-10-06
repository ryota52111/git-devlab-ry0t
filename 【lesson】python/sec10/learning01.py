# filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\text_sample.txt"

# contents = """\
# ABC
# あいうえお
# DEF
# 123
# """


# with open(filename, "w", encoding="utf-8") as f:
#     f.write(contents)

# filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\text_sample.txt"

# l = ["Python","C++","Ruby","Java"]

# with open(filename, "w", encoding="utf-8") as f:
#     # f.writelines(l)

#     f.write("\n".join(l))
#     f.write("\n")

# filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\text_sample.txt"

# contents = "PostScript\n"

# with open(filename, "a", encoding="utf-8") as f:
#     f.write(contents)

filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\text_sample.txt"


#Read
with open(filename, "r", encoding="utf-8") as f:
    # contents = f.read()
    # contents = f.readlines()


# print(contents)

    for line in f:
        print(line)