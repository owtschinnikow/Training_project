A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]

F = [0] * len(A)
for i in range(len(A)):
    for j in range(i):
        if A[j] < A[i] and F[j] > F[i]:
            F[i] = F[j]
    F[i] += 1

print(A, F, sep='\n')

for i in range(1):
    break

