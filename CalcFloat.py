from CalcGeneral import CalcGeneral
from NumberFloat import NummberFloat
from Operation import Operation


class CalcFloat (CalcGeneral):  # калькулятор рациональных чисел
    def calc(self):
        number1 = NummberFloat().get_number()
        operation = Operation.get_operation()
        number2 = NummberFloat().get_number()
        if (operation == "+"):
            print(f"Результат = {number1+number2}")
        elif (operation == "-"):
            print(f"Результат = {number1-number2}")
        elif (operation == "*"):
            print(f"Результат = {number1*number2}")
        elif (operation == "/"):
            print(f"Результат = {number1/number2}")
