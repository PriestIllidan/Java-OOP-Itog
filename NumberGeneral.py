from abc import ABC, abstractmethod


class NumberGeneral(ABC): # абстрактный класс ввода чисел
    def __init__(self):  # инициализируем класс
        super().__init__()

    @abstractmethod
    def get_number(self):
        pass