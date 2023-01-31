class Operation:
    def get_operation():
        operation = input("Введите операцию ")
        while (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
            operation = input("Введите операцию ")
        else:
            return operation
            

        
# Проверка
# op = Operation
# print(op.get_operation())