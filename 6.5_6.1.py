"""
Sample Input:
2 3
0 5
7 10
1 6 11
Sample Output:
1 0 0

Sample Input:
6 6
0 3
1 3
2 3
3 4
3 5
3 6
1 2 3 4 5 6
Sample Output:
2 3 6 3 2 1

Для тех, кто так и не понял, где здесь применять быструю сортировку и
с какого конца подступиться к этой задаче - небольшая инструкция простыми словами:
1.  Заведите массив L с началами отрезков и отсортируйте быстрой сортировкой
2.  Повторите шаг 1 для концов отрезков - массив R
3.  Напишите 2 функции для искомой точки А:
3.1 1 - будет искать в массиве L все элементы, которые меньше или равны(!)
    А и возвращать их количество LN
3.2 2 -будет искать в массиве R все элементы, которые строго (!) меньше
    А и возвращать их количество RM
4.  В цикле прогоните каждую точку из списка через обе функции -
    ответом будет разность LN - RM
"""


import sys


def dots_and_segments(bounds_and_dots, dots_count):
    """Time complexity: O(k), where k = len(bounds_and_dots) == 2 * n + m"""
    bounds_and_dots.sort()

    result = [0] * dots_count
    current = 0  # current number of started but not finished segments

    for dot in bounds_and_dots:
        current -= dot[1]
        if dot[1] == 0:
            result[dot[2]] = current

    return result


def input_and_processing(reader):
    """Time complexity: O(n + m)"""
    n, m = next(reader)
    bounds_and_dots = []  # left bounds, right bounds and input dots

    for _ in range(n):
        left, right = next(reader)
        bounds_and_dots.append((left, -1))  # -1 means left bound of the segment
        bounds_and_dots.append((right, 1))  # 1 means left bound of the segment

    input_dots = [int(i) for i in next(reader)]

    for i in range(len(input_dots)):
        bounds_and_dots.append((input_dots[i], 0, i))  # 0 means dot, i saves the order of all input dots

    return bounds_and_dots, m


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)

    bounds_and_dots, dots_count = input_and_processing(reader)
    print(*dots_and_segments(bounds_and_dots, dots_count))


if __name__ == '__main__':
    main()
