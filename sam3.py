one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 52, 98]
three = [4, 21, 37, 56, 84]


def minS(list1, list2, list3):
    a, b, c = min(list1), min(list2), min(list3)
    p = (a + b + c) / 2
    if (p - a <= 0) or (p - b <= 0) or (p - c <= 0):
        print("No")
    else:
        print(p * (p - a) * (p - b) * (p - c) ** 0.5)


def maxS(list1, list2, list3):
    a, b, c = max(list1), max(list2), max(list3)
    p = (a + b + c) / 2
    if (p - a <= 0) or (p - b <= 0) or (p - c <= 0):
        print("No")
    else:
        print(p * (p - a) * (p - b) * (p - c) ** 0.5)


minS(one, two, three)
maxS(one, two, three)
