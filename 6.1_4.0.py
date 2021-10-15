"""
Sample Input:

5 1 5 8 12 13
5 8 1 23 1 11
Sample Output:

3 1 -1 1 -1
"""

import heapq
import sys
import time

def finde_number(n, a_list, k, b_list):
    acc = []
    for i in b_list:
        l = 0
        r = n-1
        while l <= r:
            m = int(l + (r-l)/2)
            if a_list[m] == i:
                acc.append(m+1)
                break
            elif a_list[m] > i:
                r = m - 1
            else:
                l = m + 1
        if l > r:
            acc.append(-1)
    return acc


def main():
    n, *a_list = map(int, input().split())
    k, *b_list = map(int, input().split())
    number = finde_number(n, a_list, k, b_list)
    print(*number)   

    
if __name__ == "__main__":
    main()
