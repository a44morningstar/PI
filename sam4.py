one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]


def fixIt(list):
    newList = []
    for i in range(len(list)):
        if list[i] == 5 or list[i] == 4:
            newList.append(list[i])
        elif list[i] == 3:
            newList.append(4)
    return newList


if __name__ == "__main__":
    print(fixIt(one))
    print(fixIt(two))
    print(fixIt(three))
