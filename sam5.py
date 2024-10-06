one = [1, 1, 3, 3, 1]
two = [5, 5, 5, 5, 5, 5, 5]
three = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def whyamIdoingit(list):
    set1 = set(list)
    for i in range(len(list)):
        c = list.count(list[i])
        if c > 1:
            a = str(list[i])
            for j in range(c - 1):
                a += str(list[i])
                set1.add(a)
    print(set1)


if __name__ == "__main__":
    whyamIdoingit(one)
    whyamIdoingit(two)
    whyamIdoingit(three)
