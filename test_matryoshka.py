def matryoshka(n):
    if n == 1:
        print("Matryoshechka")
    else:
        print("Top of Matryoshka n = ", n)
        matryoshka(n-1)
        print("Bottom of Matryoshka n = ", n)


matryoshka(int(input('input n = ')))