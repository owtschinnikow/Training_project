import time
from matplotlib import pyplot as plt

def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()

def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def qfib(n, with_next=False):    
    if n < 2:
        response = [n, 1]
    else:
        fa, fb = qfib(n//2, with_next=True)
        if n % 2 == 1:
            response = [fa**2 + fb**2,
                        fb * (fb + fa) + fa * fb,]
        else:
            response = [fa * (fb - fa) + fa * fb,
                        fa**2 + fb**2]
    if with_next:
        return response
    return response [0]
    

def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0+f1
    return f1


def main():
    n = int(input())
    print(fib3(n))
    print()
    print(timed(fib3, n))
    print(qfib(n))
    print()
    print(timed(qfib, n))
    compare((fib3, qfib), list(range(0, 1000, 100)))


if __name__ == "__main__":
    main()

