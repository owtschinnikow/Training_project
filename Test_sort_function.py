def insert_sort(a):
    """ Сортировка списка А вставсками"""
    for top in range(1, len(a)):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


def choise_sort(a):
    """ Сортировка списка A выбором"""
    for pos in range(0, len(a)-1):
        for k in range(pos+1, len(a)):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def buble_sort(a):
    """ Сортировка списка A методом пузырьков"""
    for bypass in range(1, len(a)):
        for k in range(0, len(a) - bypass):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]


def test_sort(sort_algorithm):
    print("Test sort algorithm:", sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print('Ok' if a == a_sorted else 'Fail')

    print('testcase #2: ', end='')
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))
    sort_algorithm(a)
    print('Ok' if a == a_sorted else 'Fail')

    print('testcase #3: ', end='')
    a = [4, 2, 4, 2, 1]
    a_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(a)
    print('Ok' if a == a_sorted else 'Fail', end='\n\n')


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(buble_sort)
