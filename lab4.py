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
