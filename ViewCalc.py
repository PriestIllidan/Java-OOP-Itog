from CalcFloat import CalcFloat
from CalcInt import CalcInt


class ViewCalc:
    def click_button():
        print(("Выберите вариант калбкулятора: 1 - целочисленный; 2 - рациональный; 3 - комплексный *Пока нет* 4 - выход"))
        select_calc = input()

        match select_calc:
            case "1":
                calc_int = CalcInt()
                calc_int.calc()
            case "2":
                calc_int = CalcFloat()
                calc_int.calc()
            case "3":
                print("Еще нет решения")
            case "4":
                print("Калькулятор закрыт")
                pass


# Checkimng


calc = ViewCalc
calc.click_button()
