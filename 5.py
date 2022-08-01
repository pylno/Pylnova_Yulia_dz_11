import datetime
import re


class WareHouse:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__free_space = capacity
        self.__storage = {}

    def acceptance(self, item, number):
        if self.__free_space >= item.volume * number:
            self.__free_space -= item.volume * number
            if item.name in self.__storage.keys():
                self.__storage[item.name] += number
                print(f'На склад было принято {number} штук {item.name}')
                print()
            else:
                self.__storage[item.name] = number
                print(f'На склад было принято {number} штук {item.name}')
                print()
        else:
            print(f"Невозможно принять {item.name} в кол-ве {number} штук,\n"
                  f"поскольку требуемый объем больше свободного на складе места!")
            print()

    def transfer(self, item, number, department):
        if item.name in self.__storage.keys() and number <= self.__storage[item.name]:
            self.__storage[item.name] -= number
            self.__free_space += item.volume * number
            print(f'Со склада в {department} было отправлено {number} штук {item.name}')
            print()
        else:
            print(f"Невозможно отправить со склада {item.name} в кол-ве {number} штук,\n"
                  f"поскольку на складе нет {item.name} в таком кол-ве!")
            print()

    def __str__(self):
        out_lst = []
        for key, value in self.__storage.items():
            out_lst.append(f'{key}, кол-во на складе: {value} \n')
        out_lst.append(f'Общий объем: {self.capacity} \n')
        out_lst.append(f'Свободный объем: {round(self.__free_space, 2)}')
        out_str = ''
        for item in out_lst:
            out_str += item
        return out_str


class Office_Equipment:
    def __init__(self, name, weight, cost, need_repair):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.need_repair = need_repair

    @property
    def volume(self):
        return None


class Printer(Office_Equipment):
    def __init__(self, name, weight, cost, need_repair, has_ink):
        super().__init__(name, weight, cost, need_repair)
        self.has_ink = has_ink
        self._coef = 0.7

    @property
    def volume(self):
        if self.has_ink:
            volume = self._coef + 0.1
        else:
            volume = self._coef
        return volume


class Scanner(Office_Equipment):
    __year = None
    __month = None
    __day = None

    def __init__(self, name, weight, cost, need_repair, production_date):
        super().__init__(name, weight, cost, need_repair)
        assert re.compile(r"^(\d{2}-){2}\d{4}$").match(production_date), f'wrong date {production_date}'
        self.production_date = production_date

    @property
    def volume(self):
        volume = 0.5
        return volume

    @classmethod
    def is_valid(cls, date):
        date_lst = date.split('-')
        cls.__day = int(date_lst[0])
        cls.__month = int(date_lst[1])
        cls.__year = int(date_lst[2])
        if cls.__year < 2017:
            return False
        return True

    @staticmethod
    def validator():
        # Проверка только для примера, по факту должна быть сложнее (меньшее кол-во дней в феврале и т.д.):
        if 0 < Scanner.__day < 32 and 0 < Scanner.__month < 13 and datetime.MINYEAR < Scanner.__year < datetime.MAXYEAR:
            return True
        return False


class Xerox(Office_Equipment):
    def __init__(self, name, weight, cost, need_repair, generation):
        super().__init__(name, weight, cost, need_repair)
        self.generation = generation
        if self.generation == 1:
            self.__speed = 50
        elif self.generation == 2:
            self.__speed = 75
        elif self.generation == 3:
            self.__speed = 100

    @property
    def volume(self):
        volume = 1.2
        return volume


new_warehouse = WareHouse(30)
printer_with_ink = Printer('Принтер с чернилами', 1.5, '15000 руб', False, True)
printer_without_ink = Printer('Принтер без чернил', 1.7, '20000 руб', False, False)
new_scanner = Scanner('Сканер', 0.8, '8000 руб', False, "01-03-2019")
new_xerox = Xerox('Ксерокс 2-го поколения', 4, '34000 руб', False, 2)
new_warehouse.acceptance(printer_with_ink, 4)
new_warehouse.acceptance(printer_without_ink, 3)
new_warehouse.acceptance(new_scanner, 2)
new_warehouse.acceptance(new_xerox, 8)
new_warehouse.acceptance(new_xerox, 2)
new_warehouse.acceptance(new_xerox, 20)
print(new_warehouse)
print()
new_warehouse.transfer(new_scanner, 1, 'Бухгалетрия')
new_warehouse.transfer(printer_without_ink, 3, 'Тех. отдел')
new_warehouse.transfer(new_xerox, 18, 'Менеджмент')
print(new_warehouse)