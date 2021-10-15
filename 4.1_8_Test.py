r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

print(' _________________________- ')
for i in r:
    print(i, 'i', sep=' - ')
    r.remove(i)
    print(r, 'r', sep=' - ')


r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

print(' _________________________- ')
for i in range(len(r)):
    print(i, 'i', len(r), 'len(r)', sep=' - ')
    r.remove(r[i])
    print(r, 'r', sep=' - ')
