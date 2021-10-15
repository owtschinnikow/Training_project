"""


Первая строка содержит количество предметов 1 \le n \le 10^31≤n≤10 3
  и вместимость рюкзака 0 \le W \le 2 \cdot 10^60≤W≤2⋅10 6
 . Каждая из следующих nn строк задаёт стоимость 0 \le c_i \le 2\cdot 10^60≤c i≤2⋅106
  и объём 0 \lt w_i \le 2\cdot 10^60<w i​ ≤2⋅106   предмета (nn, WW, c_ic i  , w_iw i
​  — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000

return f"{result:.3f}"
'{:.3f}'.format(x)

"""


def spisok(n): #n - количество отрезков
    lst = []
    for i in range(n):
        a, b = input().split()
        lst.append([int(a), int(b)])
        #print(lst, 'first spisok')
    lst = sorted(lst, key = lambda x: x[0]/x[1], reverse=True)
    #print(lst, 'sorted')
    return(lst)


def sortirovka(n, m):
    lst = []
    #r1 = [[120, 30], [60, 20], [100, 50]]
    r1 = spisok(n)
    for i in r1:
        #print(i, ' - ', r1, ' - ', lst)
        if (m - i[1]) == 0: #space is
            lst.append(i)
            m = m - i[1]
            #break
        elif (m - i[1]) > 0:  #space down
            lst.append(i)
            m = m - i[1]    
        elif (m - i[1]) < 0 and m !=0 :  #space devorsed
            #print (m, i[0], i[1], 'm')
            i[0], i[1] = (i[0]/i[1])*m, m
            lst.append(i)
            m = m - i[1]   
    summa = 0
    for i in lst:
        summa += i[0]
    return(print( "%.3f"%summa))


def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    sortirovka(n, m)


if __name__ == "__main__":
    main()
