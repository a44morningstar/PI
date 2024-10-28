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
