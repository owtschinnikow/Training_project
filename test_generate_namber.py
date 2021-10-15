def gen_bin(M, prefix=''):
    if M == 0:
        print(prefix, sep='__________')
        return
    for digit in '0', '1':
        gen_bin(M-1, prefix+digit)

#__________________________________________________



def generate_number(N:int, M:int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащими нулями)
    в N-ричной системе счисления (N<=10)
    Длинны M

    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        #print('prefix.append = ', prefix)
        generate_number(N, M-1, prefix)
        #print('prefix.pop = ', prefix)
        prefix.pop()
        #print('prefix.pop = ', prefix)


#__________________________________________________

def find(number, A):
    """
    Ищет number в A и возвращает True, если такой есть
    False, еслит такого нет.
    """
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag


def generate_permutations(N:int, M:int=-1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях
    с префиксом prefix
    """
    M = N if M == -1 else M #по умолчанию N чисел в Т позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()





#Только для двоичной Системы Счисления:
#gen_bin(2)

#Для произвольной Системы Счисления:
#generate_number(2, 2)

#Генерация всех перестановок:
generate_permutations(2)