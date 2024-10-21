numWrods = 0
numChars = 0
numLines = 0
dictionary = {}
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        numLines += 1
        words = line.split()
        numWrods += len(words)
        for elem in words:
            numChars += sum(map(str.isalpha, elem))
print(numChars)
print(numWrods)
print(numLines)
