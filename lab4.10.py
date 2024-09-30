global res


def rect():
    a = float(input("Высота - "))
    b = float(input("Ширина - "))
    global res
    res = a * b


def tri():
    a = float(input("Основание - "))
    h = float(input("Высота - "))
    global res
    res = 0.5 * a * h


choice = input("1-rectangle, 2-triangle ")
if choice == "1":
    rect()
elif choice == "2":
    tri()
print(res)
