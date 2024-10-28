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
