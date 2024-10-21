str = (
    "Hello, world! Python IS the programming language of thE future. My EMAIL is...\n"
    "PYTHON is awesome!!!!"
)
with open("input.txt", "r") as file:
    forbList = list(file.readline().split(" "))
print(forbList)
nlIndex = str.index("\n")
inputList = str.split()
for i in range(len(inputList)):
    for j in range((len(forbList))):
        if forbList[j] in inputList[i].lower():
            for k in forbList[j]:
                inputList[i] = inputList[i].lower().replace(k, "*")

output = ""
for i in inputList:
    output += i + " "
    if len(output) == nlIndex + 1:
        output += "\n"
print(output)
