def func(x):
    try:
        print(2 + int(x))
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число")


if __name__ == "__main__":
    func(input("Введите число: "))
