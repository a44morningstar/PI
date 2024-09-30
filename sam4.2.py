from random import *


def main():
    res = randint(1, 6)
    if res == 5 or res == 6:
        print(res)
        print("Вы выиграли")
    elif res == 3 or res == 4:
        print(res)
        main()
    else:
        print(res)
        print("Вы проиграли")

if __name__ == "__main__":
    main()
