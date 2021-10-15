def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else: # a < b
        return gcd(a, b-a)

def gcd_1(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_2(a, b):
    return a if b == 0 else gcd(b, a % b)
