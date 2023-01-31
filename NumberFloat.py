from NumberGeneral import NumberGeneral


class NummberFloat (NumberGeneral): # класс ввода рациональных чисел
    def get_number(self):
        number = input("Введите число ")
        while number.isalpha():
            number = input("Введите число ")
        else:
            return float(number)