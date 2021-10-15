"""
Sample Input:
4
3 6 7 12
Sample Output:
3

Пример для отладки (вход)
3 6 12 7 9 24 18 3 9 24
Список подпоследовательностей
[1, 2, 3, 1, 2, 4, 3, 2, 3, 5]
Ответ:
5
"""

import sys


def longest_consecutive_multiple_subsequence(A):
    max_F = 0
    F = [0] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if ((A[i] % A[j])  == 0) and F[j] > F[i]:
                F[i] = F[j]
        F[i] += 1
        max_F = max(F[i], max_F)
    #print(A, F, sep='\n')
    return max_F

def main():
    reader = (map(int, line.split()) for line in sys.stdin) # Get-Content 8.2_5.0.txt | python  8.2_5.0.py
    n = next(reader)
    queries = list(next(reader))
    print(longest_consecutive_multiple_subsequence(queries))


if __name__ == "__main__":
    main()