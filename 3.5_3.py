from functools import lru_cache

def memo(f):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

@lru_cache(maxsize=None)#@memo # ИЛИ также можно заменить эту строчку на @lru_cache(maxsize=None) 
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)



def main():
    n = int(input())
    print(fib1(n))


if __name__ == "__main__":
    main()
