import sys
import math

with open('list.txt') as f:
    list_ = [tuple(map(int, line.split())) for line in f]

for a,b,d in list_:
    log = math.log(a,b)
    print(a, b, d, '%.2f' %log, d < log, d>log, end=' -> ')
    if d < log:
        print('O(n**{})'.format(log))
    elif d > log:
        print('O(n**{})'.format(d) if d else 'O(1)')
    elif 1 == d:
        print('O(n * log n)')
    else:
        print('O(n**{} * log n)'.format(d) if d else 'O(log n)')