import random


def spisok(n): #n - количество отрезков
    lst = []
    while len(lst) < n:
        a = random.randint(0, 50) #определяем возможные величины для первой точки отрезка
        b = a + random.randint(1, 10) #определяем возможные длины отрезка и точку конца отрезка
        lst.append([a, b])
    lst = sorted(lst, key = lambda x: x[1])
    list_true = [lst[0]] #Список подходящих отрезков
    [list_true.append(lst[i]) for i in range(n-1) if list_true[-1][1] <= lst[i][0]]
    return (print(lst), print(list_true))




def main():
    while 1 == 1:
        n = int(input())
        print(spisok(n))


if __name__ == "__main__":
    main()
