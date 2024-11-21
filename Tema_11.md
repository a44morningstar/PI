# Тема 1. Итераторы и генераторы
Отчет по Теме #11 выполнила:
- Кузьмина Анастасия Александровна
- ИВТ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Простой итератор без гибкой настройки

```python
nums = [0, 1, 2, 3, 4, 5]
for item in nums:
    print(item)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/lab1.png)

## Выводы
Ознакомились с итераторами в привычных кодах.

## Лабораторная работа №2
### Класс-итератор с гибкой настройкой

```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count


if __name__ == "__main__":
    counter = CountDown(7)
    for i in counter:
        print(i)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/lab2.png)

## Выводы
Создали класс-итератор, рассмотрели его работу.

## Лабораторная работа №3
### Генератор списка

```python
a = [i**2 for i in range(1, 6)]
print("a - ", a)
for i in a:
    print(i)

print("iter(a) - ", iter(a))
for i in a:
    print(i)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/lab3.png)

## Выводы
Составили генератор списка, ознакомились с его работой.

## Лабораторная работа №4
### Выражения-генераторы

```python
b = (i**2 for i in range(1, 6))
print(b)
print("first")
for i in b:
    print(i)
print("second")
for i in b:
    print(i)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/lab4.png)

## Выводы
Ознакомились с выражением-генератором.

## Лабораторная работа №5
### Такой же счётчик, как и в первом задании, только это генератор и использует yield

```python
def countdown(count):
    while count >= 0:
        yield count
        count -= 1


if __name__ == "__main__":
    counter = countdown(7)
    for i in counter:
        print(i)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/lab5.png)

## Выводы
Ознакомились с yield и его использованием в генераторах.

## Самостоятельная работа №1
### Реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield. Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```python
def fib(n):
    counter = 0
    a, b = 1, 1
    print(1)
    print(1)
    while counter < n:
        yield (a + b)
        a, b = b, a + b
        counter += 1


if __name__ == "__main__":
    counter = fib(224)
    for i in counter:
        print(i)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam1.1.png)
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam1.2.png)
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam1.3.png)
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam1.4.png)
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam1.5.png)

## Выводы
Программа реализована, работает корректно.

## Самостоятельная работа №2
### К коду предыдущей задачи добавить запоминание каждого числа Фибоначчи в файл "fib.txt", при этом каждое число должно находиться на отдельной строчке.

```python
def fib(n):
    counter = 0
    a, b = 1, 1
    with open("fib.txt", "a+") as file:
        file.write(str(a) + "\n")
        file.write(str(b) + "\n")
    while counter < n:
        yield (a + b)
        a, b = b, a + b
        counter += 1


if __name__ == "__main__":
    counter = fib(224)
    with open("fib.txt", "a+") as file:
        for i in counter:
            file.write(str(i) + "\n")
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam2.1.png)
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam2.2.png)
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam2.3.png)
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam2.4.png)
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_11/pic/sam2.5.png)

## Выводы
Программа реализована, работает корректно.

## Общие выводы по теме
Изучили итераторы и генераторы, попробовали их на практике.
