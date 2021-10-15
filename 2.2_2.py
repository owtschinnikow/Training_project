def fib_digit(n):
    sqrt5 = 5 ** 0.5
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    d = int((phi ** n - psi ** n) / sqrt5)
    d = str(d)
    return(d[-1])


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
