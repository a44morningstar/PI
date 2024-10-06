from random import randint


def makeList():
    list = [randint(1, 50)] * randint(3, 10)
    return list


if __name__ == "__main__":
    res = []
    for i in range(randint(1, 3)):
        res.append(makeList())

    print(res)
