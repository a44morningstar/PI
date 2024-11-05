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
