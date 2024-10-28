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
