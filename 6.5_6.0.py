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


def count_n_for_dots(count_left, count_right):
    acc = list(map(lambda x,y: x-y, count_left, count_right))
    return acc


##def count_right_dots(dots, sort_lines_right):
##    acc = []
##    for dot in dots:
##        base = 0
##        for line_left in sort_lines_right:
##            if line_left < dot:
##                base += 1
##        acc.append(base)
##    return acc


def count_left_right_dots(dots, sort_lines_left_righ):
    acc = []
    for dot in dots:
        base = 0
        for i in range(len(sort_lines_left_righ[0]):
            if sort_lines_left_righ[0][i] <= dot:
                base += 1
            if sort_lines_left_righ[1][i] < dot:
                base -= 1  
        acc.append(base)
    return acc


##def sort_lines_right(parameters, lines, dots):
##    lines_right = []
##    for line in lines:
##        lines_right.append(line[1])
##    #lines_right.sort()
##    return lines_right


def sort_lines_left_right(lines, dots):
    lines_left = []
    lines_right = []
    for line in lines:
        lines_left.append(line[0])
        lines_right.append(line[1])
    #lines_left.sort()
    return lines_left, lines_right


def main():
    parameters = [int(i) for i in input().split()]
    lines = [list(map(int,input().split())) for i in range(parameters[0])]
    dots = [int(i) for i in input().split()]
    #lines_left, lines_right = sort_lines_left_right(lines, dots)
    #print('lines_left, lines_right', lines_left, lines_right)
    acc = count_left_right_dots(dots, sort_lines_left_right(lines, dots))
    print(*acc)
    #count_left = count_left_dots(dots, sort_lines_left(parameters, lines, dots))
    #print('count_left', count_left)
    #count_right = count_right_dots(dots, sort_lines_right(parameters, lines, dots))
    #print('count_right', count_right)
    #n_for_dots = count_n_for_dots(count_left, count_right)
    #print('n_for_dots', *n_for_dots)
    #print(*n_for_dots)
    #n_for_dots = count_n_for_dots(parameters, lines, dots)
    #print('*n_for_dots', *n_for_dots)

    
if __name__ == '__main__':
    main()
