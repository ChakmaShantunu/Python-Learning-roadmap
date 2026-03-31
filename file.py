# f = open("data.txt", "r")
# content = f.read()
# print(content)
# f.close()

# f = open("data.txt", "w")
# f.write("Hello boss. Welcome to python learning")
# f.close()

# f = open("data.txt", "a")
# f.write("\nNew line added")
# f.close()

with open("data.txt", 'w') as file: 
    file.write("Hello boss. Welcome to python learning")

with open("data.txt", 'r') as file: 
    content = file.read()
    print(content)