# Тема 10. Декораторы и исключения
Отчет по Теме #10 выполнила:
- Кузьмина Анастасия Александровна
- ИВТ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Написать программу, которая будет считать числа Фибоначчи для 100 и запустить её без декоратора и с ним, посмотреть разницу во времени. При запуске без декоратора для наглядности хватит 10 секунд ожидания.

```python
from functools import lru_cache


@lru_cache(None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(100))
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/lab1.png)

## Выводы
Работа программы с декоратором значительно быстрее.

## Лабораторная работа №2
### Написать декоратор для функции, который будет принимать все параметры и проверять, чтобы возраст был больше 0 и меньше 130.

```python
def check(input_func):
    def output_func(*args):
        name, age = (
            args[0],
            args[1],
        )

        if age < 0 or age > 130:
            age = "Wrong input"
        input_func(name, age)

    return output_func


@check
def personal_info(name, age):
    print(f"Name: {name} Age: {age}")


if __name__ == "__main__":
    personal_info("Tom", 52)
    personal_info("Rudy", -1)
    personal_info("Lora", 131, 0, 4, 5)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/lab2.png)

## Выводы
Деоратор сделан, программа работает корректно.

## Лабораторная работа №3
### Написать исключения для функции, чтобы неподходящий тип данных не ломал код.

```python
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as e:
        print(e)
    finally:
        print("Information has been processed")


if __name__ == "__main__":
    data([10, -1, "Grgr", "Monkey", "f", "low", 100])
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/lab3.png)

## Выводы
Исключение сделано, программа работает корректно.

## Лабораторная работа №4
### Написать исключение, которое будет вызываться в случае, если в функцию проверки имени при регистрации передана строка длиннее десяти символов, а если имя имеет допустимую длину, то в консоль выводится "Успешная регистрация"

```python
class NegativeValueException(Exception):
    pass


def check_name(name):
    if len(name) > 10:
        raise NegativeValueException("Name is bigger than 10 simbols")
    else:
        print("Successful")


if __name__ == "__main__":
    name = "12345678910"
    check_name(name)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/lab4.png)

## Выводы
Исключение работае корректно.

## Лабораторная работа №5
### Создать логгер, вывести все логи в консоль.

```python
class SiteChecker:
    def __init__(self, func):
        print("> Класс SiteChecker метод __init__: успешный запуск")
        self.func = func

    def __call__(self):
        print("> Проверка перед запуском", self.func.__name__)
        self.func()
        print("> Проверка безопасного включения")


@SiteChecker
def site():
    print("Усердная работа сайта")


if __name__ == "__main__":
    print(">> Сайт запущен")
    site()
    print(">> Сайт выключен")
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/lab5.png)

## Выводы
Логгер создан, логи отображаются в консоли, программа работает корректно.

## Самостоятельная работа №1
### Написать декоратор для функции, который будет выяснять за какое время она выполняется.

```python
import time


def fib():
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=" ")


if __name__ == "__main__":
    a = time.time()
    fib()
    b = time.time()
    print(f"\nПрограмма выполнялась {int((b - a) * 1000)} миллисекунд")
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/sam1.png)

## Выводы
Время работы вычислено, программа выполняется корректно.

## Самостоятельная работа №2
### Написать код, который будет вызывать исключение, если файл пустой, и выводить информацию из файла, если нет.

```python
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
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/sam2.png)

## Выводы
Программа работает корректно.

## Самостоятельная работа №3
### Написать функцию, которая складывает 2 и введенное пользователем число, но если пользователь введет строку или другой неподходящий тип данных, то в консоль выведется ошибка.

```python
def func(x):
    try:
        print(2 + int(x))
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число")


if __name__ == "__main__":
    func(input("Введите число: "))
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/sam3.png)

## Выводы
Тесты проведены, программа работает корректно.

## Самостоятельная работа №4
### Cоздать свою программу с использованием декоратора на двух функциях.

```python
def convert_to_data_type(data_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return data_type(result)

        return wrapper

    return decorator


@convert_to_data_type(int)
def add_numbers(x, y):
    return x + y


@convert_to_data_type(str)
def concatenate_strings(x, y):
    return x + y


result = add_numbers(100, 1)
print("Result:", result, type(result))

result = concatenate_strings("Sleepy", "Head")
print("Result:", result, type(result))
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/sam4.png)

## Выводы
Программа складывает входящие данные, выводит сумму и тип данных. Декоратор был использован для вывода типа данных.

## Самостоятельная работа №5
### Создать свою программу с использованием исключения.

```python
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
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_10/pic/sam5.png)

## Выводы
Программа имеет две функции, для каждой их которых сделано собственное исключение: деление на ноль и не найденных файл. Исключения работают корректно.

## Общие выводы по теме
Узнали о декораторах, применили их на практике, ознакомились со структурой и применением исключений в Питоне.