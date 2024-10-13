def move_zeros(new_list):
    c = 0
    for i in range(len(new_list)):
        if new_list[i] != 0:
            new_list[c] = new_list[i]
            c += 1
    for k in range(c, len(new_list)):
        new_list[k] = 0
    return new_list


if __name__ == "__main__":
    my_list = [2, 0, 6, 0, 4, 3, 1, 4, 7, 0, 8, 2, 8]
    print(move_zeros(my_list))
