def func(tp, id):
    a, b = -1, -1
    for i in range(len(tp)):
        if tp[i] == id:
            if a != -1:
                b = i
            else:
                a = i
    return tp[a:b]


if __name__ == "__main__":
    print(func((0, 1, 8, 8, 5, 2, 6, 1, 6, 7, 6, 4, 2), 0))
