def factorize_number(n :int):
    assert n >= 0, "Факториал числа не определён"
    if n == 0:
        return 1
    return factorize_number(n-1)*n

print(factorize_number(8))

