# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнила:
- Кузьмина Анастасия Александровна
- ИВТ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Питоне. Текстовый файл должен состоять минимум из двух строк.

### Результат.
![Меню]()

## Выводы

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
file = open("input1.txt", "r")
print(file.readline())
file.close()
```
### Результат.
![Меню]()

## Выводы
Научились читать построчно из файла.

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при это используйте конструкцию open()/close().

```python
file = open("input1.txt", "r")
print(file.readlines())
file.close()
```
### Результат.
![Меню]()

## Выводы
Научились читать все строчки файла за раз.

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при это используйте конструкцию with open().

```python
with open("input1.txt") as file:
    print(file.readlines())
```
### Результат.
![Меню]()

## Выводы
Научились читать все строчки файла за раз с помощью with open().

## Лабораторная работа №5
### Напишите программу, которая выведет все строки из вашего файла отдельно, при это используйте конструкцию with open().

```python
with open("input1.txt") as file:
    for line in file:
        print(line)
```
### Результат.
![Меню]()

## Выводы
Научились читать файл построчно.

## Лабораторная работа №6
### Напишите программу, которая будет добавлять нову. строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open("input1.txt", "a+") as file:
    file.write(
        "\nNo ore takes better to being forged than the infernal iron of Avernus, where the archdevil Zariel presides."
    )

with open("input1.txt", "r") as file:
    print(file.readlines())
```
### Результат.
![Меню]()

## Выводы
Научились добавлять записи в файл.

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого. Не забудьте проверить, что измененная вами информация сохранилась в файле.

```python
lines = ["line one", "line two", "line three"]
with open("input1.txt", "w") as file:
    for line in lines:
        file.write("\n" + line)
with open("input1.txt", "r") as file:
    for line in file:
        print(line)
```
### Результат.
![Меню]()

## Выводы
Научились переписывать содержимое файла.

## Лабораторная работа №8
### Выберите любую папку на своём компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f"Папка {catalog[0]} содержит:")
        print(f"Директории: {', '.join([folder for folder in catalog[1]])}")
        print(f"Файлы: {', '.join([file for file in catalog[2]])}")
        print("-" * 40)

print_docs("E:\Учёба\Программирование\ПИ")
```
### Результат.
![Меню]()

## Выводы
Научились выводить папки, директории и их содержимое.

## Лабораторная работа №9
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таких несколько). Проверить работоспособность программы на своём наборе данных.

```python
def longestWord(file):
    with open(file, encoding="utf-8") as f:
        words = f.read().split()
        maxLength = len(max(words, key=len))
        for word in words:
            if len(word) == maxLength:
                res = word
        if len(res) == 1:
            return res[0]
        else:
            return res

print(longestWord("input1.txt"))
```
### Результат.
![Меню]()

## Выводы

## Лабораторная работа №10
### Требуется создать csv-файл "rows_300.csv" со следующими столбцами: № - номер по порядку (1-300), Секунда - текущая секунда на вашем ПК, Микросекунда - текущая миллисекунда.

```python
import csv
import datetime
import time

with open("rows_300.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["№", "Секунда", "Микросекунда"])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![Меню]()

## Выводы
Ознакомились с расширением .csv и научились создавать подобные файлы через код.

## Самостоятельная работа №1
### Скорпируйте содержимое любой статьи в файл (не менее 200 слов), напишите программу, которая считает количество слов. 

```python
numWrods = 0
dictionary = {}
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        words = line.split()
        numWrods += len(words)
        for elem in words:
            if elem in dictionary:
                dictionary[elem] += 1
            else:
                dictionary[elem] = 1
print(numWrods)
list = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
print(list[0])
```
### Результат.
![Меню]()

## Выводы
Количество слов подсчитано корректно, программа работает.

## Самостоятельная работа №2
### Напишите программу для учёта доходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль.

```python
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
```
### Результат.
![Меню]()

## Выводы
Информация записывается в файл и выводится в консоль. Программа работает корректно.

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавите, число слов, число строк.

```python
numWrods = 0
numChars = 0
numLines = 0
dictionary = {}
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        numLines += 1
        words = line.split()
        numWrods += len(words)
        for elem in words:
            numChars += sum(map(str.isalpha, elem))
print(numChars)
print(numWrods)
print(numLines)
```
### Результат.
![Меню]()

## Выводы
Научились считать буквы в тексте и строки.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предожение, выводит его в терминал, заменяя все запрещенные слова звездочками *(количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, храняться в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они не были, даже в середине другого слова. Замена производится независимо от регистра.

```python
str = (
    "Hello, world! Python IS the programming language of thE future. My EMAIL is...\n"
    "PYTHON is awesome!!!!"
)
with open("input.txt", "r") as file:
    forbList = list(file.readline().split(" "))
print(forbList)
nlIndex = str.index("\n")
inputList = str.split()
for i in range(len(inputList)):
    for j in range((len(forbList))):
        if forbList[j] in inputList[i].lower():
            for k in forbList[j]:
                inputList[i] = inputList[i].lower().replace(k, "*")

output = ""
for i in inputList:
    output += i + " "
    if len(output) == nlIndex + 1:
        output += "\n"
print(output)
```
### Результат.
![Меню]()

## Выводы
Научились "ценрузить" слова и их части.

## Самостоятельная работа №5
### В файл записаны сведения о сотрудниках некоторой фирмы в виде: Фамилия, Возраст, Профессия. Необходимо вывести всех сотрудников, возраст которых меньше 40.

```python
fout = list()
for st in open("input.txt", "r", encoding="utf-8"):
    intAge = int(st.split()[1])
    if intAge < 40:
        fout.append(st)
print(fout)
```
### Результат.
![Меню]()

## Выводы
Научились сотрировать содержание файла.

## Общие выводы по теме
Обзнакомились с базовыми приёмами и методами работы с фалами в Питоне.