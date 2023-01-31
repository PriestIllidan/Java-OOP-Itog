from NumberGeneral import NumberGeneral


class NummberInt (NumberGeneral): # класс ввода целых чисел
    def get_number(self):
        number = input("Введите число ")
        while not number.isdigit():
            number = input("Введите число ")
        else:
            return int(number)
