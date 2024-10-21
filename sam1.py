numWrods = 0
dictionary = {}
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        words = line.split()
        numWrods += len(words)
        for elem in words:
            if elem in dictionary:
                dictionary[elem] += 1
            else:
                dictionary[elem] = 1
print(numWrods)
list = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
print(list[0])
