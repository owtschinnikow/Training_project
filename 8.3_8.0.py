import sys


def levenshtein(A,B):
    F = [[i+j if i*j==0 else 0 for j in range(len(B)+1)] for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[len(A)][len(B)]


def main():
    reader = (line for line in sys.stdin) # Get-Content 8.2_5.0.txt | python  8.2_5.0.py
    A = next(reader)
    B = next(reader)
    print(levenshtein(A,B))


if __name__ == "__main__":
    main()
