def calc(a, b, operation):
    # Задаем дефолтное значение возвращаемого результата
    result = 'Операция не поддерживается'

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        # Проверка деления на ноль
        if b is not 0:
            result = a / b
        else:
            result = 'Деление на 0!'

    # Возвращаем результат выполнения функции
    return result


# Чтоэто за блок читаем гуглим (например https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
if __name__ == "__main__":
    print(calc(5, 8, '+'))  # вызываем фунцию калькулятора для сложение 5 и 8
    print(calc(5, 8, '-'))  # вызываем фунцию калькулятора для вычитания 5 и 8
    print(calc(5, 8, '*'))  # вызываем фунцию калькулятора для умножения 5 и 8
    print(calc(5, 8, '/'))  # вызываем фунцию калькулятора для деления 5 и 8
    print(calc(5, 0, '/'))  # вызываем фунцию калькулятора для деления 5 и 0
