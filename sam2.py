import datetime

choice = input("1. Ввести новую информацию \n2. Вывести информацию из файла\n")
if choice == "1":
    sum = input("Сумма: ")
    name = input("Название траты: ")
    date = datetime.date.today()
    with open("input.txt", "a+") as file:
        file.write(f"{sum} - {name}, дата: {date}\n")
elif choice == "2":
    with open("input.txt", "r") as file:
        for line in file:
            print(line)
