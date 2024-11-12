def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Ошибка деления на ноль:", e)
        return None
    else:
        return result


def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Файл {filename} не найден:", e)
        return ""
    else:
        return content


print(divide(101, 0))
print(read_file("nonexistent.txt"))
