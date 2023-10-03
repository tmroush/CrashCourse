filename = "learning_python.txt"

with open(filename) as file_object:
    contents = file_object.read()

print("read the file as one big chunk:")
print(contents)



