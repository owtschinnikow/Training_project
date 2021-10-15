"""
Sample Input:
5
2 3 9 2 9
Sample Output:
2 2 3 9 9
"""


def count_sort_dots(parameter, dots, M):
    b = [0]*M
    #print('b', b)
    a = [0]*len(dots)
    #print('a', a)
    for j in range(parameter):
        b[dots[j]-1] += 1
    #print('b', b)
    for i in range(1,M):
        b[i] = b[i] + b[i-1]
    #print('b', b)
    for j in range(parameter-1, -1, -1):
        #print('j', j)
        #print('dots[j]-1', dots[j]-1)
        #print('b[dots[j]-1]-1', b[dots[j]-1]-1)
        a[b[dots[j]-1]-1] = dots[j]
        b[dots[j]-1] = b[dots[j]-1] - 1
    return a


def main():
    parameter = int(input())
    #print('parameter', parameter)
    dots = [int(i) for i in input().split()]
    #print('dots', dots)
    M = 10
    sort_dots = count_sort_dots(parameter, dots, M)
    print(*sort_dots)

        
if __name__ == '__main__':
    main()
