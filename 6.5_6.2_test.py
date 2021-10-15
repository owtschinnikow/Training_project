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

from datetime import datetime
import random

def count_left_right_dots(dots, sort_lines_left_righ):
    acc = []
    #print('sort_lines_left_righ[0]', sort_lines_left_righ[0])
    #print('len(sort_lines_left_righ[0])', len(sort_lines_left_righ[0])+2)
    #print('sort_lines_left_righ[1]', sort_lines_left_righ[1])
    for dot in dots:
        base = 0
        for i in range(len(sort_lines_left_righ[0])):
            if sort_lines_left_righ[0][i] <= dot:
                base += 1
            if sort_lines_left_righ[1][i] < dot:
                base -= 1  
        acc.append(base)
    return acc


def sort_lines_left_right(lines, dots):
    lines_left = []
    lines_right = []
    for line in lines:
        lines_left.append(line[0])
        lines_right.append(line[1])
    return lines_left, lines_right


def main():
    n = 4
    #parameters = [int(i) for i in input().split()]
    parameters = [random.randint(0, 10**n), random.randint(0, 10**n)]
    print('parameters', parameters)
    
    #lines = [list(map(int,input().split())) for i in range(parameters[0])]
    #lines = [[random.randint(0, 10**n), random.randint(0, 10**n)] for i in range(parameters[0])]

    lines = []
    for i in range(parameters[0]):
        lines_1 = random.randint(0, 10**n)
        #print('lines_1', lines_1)
        lines_2 = lines_1 + random.randint(0, 10**n - lines_1)
        #print('lines_2', lines_2)
        lines.append([lines_1, lines_2])
    print('lines', lines)

    #dots = [int(i) for i in input().split()]
    dots = [random.randint(0, 10**n) for i in range(parameters[1])]
    print('dots', dots)
    
    t1 = datetime.now()
    #test_sort_lines_left_right = sort_lines_left_right(lines, dots)
    #print('test_sort_lines_left_right', len(sort_lines_left_right(lines, dots)[1]))
    acc = count_left_right_dots(dots, sort_lines_left_right(lines, dots))
    print('acc',acc)
    print(datetime.now() - t1)


if __name__ == '__main__':
    main()
