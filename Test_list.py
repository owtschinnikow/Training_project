a = list(range(int(input())))
b = [-x**2 if x**2 <= 400 else x**2 for x in a if x % 2 == 0]
print(b)

