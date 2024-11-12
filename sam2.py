def check_file(name):
    try:
        f = open(name)

        f_str = f.readlines()
        f_str[0] = f_str[0]
        for i in f_str:
            print(i, end="\n")
    except:
        print("Файл пустой")


if __name__ == "__main__":
    check_file("input1.txt")
    check_file("input2.txt")
