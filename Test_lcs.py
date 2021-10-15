def lcs(A,B):
    """ Наибольшая общая последовательность"""
    F = [[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]

def gis(A):
    """Наибольшая возрастающая подпоследовательность"""
    F = [0] * (len(A)+1)
    for i in range(1, len(A)+1):
        m = 0
        for j in range(0, 1):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F


def main():
    A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    B = list(reversed(A))
    print(A, B, lcs(A,B), gis(A), sep="\n")


if __name__ == "__main__":
    main()