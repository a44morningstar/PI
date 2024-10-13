def delTp(tp, num):
    tempList = list(tp)
    for elem in tp:
        if elem == num:
            tempList.remove(elem)
            break
    return tuple(tempList)


if __name__ == "__main__":
    tp = tuple
    print(delTp((2, 4, 6, 6, 4, 2), 9))
    print(delTp((2, 4, 6, 6, 4, 2), 6))
