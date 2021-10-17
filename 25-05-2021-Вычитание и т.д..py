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