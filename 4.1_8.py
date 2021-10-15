def spisok(n): #n - количество отрезков
    lst = []
    for i in range(n):
        a, b = input().split()
        lst.append([int(a), int(b)])
        #print(lst, 'spisok')
    lst = sorted(lst, key = lambda x: x[1])
    return(lst)


def sortirovka(n):
    lst = []
    r1 = spisok(n)
    lst.append(r1[0][1])
    #print(r1, lst, 'Begin', sep=' - ')
    for i in r1:
        if i[0] > lst[-1]:
            lst.append(i[1])
    #print()
    return(print(len(lst), *lst, sep='\n'))


def main():
    n = int(input())
    sortirovka(n)


if __name__ == "__main__":
    main()
