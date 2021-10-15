"""
Sample Input:

5
2 3 9 2 9
Sample Output:

2
"""

import heapq



def MergeSort(a_list, l, r):
    if l < r:
        m = (l+r)//2
        return Merge(MergeSort(a_list, l, m), MergeSort(a_list, m+1, r))
        


def Merge(a, b):
    acc = []
    while a and b:
        if a[0] <= b[0]:
            acc.append(a.pop(0))
        else:
            acc.append(b.pop(0))
            k += len(a)

    
    return acc, k


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    l = 0
    r = len(a_list)-1
    
    print('Input')
    print(a_list)
    print(l)
    print(r)
    print()
    print('Out')
    number = MergeSort(a_list, l, r)
    print(number)

    
if __name__ == "__main__":
    main()



