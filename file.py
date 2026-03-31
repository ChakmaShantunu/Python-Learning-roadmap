f = open("data.txt", "r")
content = f.read()
print(content)
f.close()

f = open("data.txt", "w")
f.write("Hello boss. Welcome to python learning")
f.close()