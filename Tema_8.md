# Тема 8. Основы ООП
Отчет по Теме #8 выполнила:
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
### Создайте класс "Car" с атрибутами проихводитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. 

```python
class Car:
    #объявляем название класса
    def __init__(self, brand, model):
        self.brand = brand
        self.model=model
    #создаем конструктор, в котором задаем атрибуты объектов данного класса

myCar = Car("Honda", "Mobolio")
#создаем объект класса Car с атрибутами Honda и Mobilio
```
### Результат.
![Меню]()

## Выводы
Научились саздавать классы на Питоне, задавать атрибуты объектов данного класса, создавать объекты.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу.

```python
class Car:
    # объявляем название класса
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    """
    Конструктор задает необходимые артбуты для объектов класса Car
    """

    def drive(self):
        print(f"Driving the {self.brand} {self.model}")

    """
    Метод drive выводит сообщение, что на этой машине едут.
    Вызывается объектом, использует его атрибуты brand и model.
    """


myCar = Car("Honda", "Mobolio")
# создаем объект класса Car с атрибутами Honda и Mobilio
myCar.drive()
# вывзвает метод drive для объекта myCar
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/lab2.png)

## Выводы
Научились создавать методы класса и вызывать их для объектов в коде.

## Лабораторная работа №3
### Создайте новый класс "ElectricCar" с методом "charge" и атрибутом емкость батарени. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу.

```python
from lab2 import Car

# импортируем класс Car из второй лабораторной работы


class ElecricalCar(Car):
    def __init__(self, brand, model, batteryCapacity):
        super().__init__(brand, model)
        self.batteryCapacity = batteryCapacity
        """
        Конструктор задает атрибуты объекта класса ElectricalCarЮ используя super(), чтобы подтянуть атрибуты класса Car
        """

    def charge(self):
        print(f"Charging the {self.brand} {self.model} with {self.batteryCapacity} kWh")
        """
        Выводит сообщение о том, какая машина заряжается, с какой мощностью
        """


myElCar = ElecricalCar("Tesla", "Model 5", 75)
# создаем объект класса ElectricalCar
myElCar.drive()
# используем метод класса Car на объекте ElecrticalCar
myElCar.charge()
# используем метод charge()
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/lab3.png)

## Выводы
Научились реализовывать наследование на Питоне.

## Лабораторная работа №4
### Релизуйте инкапсуляцуию для класса, созданного в первом задании. Создайте защищенный атрубт производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу.

```python
class Car:
    # объявляем название класса
    def __init__(self, brand, model):
        self._brand = brand  # защищенный атрибут
        self.__model = model  # приватный атрибут

    """
    Конструктор задает необходимые артбуты для объектов класса Car
    """

    def drive(self):
        print(f"Driving the {self._brand} {self.__model}")

    """
    Метод drive выводит сообщение, что на этой машине едут.
    Вызывается объектом, использует его атрибуты brand и model.
    """


myCar = Car("Honda", "Mobolio")
# создаем объект класса Car с атрибутами Honda и Mobilio
print(myCar._brand)  # Доступ к защищенному атрибуту будет предоставлен
myCar.drive()
# вывзвает метод drive для объекта myCar
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/lab4.png)

## Выводы
Изучили защищенные и приватные атрибуты.

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу.

```python
class Shape:
    def area(self):
        pass


# создаем класс Shape и определяем метод area() без тела


class Rectangle(Shape):
    # создаем класс Rectangle, наследующий класс Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height

    """
    Конструктор задает атрибуты объекта класса Rectangle
    """

    def area(self):
        return self.width * self.height

    """
    Переопределяем метод area для объектов класса Rectangle
    """


class Circle(Shape):
    # создаем класс Circle, наследующий класс Shape
    def __init__(self, radius):
        self.radius = radius

    """
    Конструктор задает атрибуты объекта класса Circle
    """

    def area(self):
        return 3.14 * self.radius * self.radius

    """
    Переопределяем метод area для объектов класса Circle
    """


shapes = [Circle(17), Rectangle(7, 12)]
# создаем массив, содержащий объект класса Circle и объекст класса Rectangle
for i in shapes:
    print(i.area())
# выводим результаты метода area() для каждого элемента массива
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/lab5.png)

## Выводы
Научились реализовывать полиморфизм на Питоне.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться от теоретичествого материала и лаб. заданий.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


doggo = Dog("Jager", "Rottweiler")
print(f"Welcome, {doggo.name} the {doggo.breed}")
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/sam1.png)

## Выводы
Был создан класс Dog, объекты которого имеют атрбуты name и breed. Создали объекста класса Dog - doggo.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться от теоретичествого материала и лаб. заданий.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")

    def pat(self):
        print(f"{self.name} loves pets!")


doggo = Dog("Jager", "Rottweiler")
print(f"Welcome, {doggo.name} the {doggo.breed}")
doggo.pat()
doggo.bark()
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/sam2.png)

## Выводы
Были созданы методы bark() и pat() у класса Dog.

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться от теоретичествого материала и лаб. заданий.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")

    def pat(self):
        print(f"{self.name} loves pets!")


class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)


class CompanionDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)


doggo1 = GuardDog("Jager", "Rottweiler")
doggo2 = CompanionDog("Willow", "Golden Retriever")
doggo1.bark()
doggo2.pat()
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/sam3.png)

## Выводы
Создали два класса, наследующие класс Dog: GuardDog и CompanionDog.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться от теоретичествого материала и лаб. заданий.

```python
class Dog:
    def __init__(self, name, breed):
        self.__name = name
        self._breed = breed

    def bark(self):
        print("woof woof")

    def pat(self):
        print("Dogs love pets!")


class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)


class CompanionDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)


doggo1 = GuardDog("Jager", "Rottweiler")
doggo2 = CompanionDog("Willow", "Golden Retriever")
doggo1.pat()
print(f"Welcome, the {doggo1._breed}")
print(f"Welcome, the {doggo2._breed}")
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/sam4.png)

## Выводы
Реализовали инкапсуляцию, сделав атрибуты name приватным и breed защищенным. 

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм, продолжая работать с ранее созданным классом. Он должен отличаться от теоретичествого материала и лаб. заданий.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")

    def pat(self):
        print(f"{self.name} loves pets!")


class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def bark(self):
        print(f"{self.breed}s are very scary. Graaah")


class CompanionDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def pat(self):
        print(f"{self.name} wants u to rub his belly")


doggo1 = GuardDog("Jager", "Rottweiler")
doggo2 = CompanionDog("Willow", "Golden Retriever")
doggo1.bark()
doggo2.pat()
```
### Результат.
![Меню](https://github.com/a44morningstar/stuff/blob/Тема_8/pic/sam5.png)

## Выводы
Реализовали полиморфизм через переопределение метода bark() для класса GuardDog и метода pat() для класса CompanionDog.

## Общие выводы по теме
Ознакомились с основами ООП на Питоне, на практике подкрепили новые умения.