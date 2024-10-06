def replace(list):
    list[0], list[len(list) - 1] = list[len(list) - 1], list[0]
    return list

print(replace([2, 5, 6, 11, 20]))
