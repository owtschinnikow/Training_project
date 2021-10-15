def fib1(n):
    print(n)
    assert n>=0
    print(n)
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


n = int(input())
print(fib1(n))




