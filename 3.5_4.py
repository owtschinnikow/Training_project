def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0+f1



def main():
    n = int(input())
    print(fib3(n))


if __name__ == "__main__":
    main()
