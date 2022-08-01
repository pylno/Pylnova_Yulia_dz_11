import re
import datetime


class Date:
    __year = None
    __month = None
    __day = None

    def __init__(self, date_str):
        assert re.compile(r"^(\d{2}-){2}\d{4}$").match(date_str), f'wrong date {date_str}'
        self.date_str = date_str

    @classmethod
    def convert_date(cls, date):
        date_lst = date.split('-')
        cls.__day = int(date_lst[0])
        cls.__month = int(date_lst[1])
        cls.__year = int(date_lst[2])
        # Вывод для проверки:
        print(
            f'день - {cls.__day}, тип - {type(cls.__day)}, месяц - {cls.__month}, тип - {type(cls.__month)}, '
            f'год - {cls.__year}, 'f'тип - {type(cls.__year)}')

    @staticmethod
    def validator():
        # Проверка только для примера, по факту должна быть сложнее (меньшее кол-во дней в феврале и т.д.):
        if 0 < Date.__day < 32 and 0 < Date.__month < 13 and datetime.MINYEAR < Date.__year < datetime.MAXYEAR:
            return True
        return False


Date.convert_date('01-02-1995')
print(Date.validator())

date_in = Date('01-12-2022')
date_in.convert_date(date_in.date_str)
print(Date.validator())

date_in = Date('32-12-2020')
date_in.convert_date(date_in.date_str)
print(Date.validator())