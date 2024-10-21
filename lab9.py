def longestWord(file):
    with open(file, encoding="utf-8") as f:
        words = f.read().split()
        maxLength = len(max(words, key=len))
        for word in words:
            if len(word) == maxLength:
                res = word
        if len(res) == 1:
            return res[0]
        else:
            return res


print(longestWord("input1.txt"))
