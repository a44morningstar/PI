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
