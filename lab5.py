def tsort(tuple1):
    for elem in tuple1:
        if not isinstance(elem, int):
            return tuple1
    return tuple(sorted(tuple1))


if __name__ == "__main__":
    print(tsort((7, 9, 5, 8, 5, 2, 1, 10, 8, 3)))
    print(tsort((1, 2, 6, 2.2, 8)))
