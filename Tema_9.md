# Тема 9. Концепции и принципы ООП
Отчет по Теме #9 выполнила:
- Кузьмина Анастасия Александровна
- ИВТ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | - |
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
### Написать класс, который будет проверять угадал ваше имя человек или нет. 

```python
class Ana:
    __slots__ = ["name"]

    def __init__(self, name):
        if name == "Ana":
            self.name = f"Yes, I'm {name}"
        else:
            self.name = f"No, I'm not {name}, I'm Ana"


print(Ana("Diana").name)
print(Ana("Ana").name)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_9/pic/lab1.png)

## Выводы
Класс реализован, программа работает корректно.

## Лабораторная работа №2
### Написать класс, в котором будет определяться изменили ли состав мороженого или нет.

```python
class iceCream:
    def __init__(self, top=None):
        if isinstance(top, str):
            self.top = top
        else:
            self.top = None

    def answer(self):
        if self.top:
            print(f"{self.top} ice cream")
        else:
            print("Plain ice cream")


ic = iceCream()
ic.answer()
ic = iceCream("Cherry")
ic.answer()
ic = iceCream(727)
ic.answer()
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_9/pic/lab2.png)

## Выводы
Класс реализован, программа работает корректно.

## Лабораторная работа №3
### Реализовать инкапсуляцию с сеттером, геттером и декструктором. Объяснить, почему код в примере не работает.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        if hasattr(self, "_value"):
            return self._value
        else:
            raise AttributeError("Атрибут был удален.")

    def del_value(self):
        if hasattr(self, "_value"):
            del self._value

    value = property(get_value, set_value, del_value, "Свойство value")


obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()  # Удаляет атрибут _value
try:
    print(obj.get_value())  # Ошибка, так как атрибут _value уже удалён
except AttributeError as e:
    print(e)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_9/pic/lab3.png)

## Выводы
Ошибка в коде примера была в том, что после удаления атрибута Петя пытался вызвать несуществующую вещь. В качестве исправления в геттер добавили проверку на наличие атрибута, а в выводе атрибута после удаления добавили уведомление, которое ловит ошибку и выводит на экран "Атрибут удален".

## Лабораторная работа №4
### Написать три класса: Кошки, Собаки, Млекопитающие. Реализовать наследование, добавть атрибут кошкам и собакам, чтобы показать, чем они отличаются.

```python
class Mammal:
    animalClass = "Mammal"


class Dog(Mammal):
    family = "Canine"
    species = "Dog"


class Cat(Mammal):
    family = "Feline"
    species = "Cat"


print(
    f"Dogs are belong to class {Dog().animalClass}s, family {Dog().family}s and species {Dog().species}s"
)
print(
    f"Cats are belong to class {Cat().animalClass}s, family {Cat().family}s and species {Cat().species}s"
)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_9/pic/lab4.png)

## Выводы
Наследование реализовано, программа работает корректно. 

## Лабораторная работа №5
### Реализовать программу с полиморфизмом, которая будет помогать переводить приветствия для разных языков. 

```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")


class English:
    @staticmethod
    def greeting():
        print("Hello")


class Spanish:
    @staticmethod
    def greeting():
        print("Hola")


def greet(lang):
    lang.greeting()

Ana = Russian()
Tom = English()
Juan = Spanish()
greet(Ana)
greet(Tom)
greet(Juan)
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_9/pic/lab5.png)

## Выводы
Ознакомились со статическими методами и их использованием. Программа работает корректно.

## Самостоятельная работа №1
### Создать классы по описанию задания "Садовник и помидоры". Выполнить следующие тесты:
### 1. Вызвать справку по садоводству
### 2. Создать объекты классов Gardener и TomatoBrush
### 3.Используя объект класса Gardener, поухаживать за кустом с помидорами.
### 4. Попробовать собрать урожай, когда томаты ещё не дозрели. Продолжить за ними ухаживать.
### 5. Собрать урожай.

```python
class Tomato:
    states = {"Отсутствует": 0, "Цветение": 1, "Зеленый": 2, "Красный": 3}

    def __init__(self, index):
        self._index = index  # защищенное свойство
        self._state = self.states["Отсутствует"]  # защищенное свойство

    """
    Конструктор
    Атрибуты: индекс помидора, статус - по умолчанию Отуствует у всех 
    """

    def grow(self):
        if self._state < 3:
            self._state += 1

    """
    Повышает статус помидора (зрелость)

    """

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False

    """
    Проверяет статус помидор, если дозрели - Тру, елсе - Фолз
    """


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    """
    Атрибут - объекты класса Томат - помидоры на кусте
    """

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    """
    Все помидоры куста растут
    """

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    """
    Возвращает Тру, если помидоры на кусте дозрели, else False
    """

    def give_away_all(self):
        self.tomatoes = []

    """
    Очищаем куст от помидор
    """


class Gardener:
    def __init__(self, name, plant):
        self.name = name  # публичное свойство
        self._plant = plant  # защищенное свойство

    """
    Конструктор Садовника
    Атрибуты: Имя и его растения
    """

    def work(self):
        self._plant.grow_all()

    """
    При работе садовника, куст растёт на 1
    """

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Урожай собран")
            self._plant.give_away_all()
        else:
            print("Урожай не готов к сбору")

    """
    Проверяем статус помидоров, если Красные, то собираем урожай, если не дозрели, выводим уведомление
    """

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Регулярно поливать и подпитывать растения")
        print("2. Избавляться от старых и заболевших частей растения")
        print("3. Регулярно протирать пыль с растений и следить за влажностью")

    """
    Статический метод, выдает справку по садоводству
    """


Gardener.knowledge_base()  # Вызываем Справку по садоводству
tBush = TomatoBush(3)  # Добавляем три куста с помидорами
gardener = Gardener("Tom", tBush)  # Создаем Садовника
gardener.work()  # Садовник работает
gardener.harvest()  # Пробуем собрать урожай
for item in tBush.tomatoes:  # Смотрим статус помидоров
    print(item._state)
while (
    tBush.all_are_ripe() == False
):  # в цикле садовник работает, пока все помидоры не дозреют
    gardener.work()
gardener.harvest()  # Собираем урожай
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_9/pic/sam.png)

## Выводы
Необходимые классы были созданы с указанными методами. Тесты проведены успешно, программа работает корректно.

## Общие выводы по теме
Укрепили знания ООП на Питоне, рассмотрели применения принципов ООП в программах.