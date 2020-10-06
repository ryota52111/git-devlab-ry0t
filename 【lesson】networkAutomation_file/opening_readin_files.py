# f = open('configuration.txt', 'r')
# content = f.read(5)
# print(content)

# content = f.read(3)
# print(content)

# print(f.tell())

# f.seek(2)
# print(f.read(3))

# f.seek(0)
# print(f.read(1))

# print(f.closed)
# f.close()
# print(f.closed)

with open('configuration.txt', 'r') as file:
    print(file.read())

file.read()

print(file.closed)