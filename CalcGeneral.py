from abc import ABC, abstractmethod


class CalcGeneral (ABC):  # создаем абстрактный класс
    def __init__(self):  # инициализируем класс
        super().__init__()

    @abstractmethod  # создаем абстрактную функицию через декоратор
    def calc(self):
        pass