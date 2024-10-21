lines = ["line one", "line two", "line three"]
with open("input1.txt", "w") as file:
    for line in lines:
        file.write("\n" + line)
with open("input1.txt", "r") as file:
    for line in file:
        print(line)
