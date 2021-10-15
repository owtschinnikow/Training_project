def min_coins(number):
    coins = [25, 10, 5, 1]
    change = []
    for coin in coins:
        if (number >= coin):
            change += [coin] * (number // coin)
            number = number % coin
    return change
number = int(input())
change = min_coins(number)
print(len(change))
print(*change, sep=' ')
