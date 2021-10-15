"""
Sample Input:
10 3
1 4 8
Sample Output:
9
"""


import sys


def knok_with_gold(W, n, B):
    F = [1]+[0]*W
    #print('B', B, 'F', F)
    for j in B:
        #print('B', j)
        for i in range(W, j-1, -1):
            #print('W', i, 'i-j>0', i-j, i-j<0, 'F[i-j] == 1', F[i-j] == 1 )
            if F[i-j] == 1:
                F[i] = 1
                #print('F', F)
    i = W
    while F[i] == 0:
        i -= 1
    return i


def main():
    reader = (map(int, line.split()) for line in sys.stdin) # Get-Content 8.2_5.0.txt | python  8.2_5.0.py
    W, n = next(reader)
    B = list(next(reader))
    print(knok_with_gold(W, n, B))


if __name__ == "__main__":
    main()
