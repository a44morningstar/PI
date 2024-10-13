def dict_maker(str):
    new_dict = dict([])
    for letter in str:
        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1
    new_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
    new_list = list(new_dict)
    print(new_dict)
    res = dict()
    for i in range(3):
        res[new_list[i]] = new_dict[new_list[i]]
    return dict(sorted(res.items()))

if __name__ == "__main__":
    print(dict_maker("10065314615382404405"))
