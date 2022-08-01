import datetime
import re


class WareHouse:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__free_space = capacity

    def acceptance(self, item):
        self.__free_space -= item.__volume


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