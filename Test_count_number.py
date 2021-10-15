def is_simple_number(x):
    """ Определяетб является ли число простым.
        x - целое положительное число.
        Если простоеб то возвращает Thrue
        а иначе - False
    """
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor += 1
    return True


def factorize_number(x):
    """ Раскладывает число на множителм.
        Печатает их на экран.
        x - целое положительное число

    """
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1

input()