def gcd(a, b):
    if a == 0:
        return(b)
    elif b == 0:
        return(a)
    else:
        a, b = max(a,b), min(a,b)
        while a!=0 or b!=0:
            a %= b
            if a == 0:
                break
            b %= a
            if b == 0:
                break
        return (max(a,b))
    


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
