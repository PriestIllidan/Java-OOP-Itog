from CalcGeneral import CalcGeneral
from NumberInt import NummberInt
from Operation import Operation


class CalcInt (CalcGeneral):  # Калькулятор целых чисел
    def calc(self):
        number1 = NummberInt().get_number()
        operation = Operation.get_operation()
        number2 = NummberInt().get_number()
        if (operation == "+"):
            print(f"Результат = {int(number1+number2)}")
        elif (operation == "-"):
            print(f"Результат = {int(number1-number2)}")
        elif (operation == "*"):
            print(f"Результат = {int(number1*number2)}")
        elif (operation == "/"):
            print(f"Результат = {int(number1/number2)}")
